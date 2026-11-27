# Mulika SACCO — Model Card

## Model Purpose

The model estimates the probability that a loan applicant
will default. It supports loan officers during application
review and must not automatically approve or reject loans.

## Intended Users

The intended users are trained SACCO loan officers and
authorised staff involved in reviewing loan applications.

## Data Source and Licence

**Dataset:** Credit Risk Dataset

**Dataset uploader:** Lao Tse (Kaggle username: laotse)

**Source:** https://www.kaggle.com/datasets/laotse/credit-risk-dataset

**Licence:** CC0 — Public Domain

**Download date:** 25 November 2026

**Original filename:** credit_risk_dataset.csv

**Original dataset size:** 32,581 rows and 12 columns.

**Cleaned dataset:** data/clean_credit.csv

The dataset contains historical-style borrower, loan and credit-history information used for educational credit-risk modelling.

### Data Cleaning and Preparation

The original dataset contained 32,581 records. During Task 2.1, 165 duplicate records, 5 records with impossible borrower ages and 2 records with impossible employment lengths were removed, leaving 32,409 records.

I filled 887 missing employment-length values using the median and 3,094 missing interest-rate values using the median interest rate of the corresponding loan grade. I also applied the Interquartile Range method to cap income outliers.

Records with imputed interest-rate targets were flagged so that they could be excluded from regression training.

### Data Limitations

- Missing-value imputation introduces estimated rather than observed values.
- Capping income outliers reduces the influence of extreme values but may remove meaningful variation.
- The dataset may not represent current Mulika SACCO applicants or local lending conditions.
- Historical patterns may not generalise to new borrowers.
- Dataset availability and reuse permission do not establish that a predictive model is fair or appropriate for real lending.

## Model and Features Used

Algorithm: Random Forest Classifier

Model file: models/G04_model.joblib

The model includes numerical and categorical preprocessing.

Input features:

- person_age
- person_income
- person_home_ownership
- person_emp_length
- loan_intent
- loan_grade
- loan_amnt
- loan_percent_income
- cb_person_default_on_file
- cb_person_cred_hist_length

The availability of internally assigned loan_grade must be
verified before deployment.

## Performance on Test Data

Held-out test records: 6482

At threshold 0.5:

- Accuracy: 0.9364
- Precision: 0.9736
- Recall: 0.7292
- F1-score: 0.8339

At provisional referral threshold 0.3:

- Accuracy: 0.9202
- Precision: 0.8426
- Recall: 0.7814
- F1-score: 0.8108

The referral threshold requires independent validation
before operational use.

## Fairness Check Results

The following table compares recall for actual defaulters
across home-ownership and age groups.

| Group Type | Group | Test Rows | Actual Defaults | Recall |
|---|---|---:|---:|---:|
| Home ownership | MORTGAGE | 2651 | 343 | 55.39% |
| Home ownership | OTHER | 23 | 5 | 80.00% |
| Home ownership | OWN | 533 | 42 | 95.24% |
| Home ownership | RENT | 3275 | 1028 | 85.02% |
| Age band | Under 25 | 2380 | 542 | 80.81% |
| Age band | 25-34 | 3238 | 710 | 75.49% |
| Age band | 35-44 | 712 | 138 | 80.43% |
| Age band | 45+ | 152 | 28 | 82.14% |

Largest observed home-ownership recall gap:
39.84 percentage points.

The largest observed difference is between OWN and
MORTGAGE borrowers.

Some groups have few actual defaults. Their recall
estimates may therefore be unreliable.

These differences require investigation and do not alone
establish discrimination.

### Review by Collins Kipkorir — Fairness and Data Quality

I reviewed the model's default recall across home-ownership and age groups.

The largest observed difference was between OWN borrowers, with recall of 95.24%, and MORTGAGE borrowers, with recall of 55.39%. This represents a gap of 39.85 percentage points and suggests that the model may perform unevenly across borrower groups.

The OTHER home-ownership group contained only five actual defaults, so its recall estimate is uncertain. The age group of 45 years and above also contained relatively few default cases.

The dataset was cleaned using missing-value imputation, outlier handling and duplicate removal. These steps improved data preparation but may affect the distribution of borrower characteristics.

I recommend further investigation of performance differences, validation on representative SACCO data and human review of lending decisions before operational deployment.

## Identifier and Leakage Checks

No input column names matched the screened personal
identifier terms.

No checked numeric input feature had an absolute
correlation greater than 0.95 with loan_status.

loan_grade was excluded from the reconstructed
interest-rate regression feature set.

These checks do not rule out every source of leakage.

## Limitations

- The dataset may not represent actual SACCO applicants.
- Predictions may be less reliable for unusual applicants.
- The model may perform differently across borrower groups.
- The model does not explain every reason for a default.
- The provisional threshold was not selected specifically
  for the deployed Random Forest using independent
  validation data.
- Historical patterns may reflect existing financial
  inequalities.

  ### Review by Hartie Omuruon — Classification Performance and Limitations

I reviewed the classification models developed during Tasks 4 and 6 to assess their suitability for loan-default screening.

The Random Forest achieved the highest reported test F1-score of 0.8333, followed by Gradient Boosting at 0.8254. SVM achieved an F1-score of 0.7333, while Balanced Logistic Regression achieved 0.6369.

