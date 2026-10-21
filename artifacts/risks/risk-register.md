7.	INITIAL RISK REGISTER
7.1	Risk Identification

Potential risk include:

•	Incorrect academic data
•	Missing academic data
•	Model misclassification
•	Data Leak
•	Model Drift
•	Unauthorised Access
•	Overreliance on AI
•	Untraceable model changes


7.2	Risk Analysis

### 1.1 Risk Analysis

| ID | Risk | Affected Stakeholder | Consequences | Likelihood | Impact | Overall | Evidence |
|---|---|---|---|---|---|---|---|
| R1 | Incorrect academic data | Lecturer, Student | Incorrect predictions may occur due to inaccurate academic data. | Medium | High | High | Data validation test results |
| R2 | False Negative | Student, Academic Advisor | A high-risk student may not receive early academic support. | Medium | High | High | High-risk recall report |
| R3 | False Positive | Lecturer, Student | A student may be incorrectly categorised as high risk. | Medium | Medium | Medium | Precision report |
| R4 | Unauthorised Access | Student | Confidential academic data may be exposed to unauthorised users. | Medium | High | High | Access control test results |
| R5 | Model Drift | Lecturer, Academic Advisors | Prediction performance may decrease over time. | Medium | Medium | Medium | Periodic evaluation report |
| R6 | Overreliance | Lecturer, Academic Advisors | Users may accept AI predictions without reviewing the supporting evidence. | Medium | High | High | Human review records |
| R7 | Untraceable Model Changes | AI Developer, Academic Advisors | Incorrect predictions may be difficult to trace to a specific model version. | Medium | Medium | Medium | Version history and model metadata |


7.3	Risk Mitigation

### 1.2 Risk Mitigation

| Risk | Mitigation | Owner |
|---|---|---|
| Incorrect academic data | Apply input validation and check data quality before prediction. | System Administrator |
| False Negative | Monitor high-risk recall and review false-negative cases. | AI Developer |
| False Positive | Require human review of potentially incorrect high-risk predictions. | Academic Advisor |
| Data Leak | Implement user authentication and role-based access control. | System Administrator |
| Model Drift | Monitor model performance periodically and evaluate whether retraining is required. | AI Developer |
| Overreliance | Require human review before any follow-up decision is made. | Academic Advisor |
| Untraceable Model Changes | Use version control and maintain model metadata and change history. | AI Developer |


