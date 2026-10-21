
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    'artifacts/docs/problem.md',
    'artifacts/docs/stakeholder.md',
    'artifacts/docs/requirement.md',
    'artifacts/docs/architecture.md',
    'artifacts/docs/decisions.md',
    'artifacts/risks/risk-register.md',
    'artifacts/traceability.md',
    'README.md',
]

PLACEHOLDERS = [
    'Replace this row',
    'Insert your diagram here.',
]

problems = []

# Check required files, minimum length and placeholders
for rel in REQUIRED:
    p = ROOT / rel

    if not p.exists():
        problems.append(f'MISSING: {rel}')
        continue

    if p.stat().st_size < 80:
        problems.append(f'TOO SHORT: {rel}')

    text = p.read_text(encoding='utf-8', errors='ignore')

    for marker in PLACEHOLDERS:
        if marker in text:
            problems.append(
                f'PLACEHOLDER: {rel} contains "{marker}"'
            )

# Check whether risk register and traceability matrix
# contain a reasonable number of non-empty records.
# These files are Markdown in this repository, not CSV.

MARKDOWN_TABLES = [
    ('artifacts/risks/risk-register.md', 4),
    ('artifacts/traceability.md', 4),
]

for rel, minimum in MARKDOWN_TABLES:
    p = ROOT / rel

    if not p.exists():
        continue

    lines = p.read_text(
        encoding='utf-8',
        errors='ignore'
    ).splitlines()

    table_rows = []

    for line in lines:
        stripped = line.strip()

        if (
            stripped.startswith('|')
            and stripped.endswith('|')
        ):
            cells = [
                cell.strip()
                for cell in stripped.strip('|').split('|')
            ]

            # Ignore Markdown table separator rows
            if cells and all(
                set(cell.replace(':', '').replace('-', '').strip()) == set()
                for cell in cells
            ):
                continue

            table_rows.append(cells)

    # First remaining row is assumed to be the header
    records = table_rows[1:] if table_rows else []

    if len(records) < minimum:
        problems.append(
            f'ROWS: {rel} requires at least {minimum} '
            f'table records; found {len(records)}'
        )

    for i, row in enumerate(records, start=2):
        if any(
            not cell or cell == 'Complete'
            for cell in row
        ):
            problems.append(
                f'INCOMPLETE: {rel} table row {i}'
            )

if problems:
    print('NEEDS WORK')

    for problem in problems:
        print('-', problem)

    sys.exit(1)

print(
    'PASS: all required artifacts meet '
    'the minimum completeness checks'
)
