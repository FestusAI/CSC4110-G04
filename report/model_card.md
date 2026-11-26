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

## Human Oversight

The model supports but does not replace the loan officer.

Every application must receive appropriate human review.

A refused applicant must be given a clear reason and an
appropriate opportunity to seek clarification.

## Group Contributions

Each of the five members must review and contribute to
this model card and record their own GitHub commit.

The group must verify the dataset licence, threshold,
fairness findings and release requirements before approval.
