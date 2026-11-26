# Mulika SACCO - Group G04 Loan Default Screening App

from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

# Resolve the project directory
ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "G04_model.joblib"

# Provisional threshold based on Task 5 analysis
THRESHOLD = 0.30

# Configure the Streamlit page
st.set_page_config(
    page_title="Mulika SACCO Loan Risk",
    page_icon="🏦",
    layout="wide", initial_sidebar_state="collapsed"
)


# Main application header

# Main application header
st.title("🏦 Mulika SACCO")
st.subheader("Loan Default Risk Screening")
st.caption("A machine learning decision-support tool for loan officers")

# Project information sidebar
with st.sidebar:
    st.header("Project Overview")
    st.write("**University:** Kibabii University")
    st.write("**Course:** CSC 4110")
    st.write("**Group:** G04")
    st.write("**Dataset:** Credit Risk Dataset")
    st.write("**Model:** Random Forest")
    st.write("**Referral Threshold:** 30% (Provisional)")

    st.divider()

    st.subheader("Project Team")
    st.write("Festus Ligeyo")
    st.write("Collins Kipkorir")
    st.write("Chirchir Collins")
    st.write("Peter Mbugua")
    st.write("Hartie Omuruon")

    st.divider()
    st.caption("Machine Learning Group Project")

# Important user guidance
st.info(
    "This application supports loan officers. "
    "It does not automatically approve or reject loans."
)

st.divider()

# Load the trained Random Forest model
@st.cache_resource
def load_pipeline():
    return joblib.load(MODEL_PATH)

# Check that the saved model exists
if not MODEL_PATH.is_file():
    st.error("Trained model file not found.")
    st.stop()

# Make the model available for predictions
model = load_pipeline()

st.header("Applicant Information")

st.caption(
    "Enter amounts in the same currency and units "
    "used by the original training dataset."
)

# Collect loan application details
with st.form("loan_application"):

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Applicant Age",
            min_value=18,
            max_value=100,
            value=30
        )

        income = st.number_input(
            "Annual Income",
            min_value=1.0,
            value=60000.0,
            step=1000.0
        )

        home = st.selectbox(
            "Home Ownership",
            ["RENT", "OWN", "MORTGAGE", "OTHER"]
        )

        employment = st.number_input(
            "Employment Length (Years)",
            min_value=0.0,
            max_value=60.0,
            value=4.0,
            step=0.5
        )

        previous_default = st.selectbox(
            "Previous Default on File",
            ["N", "Y"],
            format_func=lambda x: "Yes" if x == "Y" else "No"
        )

    with col2:
        intent = st.selectbox(
            "Loan Purpose",
            [
                "PERSONAL",
                "EDUCATION",
                "MEDICAL",
                "VENTURE",
                "HOMEIMPROVEMENT",
                "DEBTCONSOLIDATION"
            ]
        )

        grade = st.selectbox(
            "Internally Assigned Loan Grade",
            ["Select loan grade", "A", "B", "C", "D", "E", "F", "G"]
        )

        amount = st.number_input(
            "Requested Loan Amount",
            min_value=1.0,
            value=15000.0,
            step=500.0
        )

        credit_history = st.number_input(
            "Credit History Length (Years)",
            min_value=0,
            max_value=50,
            value=5
        )

    submitted = st.form_submit_button(
        "Predict Default Risk",
        use_container_width=True
    )

# Make a prediction only when the form is submitted
if submitted:

    # Do not guess or automatically assign a loan grade
    if grade == "Select loan grade":
        st.error(
            "An internally assigned loan grade is required. "
            "Please obtain the grade before screening."
        )
        st.stop()

    # Map letter grades to the encoded training values
    grade_value = ord(grade) - ord("A")

    # Calculate the loan-to-income ratio
    loan_percent_income = amount / income

    # Build one record with the exact training features
    applicant = pd.DataFrame([{
        "person_age": int(age),
        "person_income": float(income),
        "person_home_ownership": home,
        "person_emp_length": float(employment),
        "loan_intent": intent,
        "loan_grade": int(grade_value),
        "loan_amnt": float(amount),
        "loan_percent_income": float(loan_percent_income),
        "cb_person_default_on_file": previous_default,
        "cb_person_cred_hist_length": int(credit_history)
    }])

    # Calculate the estimated probability of default
    probability = float(
        model.predict_proba(applicant)[0, 1]
    )

    st.divider()
    st.header("Prediction Result")

    st.metric(
        "Estimated Probability of Default",
        f"{probability * 100:.2f}%"
    )

    st.progress(min(max(probability, 0.0), 1.0))

    # Apply the provisional referral threshold
    if probability >= THRESHOLD:
        st.warning("Refer to loan officer")
        st.write(
            "This application requires further "
            "assessment by a loan officer."
        )
    else:
        st.success("Below provisional referral threshold")
        st.write(
            "A loan officer must still complete "
            "the normal application review."
        )

    st.caption(
        "The 30% referral threshold is provisional. "
        "It was investigated in Task 5 using another "
        "classifier and must be validated separately "
        "for this Random Forest before real use."
    )

st.divider()
st.caption(
    "CSC 4110 | Kibabii University | Group G04"
)
