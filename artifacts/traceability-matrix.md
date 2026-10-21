8.	TRACEBILITY MATRIX
8.1	Problem to requirement Traceability
### 8.1	Problem to requirement Traceability

| Problem | Requirement | Requirement ID |
|---|---|---|
| Difficulty identifying students at academic risk | The system shall classify students according to their academic risk levels. | RQ-01 |
| Time-consuming manual review | The system shall provide a prioritised list of students based on their predicted risk levels. | RQ-02 |
| Difficulty understanding AI decisions | The system shall provide supporting evidence for its predictions. | RQ-03 |
| Incorrect AI predictions | An authorised user shall review AI recommendations before making a final decision. | RQ-04 |
| Sensitive student data | The system shall restrict access to authorised users only. | RQ-05 |
| Decisions and model changes may be difficult to trace | The system shall record decisions and relevant model information for auditing. | RQ-06 |

### 8.2 Requirement to Architecture Traceability

| ID | User Story / Acceptance Criterion | Architecture Component | Verification |
|---|---|---|---|
| RQ-01 | US-01 / AC-01 | ML Model Service | Test classification using valid academic records with the expected input fields. |
| RQ-02 | US-01 / AC-03 | Web Dashboard | Verify that predicted risk categories are displayed and can be reviewed by authorised users. |
| RQ-03 | US-02 / AC-06 | Explanation Component | Check that the displayed indicators correspond to the information used to explain the prediction. |
| RQ-04 | US-03 / AC-10 | Human Review Component | Verify that an authorised staff member can review the recommendation and make the final decision. |
| RQ-05 | US-01 / AC-05 | API and Access Control | Test access using authorised and unauthorised user accounts. |
| RQ-06 | US-03 / AC-11, AC-13 | Decision and Audit Log | Verify that the system records the recommendation, final decision, timestamp, and model version where applicable. |

### 8.3 Risk to Mitigation Traceability

| ID | Mitigation | Architecture Component | Verification |
|---|---|---|---|
| R1 | Input validation | Data Validation and Preprocessing | Test missing, invalid, and incorrectly formatted academic data. |
| R2 | Monitor high-risk recall | ML Model Service and Monitoring Component | Evaluate high-risk recall using labelled test data. |
| R3 | Human review | Human Review Component | Test the review and override workflow for potentially incorrect predictions. |
| R4 | User authentication and authorisation | API and Access Control | Test access permissions for authorised and unauthorised users. |
| R5 | Performance monitoring | Monitoring Component | Compare model performance across evaluation periods. |
| R6 | Mandatory human decision | Human Review Component | Verify that predictions do not automatically trigger academic interventions or final decisions. |
| R7 | Version control and metadata | Repository, Model Versioning, and Audit Log | Check that model versions and associated artifacts can be identified from recorded metadata and version history. |
