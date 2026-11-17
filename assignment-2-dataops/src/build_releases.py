
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

BASE_RAW = ROOT / "data/raw/synthetic_dataset.csv"
NEW_RAW = ROOT / "data/raw/synthetic_dataset_v1.1.0.csv"

BASE_OUTPUT = ROOT / "data/processed/controlled_dataset.csv"
NEW_OUTPUT = ROOT / "data/processed/controlled_dataset_v1.1.0.csv"

CONTRACT = ROOT / "metadata/data_contract.json"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path):
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames, list(reader)


def write_json(relative_path, data):
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2) + "\n",
        encoding="utf-8"
    )


def run_pipeline(source):
    # Run existing scripts in an isolated temporary project.
    # This keeps the original raw input unchanged.
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "assignment-2-dataops"

        required = [
            "src/ingest.py",
            "src/preprocess.py",
            "tests/test_data_quality.py",
            "metadata/data_contract.json"
        ]

        for relative in required:
            destination = work / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, destination)

        staged_raw = work / "data/raw/synthetic_dataset.csv"
        staged_raw.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, staged_raw)

        for script in ["ingest.py", "preprocess.py"]:
            result = subprocess.run(
                [sys.executable, str(work / "src" / script)],
                cwd=work,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                raise RuntimeError(
                    script + " failed:\n" + result.stderr
                )

        result = subprocess.run(
            [
                sys.executable, "-m", "unittest",
                "discover", "-s", "tests",
                "-p", "test_data_quality.py", "-v"
            ],
            cwd=work,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(
                "Data quality tests failed:\n"
                + result.stdout + result.stderr
            )

        print("PASS: Pipeline and 9 tests for", source.name)

        return (
            work / "data/processed/controlled_dataset.csv"
        ).read_bytes()


def create_release(version, raw_path, output_path, change):
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    _, rows = read_csv(raw_path)

    commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        text=True
    ).strip()

    timestamp = datetime.now(timezone.utc).isoformat()
    distribution = dict(Counter(r["risk_label"] for r in rows))

    manifest = {
        "release_id": f"student-academic-risk-{version}",
        "release_version": version,
        "schema_version": contract["schema_version"],
        "contract_version": contract["contract_version"],
        "source_identifier": str(raw_path.relative_to(ROOT)),
        "source_sha256": sha256(raw_path),
        "processed_identifier": str(output_path.relative_to(ROOT)),
        "processed_sha256": sha256(output_path),
        "row_count": len(rows),
        "class_distribution": distribution,
        "code_commit": commit,
        "parameters": {
            "original_generation_seed": 42,
            "risk_rule_version": "1.0.0",
            "transformation": "validated ingestion and performance_change"
        },
        "change_description": change,
        "created_at_utc": timestamp,
        "approval_record": "docs/change_record.md"
    }

    lineage = {
        "release_id": manifest["release_id"],
        "schema_version": contract["schema_version"],
        "source_identifier": manifest["source_identifier"],
        "source_sha256": manifest["source_sha256"],
        "steps": [
            {
                "step": 1,
                "script": "src/ingest.py",
                "action": "Validate and standardize raw values",
                "output": "data/staging/validated_input.csv"
            },
            {
                "step": 2,
                "script": "src/preprocess.py",
                "action": "Sort rows and calculate performance_change",
                "output": manifest["processed_identifier"]
            }
        ],
        "execution_note": (
            "src/build_releases.py stages the selected source "
            "as synthetic_dataset.csv in an isolated workspace."
        ),
        "processed_sha256": manifest["processed_sha256"],
        "code_commit": commit,
        "created_at_utc": timestamp
    }

    return manifest, lineage


def main():
    assert BASE_RAW.is_file(), "Baseline raw dataset missing."
    assert CONTRACT.is_file(), "Data contract missing."

    columns, rows = read_csv(BASE_RAW)

    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    expected = [field["name"] for field in contract["fields"]]

    assert columns == expected, "Unexpected baseline schema."
    assert len(rows) == 120, "Expected 120 baseline records."

    original_hash = sha256(BASE_RAW)

    # Rebuild the baseline using the submitted pipeline.
    baseline_bytes = run_pipeline(BASE_RAW)
    BASE_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    BASE_OUTPUT.write_bytes(baseline_bytes)

    # Controlled schema-compatible change: add 3 synthetic records.
    additions = [
        {
            "student_id": "STU121",
            "attendance_rate": "94.00",
            "assessment_average": "88.00",
            "assignment_completion_rate": "100.00",
            "previous_average": "83.00",
            "missing_assignments": "0",
            "risk_label": "Low"
        },
        {
            "student_id": "STU122",
            "attendance_rate": "80.00",
            "assessment_average": "69.00",
            "assignment_completion_rate": "85.00",
            "previous_average": "70.00",
            "missing_assignments": "1",
            "risk_label": "Medium"
        },
        {
            "student_id": "STU123",
            "attendance_rate": "62.00",
            "assessment_average": "47.00",
            "assignment_completion_rate": "55.00",
            "previous_average": "63.00",
            "missing_assignments": "4",
            "risk_label": "High"
        }
    ]

    old_ids = {row["student_id"] for row in rows}
    assert not any(r["student_id"] in old_ids for r in additions)

    NEW_RAW.parent.mkdir(parents=True, exist_ok=True)

    with NEW_RAW.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=columns, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows + additions)

    changed_bytes = run_pipeline(NEW_RAW)
    NEW_OUTPUT.write_bytes(changed_bytes)

    baseline_manifest, baseline_lineage = create_release(
        "1.0.0", BASE_RAW, BASE_OUTPUT,
        "Initial synthetic baseline release."
    )

    changed_manifest, changed_lineage = create_release(
        "1.1.0", NEW_RAW, NEW_OUTPUT,
        "Added three validated synthetic student records."
    )

    write_json(
        "metadata/releases/manifest-1.0.0.json",
        baseline_manifest
    )
    write_json(
        "metadata/releases/lineage-1.0.0.json",
        baseline_lineage
    )

    # Current release
    write_json(
        "metadata/dataset_manifest.json",
        changed_manifest
    )
    write_json(
        "metadata/lineage.json",
        changed_lineage
    )

    assert sha256(BASE_RAW) == original_hash
    assert len(read_csv(NEW_RAW)[1]) == 123

    print("\nPASS: Raw baseline preserved.")
    print("Baseline rows:", len(rows))
    print("Changed release rows:", len(read_csv(NEW_RAW)[1]))
    print("Schema version:", contract["schema_version"])
    print("Baseline SHA256:", sha256(BASE_OUTPUT))
    print("Changed SHA256:", sha256(NEW_OUTPUT))
    print("PASS: Release metadata generated.")


if __name__ == "__main__":
    main()
