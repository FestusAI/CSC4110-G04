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

## Smoke Test and Validation Review

### Contribution by Chirchir Collins — COM/0020/23

I reviewed the smoke-test procedure used to verify the Mulika SACCO loan-default prediction model.

The test loads the saved Random Forest pipeline from `models/G04_model.joblib` and generates predictions for three records from the held-out test dataset.

The recorded test results were default probabilities of 11.00%, 20.00% and 0.00%, with all three records classified as non-defaults. The test verifies that the model can load, generate three predictions and return probabilities within the valid range of 0 to 1.

**Validation limitations**

Although the smoke test confirms basic functionality, it does not establish model accuracy, fairness, probability calibration or suitability for real lending decisions.

I recommend retaining the separate classification evaluation and fairness analysis, verifying the application through its public Streamlit interface, and conducting additional testing using representative loan applications before operational use.

The provisional 30% referral threshold should also be validated specifically for the deployed Random Forest model.

The current application is a coursework demonstration,
not an approved real-world lending system.

Dataset and Reproducibility
Contribution by Collins Kipkorir — COM/0021/23
Dataset Description
The Mulika SACCO machine learning project uses the Credit Risk Dataset obtained from Kaggle.

Dataset source: https://www.kaggle.com/datasets/laotse/credit-risk-dataset

Dataset licence: CC0 — Public Domain

The original dataset contains 32,581 loan records and 12 columns. After cleaning and transformation, the final dataset contains 32,409 records and 25 columns.

The dataset contains borrower information, loan characteristics and credit-history information used to predict annual loan interest rates and loan defaults.
Dataset Files
The project contains three main datasets:
File	Description
data/credit_risk_dataset.csv	Original dataset before cleaning
data/stage1_credit.csv	Dataset after cleaning and missing-value handling
data/clean_credit.csv	Final transformed dataset used for machine learning


Data Preparation
During Task 2.1, duplicate records and invalid values were removed. Missing employment lengths were filled using the median, and missing interest rates were estimated using the median for the corresponding loan grade.

During Task 2.2, I transformed the data by encoding categorical features and creating additional variables, including age bands and logarithmic income.

The cleaned dataset was saved as data/clean_credit.csv.
Reproducing the Project
To reproduce the machine learning experiments:
1. Open the Group G04 project in Google Colab.
2. Connect the shared Google Drive folder.
3. Run G04_T01_setup.ipynb to verify the project environment.
4. Run G04_U2.1_cleaning.ipynb to reproduce the cleaning process.
5. Run G04_U2.2_eda_split.ipynb to reproduce the feature transformations and exploratory analysis.
6. Run the regression, classification, model evaluation, decision tree and neural network notebooks as required.
7. Run G04_U9.1_packaging_app.ipynb to reproduce the saved prediction pipeline.
8. Run the smoke test using python tests/smoke_test.py to verify model loading and predictions.
Reproducibility Settings
The machine learning experiments use random_state=42 for reproducibility where supported.

Training and testing data are separated to reduce data leakage. Numerical scaling is fitted using training data only and then applied to testing data.

For interest-rate regression, records containing imputed target values are excluded from model training, and loan_grade is removed because it is derived from interest rates.

The application dependencies are documented in app/requirements.txt.
Reproducibility Limitations
Although fixed random seeds help reproduce the experiments, results may vary across Python or library versions.

The dataset may not accurately represent current SACCO applicants or local lending conditions.

The saved model should be evaluated on representative new data before operational deployment.

The project is intended for educational demonstration and supports, but does not replace, human lending decisions.
