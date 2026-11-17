# Data Card — Synthetic Student Academic Risk Dataset

## 1. Dataset Overview

**Project:** AI-Assisted Student Academic Performance Risk Identification System

**Dataset Type:** Synthetic academic records

**Schema Version:** 1.0.0

**Baseline Release:** 1.0.0 — 120 records

**Updated Release:** 1.1.0 — 123 records

**Data Owner:** Student researcher for this academic prototype

**Purpose:** To support controlled ingestion, preprocessing, data quality testing, versioning and governance for an AI-assisted academic risk identification system.

## 2. Data Source and Collection

The dataset consists of artificially generated student academic records.

No real student records were intentionally used. The baseline was generated with a fixed random seed of 42, and the updated release adds three explicitly defined synthetic records.

The released CSV files are preserved in the GitHub repository for reproducibility.

## 3. Data Attributes

The raw dataset contains seven fields:

- student_id
- attendance_rate
- assessment_average
- assignment_completion_rate
- previous_average
- missing_assignments
- risk_label

The processed dataset includes one additional derived field, performance_change.

## 4. Dataset Distribution

| Release | Low | Medium | High | Total |
|---|---:|---:|---:|---:|
| 1.0.0 | 40 | 40 | 40 | 120 |
| 1.1.0 | 41 | 41 | 41 | 123 |

The dataset has been deliberately balanced to facilitate testing. This distribution is not representative of real institutional student populations.

## 5. Intended and Prohibited Uses

The dataset is intended for academic DataOps experimentation, automated validation, pipeline reproducibility and synthetic risk classification testing.

The dataset must not be used for real student grading, disciplinary decisions, admission decisions or automatic academic intervention.

The assigned risk labels are rule-generated reference categories, not independently verified academic outcomes.

## 6. Privacy and Consent

The dataset contains synthetic student identifiers and simulated academic indicators.

Consent from real students was not required for generating these fictional records because no real student data was intentionally collected.

For a future real-world deployment, the institution must establish an appropriate lawful basis or consent where required, implement access controls, and obtain institutional approval before processing personal academic records.

The repository must not contain real student names, identity numbers, addresses, phone numbers or other identifying information.

## 7. Data Licence and Ownership

The submitted synthetic data was generated for this academic project rather than obtained from a third-party dataset provider.

No third-party dataset licence is claimed. Any public reuse should follow the repository's explicitly stated permissions, if any.

The student researcher is accountable for the prototype dataset. A real institutional deployment would require a formally designated institutional data owner.

## 8. Data Minimisation and Access

Only academic indicators needed for the proposed risk classification and its supporting explanation are included.

Direct personal identifiers are excluded from the submitted schema.

Public access is limited to synthetic data. Real academic information would require authenticated, role-based access restricted to authorised staff.

The current DataOps package does not implement a complete institutional authentication or authorisation system.

## 9. Representation and Bias Risks

The baseline dataset contains equally represented Low, Medium and High risk categories.

This intentionally balanced distribution may misrepresent the frequency of academic risks in real student populations.

The classification rules also rely on manually selected thresholds that have not been validated as institutional policy.

No real demographic fairness evaluation has been conducted.

## 10. Data Quality Controls

The project uses nine automated tests to verify:

1. Schema consistency
2. Completeness
3. Identifier uniqueness
4. Data validity
5. Class distribution
6. Risk label consistency
7. Privacy-related schema rules
8. Processed data consistency
9. Controlled rejection of invalid attendance

The controlled failure test uses an attendance rate of 120, which exceeds the permitted range.

The privacy-related schema test checks for prohibited column names, but it does not establish that every data value is free of personal information. Additional review would be required before using externally sourced data.

## 11. Retention and Security

The synthetic dataset is maintained in a version-controlled repository for academic assessment and reproducibility.

The researcher should review retained working copies after assessment and remove unnecessary local duplicates.

For real student records, retention periods, storage security, access permissions and deletion procedures would require an approved institutional policy.

## 12. Governance and Approval

Dataset changes must be documented in docs/change_record.md.

The reviewer must inspect schema compatibility, data quality results, privacy risks, lineage and reproducibility before approving a release.

Breaking or ethically unacceptable changes must be rejected or quarantined pending further review.

The dataset manifest records release identifiers, checksums and transformation information.

## 13. Limitations

The synthetic dataset cannot demonstrate real student behaviour, real-world model accuracy, actual bias across demographic groups or performance in a live academic institution.

Because the reference labels are generated using predetermined rules, agreement with these labels does not establish the predictive validity of a machine learning model.

The original synthetic-data generation notebook or script and its dependency versions should also be preserved if full regeneration from the random seed is required.

The DataOps package establishes a reproducible data-processing foundation, not a validated operational academic decision system.
