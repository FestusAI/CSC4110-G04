# Mulika SACCO — Loan Risk Screening

## Project Overview

This project was developed by Group G04 for CSC 4110
Machine Learning at Kibabii University.

It uses the Credit Risk Dataset to predict loan interest
rates and estimate the probability of loan default.

The prediction app supports loan officers and does not
automatically approve or reject loan applications.

## Dataset

Dataset: Credit Risk Dataset
Source: https://www.kaggle.com/datasets/laotse/credit-risk-dataset
Licence: CC0 — Public Domain

Original dataset: 32,581 records
Cleaned dataset: 32,409 records

## Machine Learning Models

The group implemented Linear Regression, Logistic
Regression, Decision Trees, Random Forest, Gradient
Boosting, KNN, SVM and Neural Networks.

The deployed demonstration uses a Random Forest
classification pipeline saved as:

models/G04_model.joblib

## Group Members and Responsibilities

| Member | Assigned Tasks |
|---|---|
| Festus Ligeyo | Task 2.1 and Task 7 |
| Collins Kipkorir | Task 2.2 and Task 8 |
| Chirchir Collins | Task 3.1 and Task 5 |
| Peter Mbugua | Task 3.2 and Task 9.1 |
| Hartie Omuruon | Task 4 and Task 6 |

Tasks 1, 9.2 and 9.3 involve the whole group.

## How to Run the Notebooks

1. Open the notebooks folder.
2. Open the required notebook in Google Colab.
3. Mount Google Drive and select the project folder.
4. Run the code cells in order.

## How to Run the Streamlit App

Install the required packages:

```bash
pip install -r app/requirements.txt
```

Start the application from the project root:

```bash
streamlit run app/app.py
```

The app loads the saved Random Forest pipeline and
collects borrower details to calculate default risk.

## Streamlit Application Setup and Deployment

### Contribution by Peter Mbugua — COM/0039/23

### Application Overview

The Mulika SACCO Loan Default Risk Screening application was developed using Streamlit and a trained Random Forest classification pipeline.

The application allows a loan officer to enter applicant information and obtain an estimated probability of loan default.

The model supports human decision-making and does not automatically approve or reject loan applications.

### Application Requirements

The application requires:
- Python 3.13
- Streamlit
- Scikit-learn
- Pandas
- Joblib

The dependency versions are recorded in app/requirements.txt.

### Running the Application Locally

Open a terminal in the main CSC4110-G04 project directory.

Install the dependencies:

    pip install -r app/requirements.txt

Start the application:

    streamlit run app/app.py

Open the local Streamlit URL displayed in the terminal.

### Applicant Information

The application collects:
- Applicant age
- Annual income
- Home ownership
- Employment length
- Loan purpose
- Internally assigned loan grade
- Requested loan amount
- Credit history length
- Previous default history

The loan-to-income ratio is calculated automatically.

An internally assigned loan grade is required before prediction. The system must not guess this value.

### Prediction Results

After entering applicant details, the user clicks Predict Default Risk.

The application loads models/G04_model.joblib and calculates the estimated probability of default.

A provisional referral threshold of 30% is used.

Applicants above or equal to the threshold are flagged with the message "Refer to loan officer".

The threshold requires further validation before operational use.

### Online Deployment

The application is deployed using Streamlit Community Cloud.

Public URL:
https://mulika-sacco-g04.streamlit.app/

GitHub repository:
https://github.com/FestusAI/CSC4110-G04

Deployment configuration:
- Repository: FestusAI/CSC4110-G04
- Branch: main
- Main application: app/app.py
- Dependencies: app/requirements.txt
- Saved model: models/G04_model.joblib
- Python version: 3.13

### Troubleshooting

If the application reports a missing Python module, check app/requirements.txt and the deployment logs.

If the trained model cannot be loaded, confirm that models/G04_model.joblib exists and the required package versions are installed.

If the application fails to display, confirm that Streamlit is running app/app.py rather than tests/smoke_test.py.

The smoke test is available in tests/smoke_test.py and checks model loading and predictions.

### Responsible Use

This application is an educational demonstration.

Real applicant financial information should not be entered during public testing.

The model requires additional fairness, calibration and threshold validation before real-world use.

Final lending decisions must remain with qualified loan officers.


## Online Application

Public app URL: https://mulika-sacco-g04.streamlit.app/

This section will be updated after Streamlit Community
Cloud deployment.

## Guidance for SACCO Loan Officers

Enter the applicant's information into the screening
form and click Predict Default Risk.

The application estimates the probability of default
and indicates when additional loan-officer review is
required.

The 30% referral threshold is provisional and must be
validated before operational use.

The prediction supports human review and must never
be used as the sole reason to approve or reject a loan.

## Responsible AI

The model card is available at:

report/model_card.md

It documents model performance, fairness findings,
limitations, testing requirements and human oversight.

The current application is a coursework demonstration,
not an approved real-world lending system.
