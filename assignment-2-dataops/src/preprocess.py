
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

STAGING = ROOT / "data/staging/validated_input.csv"
OUTPUT = ROOT / "data/processed/controlled_dataset.csv"

def preprocess():
    OUTPUT.unlink(missing_ok=True)

    with STAGING.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        records = list(reader)
        original_fields = reader.fieldnames

    # Deterministic ordering
    records.sort(key=lambda row: row["student_id"])

    for row in records:
        current = float(row["assessment_average"])
        previous = float(row["previous_average"])

        # Derived academic performance indicator
        change = current - previous
        row["performance_change"] = f"{change:.2f}"

    columns = original_fields + ["performance_change"]

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)

    print("PASS: Data preprocessing completed.")
    print("Processed records:", len(records))
    print("Output:", OUTPUT)

if __name__ == "__main__":
    preprocess()
