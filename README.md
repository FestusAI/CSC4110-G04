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

## Online Application

Public app URL: Not yet deployed.

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
