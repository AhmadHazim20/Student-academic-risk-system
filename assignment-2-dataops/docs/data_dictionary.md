# Data Dictionary

## 1. Overview

This data dictionary describes the fields used in the Synthetic Student Academic Risk Dataset for the AI-Assisted Student Academic Performance Risk Identification System.

The purpose of the dataset is to support controlled data ingestion, preprocessing, automated quality validation and risk classification testing.

| **Item**            | **Description** |
| ------------------- | --------------- |
| **Schema Version**  | 1.0.0           |
| **Dataset Type**    | Synthetic       |
| **Primary Key**     | `student_id`    |
| **Target Variable** | `risk_label`    |

## 2. Field Definitions

| Field Name | Data Type | Required | Allowed Values | Description |
|---|---|---|---|---|
| student_id | String | Yes | STU followed by at least 3 digits | Unique synthetic student identifier |
| attendance_rate | Float | Yes | 0–100 | Percentage of classes attended |
| assessment_average | Float | Yes | 0–100 | Average score from current academic assessments |
| assignment_completion_rate | Float | Yes | 0–100 | Percentage of assignments completed |
| previous_average | Float | Yes | 0–100 | Average academic performance from the previous reporting period |
| missing_assignments | Integer | Yes | 0–20 | Number of missing assignments |
| risk_label | String | Yes | Low, Medium, High | Synthetic academic risk classification |

## 3. Data Semantics

### 3.1 Student Identifier

`student_id` represents a unique simulated student. It is not linked to any real student's identity. Duplicate identifiers are not allowed.

### 3.2 Attendance Rate

`attendance_rate` represents the percentage of attended classes during the reporting period.

### 3.3 Assessment Average

`assessment_average` represents the student's average assessment score on a scale from 0 to 100.

### 3.4 Assignment Completion Rate

`assignment_completion_rate` measures the percentage of required assignments completed.

### 3.5 Previous Average

`previous_average` represents the academic average for the preceding reporting period. It is used to identify performance declines.

### 3.6 Missing Assignments

`missing_assignments` represents the number of outstanding assignments during the reporting period.

### 3.7 Risk Label

`risk_label` is a synthetic reference label calculated from predetermined academic risk rules.

The label supports pipeline testing and is not an independently validated indicator of actual student performance risk.

## 4. Risk Classification Rules

**High Risk** is assigned when any of the following conditions is met:

- Attendance rate below 70%.
- Assessment average below 50%.
- Three or more missing assignments.

**Medium Risk** is assigned when no High Risk condition is met and at least one of the following applies:

- Attendance rate below 85%.
- Assessment average below 65%.
- Assignment completion rate below 80%.
- At least one missing assignment.
- Assessment average is at least 10 percentage points below the previous average.

**Low Risk** is assigned when neither High Risk nor Medium Risk conditions are met.

High Risk takes priority over Medium Risk.

These thresholds are project-specific assumptions for reproducible synthetic data testing, not institutional academic policies.

## 5. Data Quality Constraints

All seven fields are mandatory. Null values, duplicate student identifiers, unexpected columns, malformed values and values outside the specified ranges are prohibited.

The recorded `risk_label` must match the documented classification rule for the student's academic indicators.

The raw source must remain unchanged during processing. Invalid datasets must not be released as validated processed data.

## 6. Sensitive Data Classification

All fields in the submitted dataset describe simulated records and are therefore classified as non-personal synthetic data.

However, student identifiers, attendance records and academic performance information would be sensitive in a real institutional environment.

If the prototype were adapted to real data, appropriate consent or other lawful authority, access restrictions, retention policies and institutional approval would be required.

## 7. Data Ownership and Governance

The project researcher is responsible for the synthetic dataset and its technical documentation.

For a real deployment, the academic institution would need to designate an accountable data owner and data steward.

Any modification to the schema, field constraints, label definitions or data generation rules must be reviewed and documented before a new dataset release is approved.

## 8. Version Control

The baseline schema version is `1.0.0`.

Breaking changes, such as removing a required field or changing its meaning, require a major schema version increment.

Compatible changes must still be documented, tested and approved before release.

Dataset release versions will be recorded separately from schema versions in the dataset manifest.

## 9. Limitations

The dataset is synthetic and does not represent actual institutional outcomes.

Passing the documented data quality tests does not demonstrate that the risk classification rules are fair, academically appropriate or predictive of real student outcomes.

The dataset must not be used for real academic decisions without further validation and institutional governance.
