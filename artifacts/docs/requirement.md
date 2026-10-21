# 4. USER STORIES AND ACCEPTANCE CRITEREA

## 4.1 User Identification

The main users of the system are lecturers and academic advisors. The student is the affected party to the system rather than an operational user.

## 4.2 User Story 1

As a lecturer, I want to view all the potentially at risk recommended students suggest by the system so that I can decide which student to be prioritised.

### 4.2.1 Acceptance Criteria

| ID | Acceptance Criteria |
|---|---|
| AC-01 | The system displays the list of risk recommended students with risk classification |
| AC-02 | The lecturer can view the academic indicators used for the recommendation |
| AC-03 | By using valid risk classification, the lecturer can view the risk recommended student by the risk category. |
| AC-04 | The system did not automatically made academic intervention instead if missing or invalid data found the system will reject input or send it to the user for review. |
| AC-05 | Only allow Authorize users can access student information, any unauthorised user will be denied access. |

## 4.3 User Story 2

As a lecturer, I want to view students which are categorised as high risk so that I can make a decision.

### 4.3.1 Acceptance Criteria

| ID | Acceptance Criteria |
|---|---|
| AC-06 | If a student identified as high risk, the system will display the indicators associated with the prediction. |
| AC-07 | When the lecturer review the AI recommendation, the lecturer can access the relevant academic information supporting the recommendation. |
| AC-08 | The lecturer can decide to disagree with the AI recommendation and choose to override the recommendation |
| AC-09 | Upon override, the system will recorded the decision made by lecturer, original recommendation, timestamp and the user identity. |

## 4.4 User Story 3

As and authorised academic staff, I wanted to record the final decision made for this student after viewing the recommendations and evidences provided by the AI-assisted system so that the system maintain accountability and for the decision history.

### 4.4.1 Acceptance Criteria

| ID | Acceptance Criteria |
|---|---|
| AC-10 | The user input the final decision and the system will record it |
| AC-11 | Upon retrieving the decision recorded, the original AI recommendation and any override will still be retrieved |
| AC-12 | The system will denied access to unauthorised user to change or modify the record |
| AC-13 | When authorised user review the audit history, the suer will be shown the decision timestamp and responsible user. |

## 4.5 User Story to Value Mapping

| User Story | Expected Value | Stakeholder Benefiting |
|---|---|---|
| User story 1: View the list of students potentially at risk and their risk classification | Help lecturer identify student who need support and reduce effort required to review student records individually. | Lecturer and academic advisors |
| User story 2: View high risk student, their contributing indicators and review or override recommendation | Support prioritization, provides evidence for predictions and all9ow lecturer to use their judgement. | Lecturer, academic advisor and student |
| User story 3: Record the final decision and retain decision history | Improve accountability, traceability and ability to review previous decisions | Authorised academic staff and relevant administrator |

## 4.6 Acceptance Test Summary

| Test | Expected Result | Related AC |
|---|---|---|
| Login as authorised user | System is accessible | AC-05 |
| Login as unauthorised user | Access is denied | AC-05 |
| View Student list | Risk recommendation displayed | AC-01 |
| Filter student by category | Relevant selected category displayed | AC-03 |
| Open a student recommendation | Relevant academic indicators and supporting evidence are displayed | AC-02, AC-06, AC-07 |
| Override Recommendation | Lecturer can change the AI recommendation and the original recommendation remain available | AC-08, AC-09 |
| Invalid academic data input | Input rejected with appropriate error displayed | AC-04 |
| Record final decision | System save the decison | AC-10 |
| Retrieve recorded decision | The original AI recommendation, final decision and override are available | AC-11 |
| Unauthorised modification of a decision | System denies the modification | AC-12 |
| Review audit history | System display the decision timestamp and responsible user identity | AC-13 |

# 5. QUALITY ATTRIBUTES SCENARIOS

The quality attributes that are present in the project are Model Performance, Privacy, Explainability, Usability and Performance.

## 5.1 Model Performance

### 5.1.1 Scenario

When the model receive a valid input of the student record, it should analyse the student performance and classify them with acceptable predictive performance.

### 5.1.2 Measure

#### 5.1.2.1 Precision

Predict the actual number of student that are significantly high risk from the same category. For example there are 20 student in the high risk category but after the prediction the actually high risk student from it are just 15.

#### 5.1.2.2 Recall

Measure the number of student that are correctly categorise by the system. For example, tehr are 20 student identified by the lecturer tobe high risk but the system only detect 10 of them.

#### 5.1.2.3 Confusion matrix

It’s a table that compares the model’s predicted categories against the actual categories. Example as below:

| Actual | Predicted Low | Predicted Medium | Predicted High |
|---|---:|---:|---:|
| Low | 40 | 5 | 2 |
| Medium | 6 | 25 | 4 |
| High | 3 | 7 | 15 |

As example, at the final row, 3 student that are high risk were classified as low risk and 7 students were classified as medium risk. Only 15 were correctly classified.

### 5.1.3 Verification

Test model by using a test set that the model has not seen before and compare the model’s results with the result from the non-AI baseline.

### 5.1.4 Acceptance Criteria

Define the level of performance that is acceptable and explain why that level is chosen before you run the evaluation.

## 5.2 Privacy

### 5.2.1 Scenario

When an unauthorised user tries to access the students academic information, the system should deny access.

### 5.2.2 Acceptance Criteria

Student academic information should only be access by authorised user such as lecturers and academic advisors.

### 5.2.3 Verification

Test authorised and unauthorised user access attempt.

## 5.3 Explainability

### 5.3.1 Scenario

When the system classified a student as high risk, the lecturer should be able to see the main academic evidence based on the recommendation.

### 5.3.2 Acceptance Criteria

The system should provide appropriate evidence rather than only displaying the risk categories.

### 5.3.3 Verification

Conduct a test review with the intended users to check whether the displayed explanation is understandable.

## 5.4 Usability

### 5.4.1 Scenario

When the authorised academic staff access the system and see the dashboard, they should be able to understand the most important risk information without prior knowledge of machine learning.

### 5.4.2 Acceptance Criteria

The system should use simple but understandable terminology, show the risk categories clearly, avoid unnecessary information and provide access to the evidence for the recommendation.

### 5.4.3 Verification

Ask representative users to complete a student-review task and keep track of whether they finish it correctly and record the result of the task.

## 5.5 Performance

### 5.5.1 Scenario

When the lecturers or academic advisor request a prediction for a student, the system should return the result within an acceptable response time.

### 5.5.2 Acceptance Criteria

The acceptable response time are within 3 second under normal system load.

### 5.5.3 Verification

Test the speed of the system respond time when a request is send one after the other under the testing load planned.
