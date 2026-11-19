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

**Medium Risk** is given if none of the High Risk conditions are present and one or more of the following are present:

- Attendance rate below 85%.
- Assessment average below 65%.
- Assignment completion rate below 80%.
- At least one missing assignment.
- Assessment average is at least 10 percentage points below the previous average.

**Low Risk** is assigned when there are neither High Risk nor Medium Risk conditions.

High Risk is more important than Medium Risk.

These thresholds are not academic policies, but assumptions that can be used to test reproducible synthetic data for these projects.

## 5. Data Quality Constraints

All Seven fields are required. All nulls, duplicate student identifier, unexpected columns, malformed values and values outside the specified range are disallowed.

The 'risk_label' recorded should correspond to the documentation of the classification rule for the student's academic indicators.

Processing the raw source shall not alter its content. Processed data with invalid datasets should not be released as validated data.

## 6. Sensitive Data Classification

All the fields indicated in the submitted data set represent synthetic (simulated) data and are considered non-personal.

In the real institutional environment, however, student identifiers, attendance records and academic performance information would be sensitive.

When applied to real data, there would be access restrictions, retention policies and institutional approval, and the prototype would require appropriate consent or other lawful authorization.

## 7. Data Ownership and Governance

The project researcher will be responsible for synthetic data and technical documentation.

In an actual deployment, an academic institution should have a data owner and data steward to whom it can report.

The changes in the schema, field constraints, label definitions and rules for generating data should be reviewed and recorded before the approval of a new dataset release.

## 8. Version Control

The baseline schema version is `1.0.0`.

Major schema version increment – changes that will cause problems if you don't upgrade. Breaking changes like the removal of a required field or the change in meaning of a field.

Document, test, and approve - for release: changes compatible.

Version of the dataset will be recorded separately to schema versions in the dataset manifest for dataset release versions.

## 9. Limitations

The data is hypothetical and not reflective of actual institutional results.

Data passing the documented data quality tests does not indicate the fairness, academic appropriateness or predictive value of the risk classification rules.

Data should not be used for actual academic judgements without further checks and institutional control.

The dataset must not be used for real academic decisions without further validation and institutional governance.
