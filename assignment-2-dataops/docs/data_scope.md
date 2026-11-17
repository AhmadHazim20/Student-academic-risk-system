# 1. Data Scope and Requirements

## 1.1 Project Title

AI-Assisted Student Academic Performance Risk Identification System

## 1.2 Data Purpose

The purpose of the dataset is to support the development and testing of an AI-assisted system that identifies students who may be at risk of poor academic performance.

The system uses academic indicators such as attendance, assessment results and assignment completion to support risk classification into three categories: Low Risk, Medium Risk and High Risk.

The risk classification is intended to assist lecturers and academic advisors in identifying students who may require additional academic support. The system does not automatically make academic decisions.

## 1.3 Data Source

This project will use a **synthetic student academic performance dataset** created specifically for educational testing.

The dataset will contain simulated academic records rather than real student information. This approach protects student privacy and allows controlled testing of valid and invalid data.

The raw dataset will be preserved before preprocessing to support reproducibility and data lineage.

## 1.4 Data Ownership and Consumers

| Role | Responsibility |
|---|---|
| Data Owner | Academic institution (proposed role in a real deployment) |
| Data Steward | System Administrator |
| Data Engineer | Responsible for dataset generation, validation, preprocessing and versioning |
| Lecturer | Reviews student academic indicators and risk recommendations |
| Academic Advisor | Reviews students who may require academic support |
| AI Developer | Uses validated data for model development and testing |

For this prototype, the student researcher is responsible for generating and managing the synthetic dataset.

## 1.5 Permitted Data Use

The dataset is intended for academic research, prototype development, DataOps validation and testing.

It may be used to test ingestion, preprocessing, data quality checks, risk classifications and reproducibility.

The dataset must not be used to make real academic, disciplinary or admission decisions. Real student information must not be included in the public repository.

## 1.6 Required Data Fields

| Field | Data Type | Description |
|---|---|---|
| student_id | String | Unique synthetic student identifier |
| attendance_rate | Float | Attendance percentage from 0 to 100 |
| assessment_average | Float | Average assessment score from 0 to 100 |
| assignment_completion_rate | Float | Percentage of completed assignments |
| previous_average | Float | Previous academic performance average |
| missing_assignments | Integer | Number of incomplete or missing assignments |
| risk_label | String | Reference risk category: Low, Medium or High |

These fields form the proposed baseline schema. Detailed validation rules will be specified in the data contract.

## 1.7 Target Label Definition

The target field is `risk_label`, which represents a student's simulated academic risk category.

For this prototype, risk labels will be generated using predefined rules:

| Risk Category | Proposed Rule |
|---|---|
| High | Attendance below 70%, or assessment average below 50%, or at least 3 missing assignments |
| Medium | If not High: attendance below 85%, assessment average below 65%, assignment completion below 80%, at least 1 missing assignment, or a performance decline of at least 10 percentage points |
| Low | None of the High or Medium conditions apply |

These thresholds are **prototype assumptions**, not officially validated institutional policies. High-risk conditions take priority over medium-risk conditions.

The labels are synthetic reference labels for pipeline testing. They are not independently verified measures of actual student academic risk.

## 1.8 Data Assumptions and Limitations

The baseline dataset represents a single academic reporting period, with one record per simulated student.

All percentages must be between 0 and 100. Missing or invalid required values must be detected during validation rather than silently accepted.

Synthetic records will be generated reproducibly using a fixed random seed. The dataset will include different risk categories and representative failure cases.

The dataset cannot demonstrate actual student behaviour, institutional differences, demographic fairness or real-world predictive accuracy. Further validation using appropriately authorised real data would be necessary before operational deployment.

## 1.9 Relationship to Assignment 1 Requirements

| Requirement ID | Assignment 1 Requirement | Relationship to Assignment 2 |
|---|---|---|
| RQ-01 | Classify students according to academic risk levels | The dataset provides validated academic indicators and a reference risk label |
| RQ-03 | Provide supporting evidence for predictions | Academic indicators are retained in the processed dataset |
| RQ-05 | Restrict access to authorised users | Synthetic records are used for the public repository; real academic data would require access controls |
| RQ-06 | Record decisions and relevant model information for auditing | Dataset releases, transformations and changes will be recorded through manifests and lineage metadata |

## 1.10 Relationship to Assignment 1 Risks

| Risk ID | Assignment 1 Risk | DataOps Control |
|---|---|---|
| R1 | Incorrect academic data | Schema validation, missing-value checks and range validation |
| R2 | False Negative | Document class distribution and limitations of synthetic labels |
| R4 | Unauthorised Access | Prohibit real student information from the public dataset |
| R5 | Model Drift | Record dataset versions and distribution statistics to support future monitoring |
| R7 | Untraceable Model Changes | Maintain dataset release IDs, checksums, transformation identifiers and lineage |

## 1.11 Expected DataOps Outcome

The expected outcome is a controlled and reproducible data foundation for the AI-assisted student academic risk system.

The pipeline should preserve raw data, validate academic records, transform valid inputs consistently, detect controlled failures and generate documentation for dataset identification and traceability.

Data changes will require documented review before acceptance. Invalid or ethically unacceptable changes must be rejected.
