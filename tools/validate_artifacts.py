from pathlib import Path
import platform
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "artifacts/docs/problem.md",
    "artifacts/docs/stakeholder.md",
    "artifacts/docs/requirements.md",
    "artifacts/docs/architecture.md",
    "artifacts/docs/decision.md",
]


REQUIRED_SECTIONS = {
    "artifacts/docs/problem.md": [
        "real world problem",
        "current process",
        "potential harm",
        "non-ai alternative",
    ],
    "artifacts/docs/stakeholder.md": [
        "stakeholder needs",
        "decision authority",
        "human oversight",
        "accountability",
    ],
    "artifacts/docs/requirements.md": [
        "user story",
        "acceptance criteria",
        "quality attributes",
        "verification",
    ],
    "artifacts/docs/architecture.md": [
        "architecture overview",
        "system components",
        "data flow",
        "human in the loop",
    ],
    "artifacts/docs/decision.md": [
        "proposed solution",
        "ai suitability",
        "final recommendation",
    ],
}


def main():
    errors = []

    print("Student Academic Risk System")
    print("Artifact Validation")
    print("------------------------------")
    print("Python version:", platform.python_version())
    print("Repository root:", ROOT)
    print()


    if sys.version_info.major != 3:
        errors.append("Python 3 is required.")
    else:
        print("[PASS] Python 3 environment detected.")


    print("\nChecking required files...")

    for relative_path in REQUIRED_FILES:
        file_path = ROOT / relative_path

        if not file_path.is_file():
            errors.append("Missing required file: " + relative_path)
            print("[FAIL] Missing:", relative_path)
        elif file_path.stat().st_size == 0:
            errors.append("Empty file: " + relative_path)
            print("[FAIL] Empty:", relative_path)
        else:
            print("[PASS] Found:", relative_path)

 
    print("\nChecking required document sections...")

    for relative_path, required_terms in REQUIRED_SECTIONS.items():
        file_path = ROOT / relative_path

        if not file_path.is_file():
            continue

        content = file_path.read_text(
            encoding="utf-8"
        ).lower()

        for term in required_terms:
            if term not in content:
                errors.append(
                    "Missing section or keyword '" + term
                    + "' in " + relative_path
                )
                print("[FAIL] Missing keyword:", term,
                      "in", relative_path)
            else:
                print("[PASS]", term, "-", relative_path)

 
    print("\nChecking risk and traceability artifacts...")

    for folder_name in ["risks", "traceability"]:
        folder_path = ROOT / folder_name

        if not folder_path.is_dir():
            errors.append("Missing folder: " + folder_name)
            print("[FAIL] Missing folder:", folder_name)
            continue

        markdown_files = list(folder_path.rglob("*.md"))

        if not markdown_files:
            errors.append(
                "No Markdown files found in " + folder_name
            )
            print("[FAIL] No Markdown files in:", folder_name)
            continue

        print("[PASS] Markdown files found in:", folder_name)

        for file_path in markdown_files:
            if file_path.stat().st_size == 0:
                relative_path = file_path.relative_to(ROOT)
                errors.append("Empty file: " + str(relative_path))
                print("[FAIL] Empty:", relative_path)

    print("\n------------------------------")

    if errors:
        print("VALIDATION FAILED")
        print("Problems found:", len(errors))

        for error in errors:
            print("-", error)

        return 1

    print("VALIDATION PASSED")
    print("All required artifact checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