Although Random Forest performed best in these experiments, it may be more difficult to explain than a simple decision tree or logistic regression model. Its performance could also change when applied to new applicants whose characteristics differ from the training data.

The model uses historical credit-risk information, which may contain patterns that do not represent the current SACCO applicant population. It also uses an internally assigned loan grade, which must be available before screening to avoid using unavailable information.

I recommend monitoring performance across borrower groups, checking probability calibration and validating the model using representative SACCO data before real deployment.

The model should support loan officers and must not automatically approve or reject loan applications.

## Who Should Not Use the Model

Applicants must not use this model to determine whether
they qualify for a loan.

The model must not be used to automatically deny loans.

It must not be used for real lending decisions without
appropriate validation, oversight and approval.

## Testing Before Release

Test data: the held-out 20% classification test split.

Proposed release targets, subject to group approval:

- Default recall of at least 0.80.
- F1-score of at least 0.75 at the selected threshold.
- Investigate substantial recall gaps between borrower
  groups before operational release.

These are proposed targets, not claims that the model
already meets them.

Before release, select and validate the decision threshold
without repeatedly tuning on the held-out test set.

The first pilot should involve a designated loan officer
and supervised demonstration using fictional applicants.

If the model fails the release checks, it should remain
a coursework demonstration.

### Review by Chirchir Collins — Model Evaluation and Release Testing

I reviewed the Random Forest model's evaluation results and the decision threshold used in the Mulika SACCO application.

At threshold 0.5, the model achieved 93.64% accuracy, 72.92% recall and an F1-score of 0.8339.

Reducing the threshold to 0.3 increased default recall to 78.14%, but precision decreased from 97.36% to 84.26% and F1-score decreased to 0.8108.

The model card proposes a minimum recall of 80% and an F1-score of 0.75 before release. Although the model meets the proposed F1-score requirement at threshold 0.3, its recall remains below the proposed minimum.

I recommend selecting and validating the decision threshold using a separate validation dataset rather than repeatedly adjusting it on the final test set. The predicted probabilities should also be checked for calibration.

Before operational deployment, the group should investigate the observed differences in recall across borrower groups, verify that the required input features are available at application time, and test the system with representative SACCO data.

The application should remain a supervised coursework demonstration until the release criteria are met and qualified loan officers have reviewed its performance.

## Human Oversight

The model supports but does not replace the loan officer.

Every application must receive appropriate human review.

A refused applicant must be given a clear reason and an
appropriate opportunity to seek clarification.

## Dataset and Reproducibility

### Contribution by Collins Kipkorir — COM/0021/23

### Dataset Description

The Mulika SACCO machine learning project uses the Credit Risk Dataset obtained from Kaggle.

**Dataset source:** https://www.kaggle.com/datasets/laotse/credit-risk-dataset

**Dataset licence:** CC0 — Public Domain

The original dataset contains 32,581 loan records and 12 columns. After cleaning and transformation, the final dataset contains 32,409 records and 25 columns.

The dataset contains borrower information, loan characteristics and credit-history information used to predict annual loan interest rates and loan defaults.

### Dataset Files

The project contains three main datasets:

| File | Description |
|---|---|
| `data/credit_risk_dataset.csv` | Original dataset before cleaning |
| `data/stage1_credit.csv` | Dataset after cleaning and missing-value handling |
| `data/clean_credit.csv` | Final transformed dataset used for machine learning |

### Data Preparation

During Task 2.1, duplicate records and invalid values were removed. Missing employment lengths were filled using the median, and missing interest rates were estimated using the median for the corresponding loan grade.

During Task 2.2, I transformed the data by encoding categorical features and creating additional variables, including age bands and logarithmic income.

The cleaned dataset was saved as `data/clean_credit.csv`.

### Reproducing the Project

To reproduce the machine learning experiments:

1. Open the Group G04 project in Google Colab.
2. Connect the shared Google Drive folder.
3. Run `G04_T01_setup.ipynb` to verify the project environment.
4. Run `G04_U2.1_cleaning.ipynb` to reproduce the cleaning process.
5. Run `G04_U2.2_eda_split.ipynb` to reproduce the feature transformations and exploratory analysis.
6. Run the regression, classification, model evaluation, decision tree and neural network notebooks as required.
7. Run `G04_U9.1_packaging_app.ipynb` to reproduce the saved prediction pipeline.
8. Run the smoke test using `python tests/smoke_test.py` to verify model loading and predictions.

### Reproducibility Settings

The machine learning experiments use `random_state=42` for reproducibility where supported.

Training and testing data are separated to reduce data leakage. Numerical scaling is fitted using training data only and then applied to testing data.

For interest-rate regression, records containing imputed target values are excluded from model training, and `loan_grade` is removed because it is derived from interest rates.

The application dependencies are documented in `app/requirements.txt`.

### Reproducibility Limitations

Although fixed random seeds help reproduce the experiments, results may vary across Python or library versions.

The dataset may not accurately represent current SACCO applicants or local lending conditions.

The saved model should be evaluated on representative new data before operational deployment.

The project is intended for educational demonstration and supports, but does not replace, human lending decisions.

## Group Contributions

Each of the five members must review and contribute to
this model card and record their own GitHub commit.

The group must verify the dataset licence, threshold,
fairness findings and release requirements before approval.

