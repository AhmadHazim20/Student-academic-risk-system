# MCI1014 Assignment 2 — DataOps Engineering

## 1. Project Overview

**Project Title:** AI-Assisted Student Academic Performance Risk Identification System

**Course:** MCI1014 — Artificial Intelligence in Software Engineering

**Assignment:** Assignment 2 — DataOps Engineering

This project extends Assignment 1 by implementing a controlled and reproducible data foundation for an AI-assisted student academic risk identification system.

The DataOps package demonstrates synthetic dataset generation, ingestion, validation, preprocessing, automated quality tests, dataset versioning, lineage and governance.

The project does not implement an operational academic decision system.

## 2. Dataset Description

The project uses synthetic academic records without real student personal information.

The raw dataset contains seven fields: student_id, attendance_rate, assessment_average, assignment_completion_rate, previous_average, missing_assignments and risk_label.

The processed dataset contains one additional derived field, performance_change.

Risk categories are Low, Medium and High, assigned using predefined prototype rules.

## 3. Dataset Releases

| Release | Records | Low | Medium | High | Schema |
|---|---:|---:|---:|---:|---|
| 1.0.0 | 120 | 40 | 40 | 40 | 1.0.0 |
| 1.1.0 | 123 | 41 | 41 | 41 | 1.0.0 |

Release 1.1.0 adds three synthetic records while preserving the original 120 records.

Both dataset releases use the same schema.

## 4. Repository Structure

The Assignment 2 package is located in the `assignment-2-dataops/` directory within the Assignment 1 repository.

- `data/raw/` — Original and updated synthetic input datasets.
- `data/processed/` — Validated and transformed datasets.
- `metadata/data_contract.json` — Dataset schema and validation rules.
- `metadata/dataset_manifest.json` — Current dataset release identity.
- `metadata/lineage.json` — Current dataset transformation lineage.
- `metadata/releases/` — Baseline release metadata.
- `docs/data_scope.md` — Data scope and requirements.
- `docs/data_dictionary.md` — Field definitions and semantics.
- `docs/data_card.md` — Dataset governance, ethics and limitations.
- `docs/change_record.md` — Dataset change review and impact analysis.
- `docs/traceability.csv` — Assignment 1 to Assignment 2 traceability.
- `src/ingest.py` — Data ingestion and validation.
- `src/preprocess.py` — Deterministic data transformation.
- `src/build_releases.py` — Dataset release generation.
- `tests/test_data_quality.py` — Automated data quality tests.
- `requirements.txt` — Environment dependency information.

The GitHub Actions workflow is located at the repository root in `.github/workflows/data-quality.yml`.

## 5. Environment

The GitHub Actions workflow uses Python 3.12.

The DataOps pipeline uses Python standard-library modules and does not require third-party Python packages for ingestion, preprocessing, release generation or quality testing.

Google Colab was used as a development and testing environment.

## 6. Clean-Run Instructions

Clone the repository:

`git clone https://github.com/AhmadHazim20/Student-academic-risk-system.git`

Enter the DataOps directory:

`cd Student-academic-risk-system/assignment-2-dataops`

Install the declared dependencies:

`python -m pip install -r requirements.txt`

Run data ingestion:

`python src/ingest.py`

Run preprocessing:

`python src/preprocess.py`

Run automated tests:

`python -m unittest discover -s tests -p "test_data_quality.py" -v`

Build and validate both dataset releases:

`python src/build_releases.py`

The expected results are successful ingestion, preprocessing, nine passing data quality tests and verified release outputs.

## 7. Automated Quality Tests

Nine tests are implemented:

1. Schema validation
2. Completeness validation
3. Uniqueness validation
4. Value and range validation
5. Class distribution validation
6. Academic risk-label consistency
7. Privacy-related schema validation
8. Processed dataset consistency
9. Controlled failure validation

The controlled failure deliberately introduces an invalid attendance rate of 120. The ingestion script must reject the invalid input.

## 8. Reproducibility and Lineage

The dataset manifest records release IDs, versions, source identifiers, SHA-256 checksums, row counts, transformation parameters, timestamps and code identifiers.

Lineage metadata identifies the raw source, validation stage, preprocessing stage and final processed output.

The deterministic ingestion and preprocessing scripts must produce identical processed CSV content when executed against the same valid input and configuration.

## 9. GitHub Actions

Workflow: **Assignment 2 - Data Quality Gate**

The workflow verifies committed release identities, runs ingestion and preprocessing, executes automated quality tests, validates both releases and verifies dataset reproducibility.

The workflow is configured to run on changes to the main branch, pull requests and manual execution.

Successful GitHub Actions runs provide automated CI evidence.

## 10. Data Governance and Ethics

Only synthetic academic records are included.

The dataset must not be used for real student grading, discipline or other consequential decisions.

Dataset changes require documentation and review. The current project includes a schema-compatible addition of three synthetic records and an example of an ethically unacceptable proposal involving real student email addresses.

The synthetic risk labels are not validated real-world academic outcomes.

## 11. Project Limitations

The dataset is artificially generated and deliberately balanced.

The DataOps tests demonstrate data quality checks and pipeline reproducibility; they do not establish real-world machine-learning accuracy, fairness or institutional readiness.

The original data-generation notebook or script should be retained alongside this repository if full regeneration of the initial synthetic source from its random seed is required.

## 12. Relationship to Assignment 1

This project extends the requirements, acceptance criteria, risks and architecture identified in Assignment 1.

The DataOps package supports the system's data preparation and governance needs but does not replace the proposed human review and decision-making controls.

Detailed mappings are provided in `docs/traceability.csv`.

## 13. Generative AI Declaration

Generative AI assistance was used during development to help explain DataOps concepts, draft documentation, suggest Python implementations and troubleshoot errors.

Adopted outputs were reviewed, modified where necessary and checked using Google Colab, automated tests and GitHub Actions.

The submitted report contains a more detailed record of prompts, adopted outputs and justifications.
