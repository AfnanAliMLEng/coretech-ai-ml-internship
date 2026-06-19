
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# Load Model Files
model = joblib.load("customer_churn_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="CoreTech AI Customer Churn Intelligence Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# PREMIUM CSS
# ==========================================================

st.markdown("""
<style>

.main {
    background: linear-gradient(
        135deg,
        #f8fafc,
        #e0f2fe
    );
}

.block-container{
    padding-top:1rem;
}

.hero {
    padding:35px;
    border-radius:25px;
    text-align:center;

    background: linear-gradient(
        135deg,
        #2563eb,
        #7c3aed
    );

    color:white;

    box-shadow:
    0px 10px 25px rgba(
        0,
        0,
        0,
        0.20
    );
}

.metric-card{

    background:white;

    padding:15px;

    border-radius:15px;

    box-shadow:
    0px 4px 15px rgba(
        0,
        0,
        0,
        0.10
    );
}

.result-card{

    background:white;

    padding:20px;

    border-radius:20px;

    box-shadow:
    0px 4px 15px rgba(
        0,
        0,
        0,
        0.10
    );
}

.stButton>button{

    width:100%;

    height:60px;

    font-size:20px;

    font-weight:bold;

    border-radius:15px;

    background:
    linear-gradient(
        135deg,
        #2563eb,
        #7c3aed
    );

    color:white;
}

.stButton>button:hover{

    background:
    linear-gradient(
        135deg,
        #1d4ed8,
        #6d28d9
    );

    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("""
<div class="hero">

<h1>
CoreTech AI Customer Churn Intelligence Platform
</h1>

<h4>
Advanced Machine Learning for Customer Retention Intelligence
</h4>

<p>
Predict customer churn risk, evaluate customer health,
and generate actionable business recommendations.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# DASHBOARD KPIs
# ==========================================================

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.metric(
        "Accuracy",
        "80.34%"
    )

with col2:

    st.metric(
        "Cross Validation",
        "80.20%"
    )

with col3:

    st.metric(
        "ROC-AUC",
        "84.23%"
    )

with col4:

    st.metric(
        "Customers",
        "7043"
    )

st.write("")

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.image(
    "IMG_20260529_145745.png",
    width=120
)

st.sidebar.markdown("""
### Afnan Ali

AI & Machine Learning Engineer

CoreTech AI Internship Project
""")

st.sidebar.title(
    "CoreTech AI"
)

st.sidebar.markdown("""
### Platform Overview

This intelligent system predicts:

✔ Customer Churn

✔ Risk Category

✔ Customer Health

✔ Retention Recommendations

✔ Business Insights
""")

st.sidebar.info("""
Machine Learning Model

Gradient Boosting Classifier

Accuracy: 80.34%
""")



st.markdown("""
## 👤 Customer Information

Provide customer details below to
generate churn prediction and
business intelligence insights.
""")

# Customer Inputs
# ==========================================================
# CUSTOMER INPUT SECTIONS
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("### 👤 Customer Profile")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        24
    )

with col2:

    st.markdown("### 📡 Services")

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

with col3:

    st.markdown("### 💳 Billing & Contract")

    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
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
st.markdown("---")

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

if st.button(
    "🚀 Analyze Customer Risk"
):
    input_data = input_data[feature_columns]
    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]
    health_score = round(
    100 - (probability * 100),
    2
    )

    st.markdown("""
    # 📊 Customer Intelligence Report
    """)

    if prediction == 1:
        st.error("⚠️ High Risk of Churn")
    else:
        st.success("✅ Customer Likely to Stay")

    st.markdown("---")

    st.subheader(
       "📈 Executive Risk Dashboard"
    )

    m1,m2,m3,m4 = st.columns(4)

    with m1:

     st.metric(
          "Churn Probability",
          f"{probability*100:.2f}%"
     )

    with m2:

        st.metric(
            "Customer Health",
            f"{health_score}/100"
        )

    with m3:

        st.metric(
            "Monthly Revenue",
            f"${monthly_charges:.2f}"
        )

    with m4:

        st.metric(
            "Lifetime Value",
            f"${customer_lifetime_value:.2f}"
        )
    st.subheader(
        "⚠ Risk Assessment"
    )

    st.progress(
        int(probability * 100)
    )

    if probability < 0.30:
        risk = "Low Risk"
    elif probability < 0.70:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    st.subheader("Risk Category")
    if risk == "High Risk":

        st.error(
            "🔴 HIGH RISK CUSTOMER"
        )

    elif risk == "Medium Risk":

        st.warning(
            "🟡 MEDIUM RISK CUSTOMER"
        )

    else:

        st.success(
            "🟢 LOW RISK CUSTOMER"
        )


    st.subheader(
        "🎯 Churn Probability Gauge"
    )

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=probability * 100,

            title={
                "text":"Churn Probability %"
            },

            gauge={

                "axis":{
                    "range":[0,100]
                },

                "bar":{
                    "color":"darkblue"
                },

                "steps":[

                    {
                        "range":[0,30],
                        "color":"lightgreen"
                    },

                    {
                        "range":[30,70],
                        "color":"gold"
                    },

                    {
                        "range":[70,100],
                        "color":"salmon"
                    }
                ]
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )




    st.subheader(
        "❤️ Customer Health Visualization"
    )

    health_fig = go.Figure(

        data=[

            go.Pie(

                labels=[
                    "Healthy",
                    "Churn Risk"
                ],

                values=[
                    health_score,
                    100-health_score
                ],

                hole=0.65
            )
        ]

    )

    st.plotly_chart(
        health_fig,
        use_container_width=True
    )




    st.subheader(
    "🤖 AI Business Insight"
    )

    if risk == "High Risk":

        st.error(f"""
        This customer shows a strong probability of churn.

        Key Factors:

        • Tenure: {tenure} Months

        • Monthly Charges: ${monthly_charges:.2f}

        • Loyalty Score: {loyalty_score}

        Business Impact:

        This customer represents a potential revenue loss and should be prioritized for retention campaigns.
        """)

    elif risk == "Medium Risk":

        st.warning(f"""
        This customer shows moderate churn risk.

        Key Factors:

        • Tenure: {tenure} Months

        • Monthly Charges: ${monthly_charges:.2f}

        • Loyalty Score: {loyalty_score}

        Business Impact:

        Customer engagement initiatives may improve retention probability.
        """)

    else:

        st.success(f"""
        This customer demonstrates strong retention potential.

        Key Factors:

        • Long Customer Relationship

        • Stable Revenue Contribution

        • Positive Loyalty Indicators

        Business Impact:

        Customer is likely to remain active and continue generating revenue.
        """)





    st.subheader("Customer Profile Summary")

    profile_df = pd.DataFrame({

    "Metric":[

        "Tenure",

        "Monthly Charges",

        "Lifetime Value",

        "Contract Score",

        "Loyalty Score",

        "Risk Score"

    ],

    "Value":[

        tenure,

        monthly_charges,

        customer_lifetime_value,

        contract_score,

        loyalty_score,

        round(
            risk_score,
            2
        )
    ]

    })

    st.dataframe(
    profile_df,
    use_container_width=True
    )


    st.subheader(
        "🏷 Customer Segment"
    )

    if premium_customer == 1:

        st.success(
            "Premium Customer"
        )

    elif monthly_charges > 60:

        st.info(
            "High Revenue Customer"
        )

    else:

        st.warning(
         "Standard Customer"
        )



    st.subheader(
    "📋 Executive Summary"
    )

    st.info(f"""
    Customer Overview

    • Churn Probability:
    {probability*100:.2f}%

    • Customer Health:
    {health_score}/100

    • Risk Category:
    {risk}

    • Monthly Revenue:
    ${monthly_charges:.2f}

    • Lifetime Value:
    ${customer_lifetime_value:.2f}

    This summary provides an executive-level view of customer retention risk and business impact.
    """)



    st.subheader(
    "🎯 Retention Strategy"
    )

    if risk == "High Risk":

        col1,col2 = st.columns(2)

        with col1:

            st.warning("""
            ### Immediate Actions

            ✔ Offer Retention Discount

            ✔ Upgrade Customer Support

            ✔ Personalized Outreach
            """)

        with col2:

            st.error("""
            ### Critical Actions

            ✔ Assign Relationship Manager

            ✔ Contract Upgrade Campaign

            ✔ Priority Follow-up
            """)

    elif risk == "Medium Risk":

        col1,col2 = st.columns(2)

        with col1:

            st.info("""
            ### Recommended Actions

            ✔ Customer Engagement

            ✔ Promotional Offers

            ✔ Service Optimization
            """)

        with col2:

            st.info("""
            ### Monitoring Actions

            ✔ Usage Monitoring

            ✔ Satisfaction Survey

            ✔ Loyalty Campaign
            """)

    else:

        col1,col2 = st.columns(2)

        with col1:

            st.success("""
            ### Growth Actions

            ✔ Loyalty Rewards

            ✔ Upselling Opportunities

            ✔ Premium Plans
            """)

        with col2:

            st.success("""
            ### Retention Actions

            ✔ Maintain Engagement

            ✔ Customer Appreciation

            ✔ Exclusive Benefits
            """)


    report = f"""
    CUSTOMER CHURN REPORT

    Prediction:
    {prediction}

    Risk:
    {risk}

    Churn Probability:
    {probability*100:.2f}%

    Customer Health:
    {health_score}/100

    Monthly Charges:
    ${monthly_charges:.2f}

    Lifetime Value:
    ${customer_lifetime_value:.2f}
    """

    st.download_button(

        label="📥 Download Report",

        data=report,

        file_name="customer_churn_report.txt",

        mime="text/plain"
    )

st.markdown("---")

st.markdown("""

<div style='text-align:center;'>

<h3>
CoreTech AI Customer Churn Intelligence Platform
</h3>

<p>

Machine Learning • Business Intelligence • Streamlit

</p>

<p>

Developed by Afnan Ali

</p>

</div>

""",
unsafe_allow_html=True)