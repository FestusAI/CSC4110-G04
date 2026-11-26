# Group G04: Model smoke test

from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

# Locate the project root
ROOT = Path(__file__).resolve().parent.parent

# Locate the model and dataset
MODEL_PATH = ROOT / "models" / "G04_model.joblib"
DATA_PATH = ROOT / "data" / "clean_credit.csv"

# Check the required files
if not MODEL_PATH.is_file():
    raise FileNotFoundError("Trained model not found")

if not DATA_PATH.is_file():
    raise FileNotFoundError("Cleaned dataset not found")

# Load the saved model
model = joblib.load(MODEL_PATH)

# Load the cleaned dataset
df = pd.read_csv(DATA_PATH)

# Use the exact training features
features = [
    "person_age",
    "person_income",
    "person_home_ownership",
    "person_emp_length",
    "loan_intent",
    "loan_grade",
    "loan_amnt",
    "loan_percent_income",
    "cb_person_default_on_file",
    "cb_person_cred_hist_length"
]

X = df[features].copy()
y = df["loan_status"].astype(int)

# Reproduce previous-default encoding
X["cb_person_default_on_file"] = (
    X["cb_person_default_on_file"]
    .astype(str)
    .str.strip()
    .str.upper()
    .replace({"0": "N", "1": "Y"})
)

# Reproduce the original held-out test split
_, X_test, _, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42
)

# Select three test records
test_rows = X_test.iloc[:3]

# Make predictions
predictions = model.predict(test_rows)
probabilities = model.predict_proba(test_rows)[:, 1]

# Verify the outputs
if len(predictions) != 3:
    raise RuntimeError("Incorrect number of predictions")

if not all(0 <= p <= 1 for p in probabilities):
    raise RuntimeError("Invalid default probabilities")

# Display the predictions
print("MULIKA SACCO MODEL SMOKE TEST")

for i, (prediction, probability) in enumerate(
    zip(predictions, probabilities), start=1
):
    print(
        f"Loan {i}: Predicted={prediction}, "
        f"Default probability={probability:.2%}"
    )

print("\nSMOKE TEST PASSED!")
