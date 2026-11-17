
import csv
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/synthetic_dataset.csv"
PROCESSED = ROOT / "data/processed/controlled_dataset.csv"
CONTRACT = ROOT / "metadata/data_contract.json"
INGEST = ROOT / "src/ingest.py"


def load_csv(path):
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames, list(reader)


def expected_risk(row):
    attendance = float(row["attendance_rate"])
    assessment = float(row["assessment_average"])
    completion = float(row["assignment_completion_rate"])
    previous = float(row["previous_average"])
    missing = int(row["missing_assignments"])

    if attendance < 70 or assessment < 50 or missing >= 3:
        return "High"

    if (
        attendance < 85
        or assessment < 65
        or completion < 80
        or missing >= 1
        or previous - assessment >= 10
    ):
        return "Medium"

    return "Low"


class TestDataQuality(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads(
            CONTRACT.read_text(encoding="utf-8")
        )
        cls.columns, cls.rows = load_csv(RAW)

    def test_01_schema(self):
        expected = [
            f["name"] for f in self.contract["fields"]
        ]
        self.assertEqual(self.columns, expected)

    def test_02_completeness(self):
        self.assertGreater(len(self.rows), 0)

        for row in self.rows:
            for field in self.columns:
                self.assertIsNotNone(row[field])
                self.assertNotEqual(row[field].strip(), "")

    def test_03_uniqueness(self):
        ids = [r["student_id"] for r in self.rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_04_validity(self):
        for row in self.rows:
            for field in self.contract["fields"]:
                name = field["name"]
                value = row[name]

                if field["type"] == "float":
                    number = float(value)
                    self.assertTrue(math.isfinite(number))
                    self.assertGreaterEqual(
                        number, field["minimum"]
                    )
                    self.assertLessEqual(
                        number, field["maximum"]
                    )

                elif field["type"] == "integer":
                    self.assertRegex(
                        value, r"^(0|[1-9][0-9]*)$"
                    )
                    number = int(value)
                    self.assertGreaterEqual(
                        number, field["minimum"]
                    )
                    self.assertLessEqual(
                        number, field["maximum"]
                    )

                else:
                    if "pattern" in field:
                        self.assertIsNotNone(
                            re.fullmatch(field["pattern"], value)
                        )

                    if "allowed_values" in field:
                        self.assertIn(
                            value, field["allowed_values"]
                        )

    def test_05_class_distribution(self):
        counts = {
            label: sum(
                r["risk_label"] == label
                for r in self.rows
            )
            for label in ["Low", "Medium", "High"]
        }

        for count in counts.values():
            self.assertGreaterEqual(
                count / len(self.rows), 0.10
            )

        print("\nClass distribution:", counts)

    def test_06_domain_label_rule(self):
        for row in self.rows:
            self.assertEqual(
                row["risk_label"],
                expected_risk(row)
            )

    def test_07_privacy_rule(self):
        forbidden = {
            "name", "full_name", "email",
            "phone", "address", "ic_number",
            "national_id", "date_of_birth"
        }

        self.assertTrue(
            forbidden.isdisjoint(set(self.columns))
        )

    def test_08_processed_consistency(self):
        self.assertTrue(
            PROCESSED.is_file(),
            "Run preprocessing before testing."
        )

        columns, processed = load_csv(PROCESSED)

        self.assertEqual(
            columns,
            self.columns + ["performance_change"]
        )

        self.assertEqual(len(processed), len(self.rows))

        raw_by_id = {
            r["student_id"]: r for r in self.rows
        }

        processed_ids = [
            r["student_id"] for r in processed
        ]

        self.assertEqual(
            processed_ids, sorted(processed_ids)
        )

        self.assertEqual(
            set(processed_ids), set(raw_by_id)
        )

        for row in processed:
            raw = raw_by_id[row["student_id"]]

            for name in self.columns:
                self.assertEqual(row[name], raw[name])

            expected = (
                float(raw["assessment_average"])
                - float(raw["previous_average"])
            )

            self.assertAlmostEqual(
                float(row["performance_change"]),
                expected,
                places=2
            )

    def test_09_controlled_failure(self):
        # Test the real ingestion script using a temporary
        # invalid dataset. The original raw data is untouched.

        with tempfile.TemporaryDirectory() as temp:
            test_root = Path(temp) / "assignment-2-dataops"

            for folder in ["src", "metadata", "data/raw"]:
                (test_root / folder).mkdir(
                    parents=True, exist_ok=True
                )

            shutil.copy2(
                INGEST, test_root / "src/ingest.py"
            )
            shutil.copy2(
                CONTRACT,
                test_root / "metadata/data_contract.json"
            )

            invalid_rows = [
                dict(row) for row in self.rows
            ]

            # Deliberately introduce an invalid attendance rate
            invalid_rows[0]["attendance_rate"] = "120.00"

            invalid_file = (
                test_root / "data/raw/synthetic_dataset.csv"
            )

            with invalid_file.open(
                "w", encoding="utf-8", newline=""
            ) as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=self.columns,
                    lineterminator="\n"
                )
                writer.writeheader()
                writer.writerows(invalid_rows)

            result = subprocess.run(
                [
                    sys.executable,
                    str(test_root / "src/ingest.py")
                ],
                capture_output=True,
                text=True
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn(
                "Out-of-range attendance_rate",
                result.stderr
            )

            self.assertFalse(
                (
                    test_root /
                    "data/staging/validated_input.csv"
                ).exists()
            )

            print(
                "\nCONTROLLED FAILURE: "
                "Invalid attendance 120 rejected successfully."
            )


if __name__ == "__main__":
    unittest.main()
