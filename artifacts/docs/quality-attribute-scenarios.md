5.	QUALITY ATTRIBUTES SCENARIOS
The quality attributes that are present in the project are Model Performance, Privacy, Explainability, Usability and Performance.


5.1	Model Performance

5.1.1	Scenario
When the model receive a valid input of the student record, it should analyse the student performance and classify them with acceptable predictive performance.

5.1.2	Measure
5.1.2.1	Precision

Predict the actual number of student that are significantly high risk from the same category. For example there are 20 student in the high risk category but after the prediction the actually high risk student from it are just 15.

5.1.2.2	Recall

Measure the number of student that are correctly categorise by the system. For example, tehr are 20 student identified by the lecturer tobe high risk but the system only detect 10 of them.

5.1.2.3	Confusion matrix

It’s a table that compares the model’s predicted categories against the actual categories. Example as below:

	Predicted	Low	Medium	High
Actual				
Low	40	5	2
Medium	6	25	4
High	3	7	15

As example, at the final row, 3 student that are high risk were classified as low risk and 7 students were classified as medium risk. Only 15 were correctly classified.

5.1.3	Verification
Test model by using a test set that the model has not seen before and compare the model’s results with the result from the non-AI baseline.

5.1.4	Acceptance Criteria

Define the level of performance that is acceptable and explain why that level is chosen before you run the evaluation.
5.2	Privacy

5.2.1	Scenario

When an unauthorised user tries to access the students academic information, the system should deny access.

5.2.2	Acceptance Criteria

Student academic information should only be access by authorised user such as lecturers and academic advisors.

5.2.3	Verification

Test authorised and unauthorised user access attempt
 Explainability

5.2.4	Scenario

When the system classified a student as high risk, the lecturer should be able to see the main academic evidence based on the recommendation.

5.2.5	Acceptance Criteria

The system should provide appropriate evidence rather than only displaying the risk categories.

5.2.6	Verification

Conduct a test review with the intended users to check whether the displayed explanation is understandable.


5.3	Usability

5.3.1	Scenario

When the authorised academic staff access the system and see the dashboard, they should be able to understand the most important risk information without prior knowledge of machine learning. 

5.3.2	Acceptance Criteria

The system should use simple but understandable terminology, show the risk categories clearly, avoid unnecessary information and provide access to the evidence for the recommendation. 

5.3.3	Verification

Ask representative users to complete a student-review task and keep track of whether they finish it correctly and record the result of the task.

 5.4	Performance

5.4.1	Scenario

When the lecturers or academic advisor request a prediction for a student, the system should return the result within an acceptable response time.

5.4.2	Acceptance Criteria

The acceptable response time are within 3 second under normal system load.

5.4.3	Verification

Test the speed of the system respond time when a request is send one after the other under the testing load planned.


11.5	Testing and Validation

Testing and validation are required to determine whether a system works correctly and produces reliable predictions that can be use. Software testing checks the behaviour of the individual functions and interaction between the system. Model evaluation assess the quality of the machine learning prediction. The following testing and validation is proposed for this project :

1.	Unit testing

Verify individual functions such as data processing and risk classification.

2.	Data validation

Check for missing values, invalid marks, invalid data types and inconsistent records before predictions.

3.	Integration testing

Verify that data processing, component, prediction model and lecturer dashboard work together correctly.

4.	Regression testing

Check that new code changes do not break previously working features.

5.	Privacy and security testing

Verify that access to student information is appropriately restricted and that sensitive data is not exposed in the repository.


To identify the students who are academically at risk, high risk recall is an important as to ensure that students who need support are identifies while precision help prevent students form being incorrectly flagged. The result of the testing should be kept as proof and this include things such as model evaluation report, test results and pictures of automated workflow that are working correctly.
