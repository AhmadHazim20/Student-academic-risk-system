# Dataset Change Record and Impact Analysis

## 1. Change Request DCR-001

| **Item**             | **Description**                                                     |
| -------------------- | ------------------------------------------------------------------- |
| **Project**          | AI-Assisted Student Academic Performance Risk Identification System |
| **Baseline Release** | 1.0.0                                                               |
| **Updated Release**  | 1.1.0                                                               |
| **Schema Version**   | 1.0.0                                                               |
| **Change Type**      | Schema-compatible dataset update                                    |
| **Change Owner**     | Student Researcher                                                  |
| **Reviewer**         | Student Researcher acting as Prototype Data Steward                 |
| **Review Date**      | 17 November 2026                                                    |
| **Approval Status**  | Pending manual review                                               |

### 1.1 Description

Three additional synthetic student records were introduced into the baseline dataset.

The new records are STU121, STU122 and STU123, representing Low, Medium and High academic risks respectively.

The number of records increased from 120 to 123 without modifying the data schema, existing 120 records, validation constraints or classification rules.

### 1.2 Impact Analysis

| Component | Impact |
|---|---|
| Data Schema | No change |
| Data Contract | Remains 1.0.0 |
| Dataset Size | 120 to 123 |
| Class Distribution | 40 to 41 records per category |
| Ingestion | Existing script reused |
| Preprocessing | Existing script reused |
| Data Quality Tests | Nine automated tests applicable to both releases |
| Privacy | No new personal information |
| Release Version | 1.0.0 to 1.1.0 |

### 1.3 Verification Evidence

The GitHub Actions Data Quality Gate successfully executed the automated pipeline.

Review evidence must include:

- Successful ingestion and preprocessing.
- Nine passing automated data quality tests.
- Successful controlled failure test.
- Dataset release identity and checksum verification.
- Reproducibility verification.
- Confirmation that baseline data remains unchanged.

### 1.4 Review Decision

**Decision:** [Approved / Rejected / Changes Required]

**Justification:** [Enter actual reviewer findings]

**Approval Scope:** Synthetic academic prototype only.

The change may be approved after the reviewer confirms the validation results and governance requirements.

---

## 2. Change Request DCR-002 — Unacceptable Change

**Proposed Change:** Introduce a new email field containing real student email addresses in the publicly shared dataset.

**Change Type:** Breaking and ethically unacceptable

**Status:** Rejected in the proposed design review; not implemented.

### 2.1 Technical Impact

The change introduces a field that is not permitted by the current schema.

The existing contract prohibits unexpected fields. Consequently, the ingestion pipeline should reject the modified schema.

The schema test would also detect the mismatch, and the privacy-related test would identify the prohibited email field.

### 2.2 Ethical Impact

Real student email addresses introduce personal data and increase the risk of unauthorised disclosure.

Publishing this information would contradict the synthetic dataset's intended scope and data minimisation policy.

### 2.3 Required Response

The proposed change must not be merged into the public dataset.

A future request to process real student information would require an approved institutional purpose, appropriate lawful authority, access controls, retention policy and a separate governance review.

### 2.4 Impact Summary

| Aspect | DCR-001 | DCR-002 |
|---|---|---|
| Schema compatibility | Compatible | Breaking |
| Privacy risk | Low for synthetic prototype | Unacceptable for public dataset |
| Existing pipeline | Supports update | Should reject schema |
| Approval outcome | Subject to review | Rejected |
| Dataset publication | Permitted after approval | Not permitted |

## 3. Traceability

DCR-001 relates to AC-02, AC-04 and risks R1, R5 and R7 from Assignment 1.

DCR-002 relates to AC-04, AC-05 and risk R4.

Detailed traceability is maintained in docs/traceability.csv.
