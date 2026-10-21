4.	USER STORIES AND ACCEPTANCE CRITEREA
4.1	User Identification

The main users of the system are lecturers and academic advisors. The student is the affected party to the system rather than an operational user.

4.2	User Story 1

As a lecturer, I want to view all the potentially at risk recommended students suggest by the system so that I can decide which student to be prioritised.

4.2.1	Acceptance Criteria

ID	Acceptance Criteria
AC-01 -	The system displays the list of risk recommended students with risk classification
AC-02 -	The lecturer can view the academic indicators used for the recommendation
AC-03 -	By using valid risk classification, the lecturer can view the risk recommended student by the risk category.
AC-04 -	The system did not automatically made academic intervention instead if missing or invalid data found the system will reject input or send it to the user for review.
AC-05 -	Only allow Authorize users can access student information, any unauthorised user will be denied access.


4.3	User Story 2

As a lecturer, I want to view students which are categorised  as high risk so that I can make a decision.


4.3.1	Acceptance Criteria

ID	Acceptance Criteria
AC-06 -	If a student identified as high risk, the system will display the indicators associated with the prediction.
AC-07 -	When the lecturer review the AI recommendation, the lecturer can access the relevant academic information supporting the recommendation.
AC-08 -	The lecturer can decide to disagree with the AI recommendation and choose to override the recommendation
AC-09 -	Upon override, the system will recorded the decision made by lecturer, original recommendation, timestamp and the user identity.


4.4	User Story 3

As and authorised academic staff, I wanted to record the final decision made for this student after viewing the recommendations and evidences provided by the AI-assisted system so that the system maintain accountability and for the decision history. 

4.4.1	Acceptance Criteria

ID	Acceptance Criteria
AC-10 -	The user input the final decision and the system will record it
AC-11 -	Upon retrieving the decision recorded, the original AI recommendation and any override will still be retrieved
AC-12 -	The system will denied access to unauthorised user to change or modify the record
AC-13 -	When authorised user review the audit history, the suer will be shown the decision timestamp and responsible user.


4.5	User Story to Value Mapping

User story 1:
View the list of students potentially at risk and their risk classification	
Expected Value: Help lecturer identify student who need support and reduce effort required to review student records individually.	
Stakeholder Benefiting: Lecturer and academic advisors

User story 2:
View high risk student, their contributing indicators and review or override recommendation	
Expected Value: Support prioritization, provides evidence for predictions and all9ow lecturer to use their judgement.	
Stakeholder Benefiting: Lecturer, academic advisor and student

User story 3:
Record the final decision and retain decision history	
Expected Value: Improve accountability, traceability and ability to review previous decisions	
Stakeholder Benefiting:Authorised academic staff and relevant administrator


4.6	Acceptance Test Summary 

Test :Login as authorised user	Expected Result :
System is accessible	
Related AC :AC-05

Test :Login as unauthorised user	
Expected Result :Access is denied	
Related AC :AC-05

Test :View Student list	
Expected Result :Risk recommendation displayed	
Related AC :AC-01

Test :Filter student by category	
Expected Result :Relevant selected category displayed	
Related AC :AC-03

Test :Open a student recommendation	
Expected Result :Relevant academic indicators and supporting evidence are displayed	
Related AC :AC-02,AC-06,AC-07

Test :Override Recommendation	
Expected Result :Lecturer can change the AI recommendation and the original recommendation remain available	
Related AC :AC-08,AC-09

Test :Invalid academic data input	
Expected Result :Input rejected with appropriate error displayed	
Related AC :AC-04

Test :Record final decision	
Expected Result :System save the decison	
Related AC :AC-10
