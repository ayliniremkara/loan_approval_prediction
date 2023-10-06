# Loan Approval Prediction Project
For financial companies, it is of utmost importance to check their customers for eligibility for loans. In order to speed up the decision-making process utilization of machine learning models is much needed.
In this project, a machine learning model is created to predict whether customers are eligible for a loan based on their financial data. REST API is developed using Python and Flask to serve the trained model for production use. Additionally, Docker is used to containerize the application for production deployment. The project also includes logging and exception handling. 


## Setup and Run the Project

1) Firstly, in order to copy the project, clone the repository.

```bash
$ git clone https://github.com/ayliniremkara/loan_approval_prediction
$ cd loan_approval_prediction
```

2) Go to 'docker-compose.yml' file and change the volumes properly with your own host computer paths, so that volumes will be created successfully.


3) Build & run Docker containers
```bash
$ docker compose up
```

4) Test if flask app is up and running with the following request.
```bash
$ http://localhost:2222/
```
If you see `Welcome to Loan Prediction App!` as response it is working!

5) Time to use the prediction endpoint! You can find example POST request body in the `request_example` folder.
```bash
$ http://localhost:2222/predict
```







