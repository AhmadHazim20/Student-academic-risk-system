# 6. LIGHTWEIGHT SYSTEM ARCHITECTURE

## 6.1 Architecture Overview

The proposed system uses layered architecture consisting of a user interface, application layer, data layer, AI model and decision layer. Lecturer and academic advisors enter or review students academic information through the user interface. The application validates and processes the data , while the data layer stores the relevant academic records. The AI model analyses the selected academic indicators and predicts an academic risk category. The decision layer presents the prediction and its explanation to the lecturer who reviews the results and decide whether further acade4mic support is needed.

## 6.2 System Components

### 6.2.1 User Interface

Allow the lecturer and academic advisors to review the student academic information, risk predictions and reports.

### 6.2.2 Application Layer

Handles user requests, validates academic data and coordinates coordination between components

### 6.2.3 Data layer

Stores relevant student academic records and prediction results.

### 6.2.4 AI model

Analyses selected academic indicators and classifies students into low, medium or high risk categories

### 6.2.5 Decision Layer

Presents the predicted risk and relevant explanation so that lecturers can review the results before deciding on further action.

### 6.2.6 Monitoring and Evaluation

Tracks model performance and prediction errors so that potential problems can be identified

## 6.3 Data Flow

- A lecturer or academic advisors logs into the system. Chooses the students academic information that is relevant
- The application looks over the input to find any details, incorrect entries or data that does not relevant
- The system pulls the needed records from the data storage layer
- An AI model examines the selected indicators and creates a risk prediction for the student
- The decision layer shows the risk category and the explanation that the lecturer can understand
- The lecturer review the prediction and decide if the student should get additional academic support
- The prediction outcome and relevant evaluations can be recorded for monitoring and future uses as long as privacy rules are followed.

## 6.4 Human in the Loop

A human decision is mandatory after the AI prediction. AI should not have the authority to finalise a decision on its own.

## 6.5 Architecture Design Rationale

The proposed system architecture is designed to make the AI assisted academic performance risk identification system easier to understand, develop, maintain and test. The system separate the user interface, application layer, data layer, AI model, and decision layer so that each component has its own responsibility. This separation allows academic data to be processed step by step before the AI model generate a prediction.

The architecture also takes into account the data privacy, model reliability and human oversight. The data layer manages student records while AI model classifies student into Low, Medium or high risk categories. The decision layer presents the predictions and relevant explanations to lecturers or academic advisors to review. This approach ensures that the AI assisted student academic performance risk identification system helps identify students who might need help without replacing human judgement. The monitoring and evaluation helps identify predictions errors and assess model performance over time. In summary, this architecture is the most suitable for the proposed system because it supports organised development, reliable predictions and responsible use of AI in education.
