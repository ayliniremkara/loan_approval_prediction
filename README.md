# Loan Approval Prediction Project
For financial companies, it is of utmost importance to check their customers for eligibility for loans. In order to speed up the decision-making process utilization of machine learning models is much needed.
In this project, a machine learning model is created to predict whether customers are eligible for a loan based on their financial data. Additionally, REST API is developed using Python and Flask to serve the trained model for production use. Additionally, Docker is used to containerize the application for production deployment. The project also includes logging and exception handling. 

## Table of Contents
- [Technologies](#tech)
- [Task 1: Training and Evaluating the Model](#task-1)
- [Task 2: Developing a REST API and Deployment](#task-2)

    
## Technologies
The project is created with:
- Python 3.11
- Flask 3.0.0
- Gunicorn 21.2.0
- Pandas 2.1.1
- Joblib 1.3.2
- Scikit-learn 1.3.1
- Docker 24.0.6



##Setup and Run the Project

Firstly, in order to copy the project, clone the repository.

```bash
git clone https://github.com/ayliniremkara/loan_approval_prediction
cd loan_approval_prediction
```

Build docker. 

```bash

$ docker build  loan-approval-prediction .

```

Run docker. 

```bash

$ docker run -p 5000:5000 loan-approval-prediction

```






