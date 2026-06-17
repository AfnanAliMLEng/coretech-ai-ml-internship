
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load Model Files
model = joblib.load("customer_churn_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")


st.set_page_config(
    page_title="CoreTech AI Customer Churn Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 CoreTech AI Customer Churn Intelligence Platform")

st.markdown("""
This application predicts customer churn risk using Machine Learning and provides business recommendations for customer retention.
""")

st.header("Customer Information")

# Customer Inputs
gender = st.selectbox("Gender", ["Male", "Female"])

senior = st.selectbox("Senior Citizen", [0, 1])

partner = st.selectbox("Partner", ["No", "Yes"])

dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.slider(
    "Tenure (Months)",
    0,
    72,
    24
)

phone_service = st.selectbox(
    "Phone Service",
    ["No", "Yes"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["No", "Yes"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["No", "Yes"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["No", "Yes"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["No", "Yes"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["No", "Yes"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes"]
)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1500.0
)

# Feature Engineering
contract_score_map = {
    "Month-to-month": 1,
    "One year": 2,
    "Two year": 3
}

contract_score = contract_score_map[contract]

customer_lifetime_value = (
    tenure * monthly_charges
)

loyalty_score = (
    tenure * contract_score
)

risk_score = (
    (72 - tenure)
    + (monthly_charges / 10)
)

premium_customer = 1 if (
    monthly_charges > 80
    and tenure > 24
) else 0

if monthly_charges < 35:
    revenue_segment = 0
elif monthly_charges < 65:
    revenue_segment = 1
elif monthly_charges < 90:
    revenue_segment = 2
else:
    revenue_segment = 3

if risk_score < 30:
    risk_category = 0
elif risk_score < 60:
    risk_category = 1
else:
    risk_category = 2

# Encoding
binary_map = {
    "No": 0,
    "Yes": 1
}

gender_map = {
    "Male": 1,
    "Female": 0
}

internet_map = {
    "DSL": 0,
    "Fiber optic": 1,
    "No": 2
}

contract_map = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}

payment_map = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer (automatic)": 2,
    "Credit card (automatic)": 3
}

input_data = pd.DataFrame(
    [[0] * len(feature_columns)],
    columns=feature_columns
)
input_data["customerID"] = 0
input_data["gender"] = gender_map[gender]
input_data["SeniorCitizen"] = senior
input_data["Partner"] = binary_map[partner]
input_data["Dependents"] = binary_map[dependents]
input_data["tenure"] = tenure
input_data["PhoneService"] = binary_map[phone_service]
input_data["MultipleLines"] = binary_map[multiple_lines]
input_data["InternetService"] = internet_map[internet_service]
input_data["OnlineSecurity"] = binary_map[online_security]
input_data["OnlineBackup"] = binary_map[online_backup]
input_data["DeviceProtection"] = binary_map[device_protection]
input_data["TechSupport"] = binary_map[tech_support]
input_data["StreamingTV"] = binary_map[streaming_tv]
input_data["StreamingMovies"] = binary_map[streaming_movies]
input_data["Contract"] = contract_map[contract]
input_data["PaperlessBilling"] = binary_map[paperless_billing]
input_data["PaymentMethod"] = payment_map[payment_method]
input_data["MonthlyCharges"] = monthly_charges
input_data["TotalCharges"] = total_charges

input_data["CustomerLifetimeValue"] = customer_lifetime_value
input_data["ContractScore"] = contract_score
input_data["LoyaltyScore"] = loyalty_score
input_data["RevenueSegment"] = revenue_segment
input_data["RiskScore"] = risk_score
input_data["RiskCategory"] = risk_category
input_data["PremiumCustomer"] = premium_customer

if st.button("Analyze Customer"):
    input_data = input_data[feature_columns]
    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Churn")
    else:
        st.success("✅ Customer Likely to Stay")

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    if probability < 0.30:
        risk = "Low Risk"
    elif probability < 0.70:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    st.subheader("Risk Category")
    st.write(risk)

    st.subheader("Customer Profile Summary")

    st.write(f"Tenure: {tenure} Months")
    st.write(f"Monthly Charges: ${monthly_charges:.2f}")
    st.write(f"Customer Lifetime Value: ${customer_lifetime_value:.2f}")
    st.write(f"Loyalty Score: {loyalty_score}")

    st.subheader("Business Recommendation")

    if risk == "High Risk":
        st.warning("""
        • Offer retention discounts

        • Upgrade support services

        • Encourage long-term contracts

        • Assign customer success representative
        """)

    elif risk == "Medium Risk":
        st.info("""
        • Monitor customer engagement

        • Offer promotional plans

        • Improve customer communication
        """)

    else:
        st.success("""
        • Maintain current relationship

        • Continue loyalty rewards

        • Encourage premium service adoption
        """)