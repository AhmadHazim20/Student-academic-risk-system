
from pathlib import Path
import csv
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]

RAW = ROOT / "data/raw/synthetic_dataset.csv"
CONTRACT = ROOT / "metadata/data_contract.json"
STAGING = ROOT / "data/staging/validated_input.csv"

def run_ingestion():
    # Remove old intermediate output before validating
    STAGING.unlink(missing_ok=True)

    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    fields = contract["fields"]
    expected = [f["name"] for f in fields]

    records = []
    student_ids = set()

    with RAW.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != expected:
            raise ValueError("Schema mismatch: unexpected or missing columns")

        for line_no, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(f"Extra CSV values at line {line_no}")

            clean = {}

            for field in fields:
                name = field["name"]
                value = row[name]

                if value is None or not value.strip():
                    raise ValueError(f"Missing {name} at line {line_no}")

                if field["type"] == "float":
                    try:
                        number = float(value)
                    except ValueError:
                        raise ValueError(f"Invalid {name} at line {line_no}")

                    if not math.isfinite(number):
                        raise ValueError(f"Non-finite {name} at line {line_no}")

                    if not field["minimum"] <= number <= field["maximum"]:
                        raise ValueError(f"Out-of-range {name} at line {line_no}")

                    clean[name] = f"{number:.2f}"

                elif field["type"] == "integer":
                    if not re.fullmatch(r"0|[1-9][0-9]*", value):
                        raise ValueError(f"Invalid integer {name} at line {line_no}")

                    number = int(value)
                    if not field["minimum"] <= number <= field["maximum"]:
                        raise ValueError(f"Out-of-range {name} at line {line_no}")

                    clean[name] = str(number)

                else:
                    if "pattern" in field and not re.fullmatch(field["pattern"], value):
                        raise ValueError(f"Invalid {name} at line {line_no}")

                    if "allowed_values" in field and value not in field["allowed_values"]:
                        raise ValueError(f"Invalid {name} at line {line_no}")

                    clean[name] = value

            student_id = clean["student_id"]

            if student_id in student_ids:
                raise ValueError(f"Duplicate student_id: {student_id}")

            student_ids.add(student_id)
            records.append(clean)

    if not records:
        raise ValueError("Dataset is empty")

    STAGING.parent.mkdir(parents=True, exist_ok=True)

    with STAGING.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=expected, lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)

    print("PASS: Data ingestion completed.")
    print("Validated records:", len(records))

if __name__ == "__main__":
    run_ingestion()
