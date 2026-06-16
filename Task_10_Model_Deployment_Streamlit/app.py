
import streamlit as st
import joblib
import numpy as np

model = joblib.load(
    "project_status_model.pkl"
)

st.title(
    "CoreTech Project Status Predictor"
)

st.info(
    "This application predicts project status using an optimized Random Forest model developed during Task 09."
)

st.subheader(
    "AI-Powered Project Analytics Dashboard"
)

employees = st.number_input(
    "Employees"
)

annual_revenue = st.number_input(
    "Annual Revenue"
)

projects_completed = st.number_input(
    "Projects Completed"
)

years_with_company = st.number_input(
    "Years With Company"
)

customer_satisfaction = st.number_input(
    "Customer Satisfaction"
)

if st.button(
    "Predict Project Status"
):

    data = np.array([[

        employees,

        annual_revenue,

        projects_completed,

        years_with_company,

        customer_satisfaction

    ]])

    prediction = model.predict(
        data
    )

    st.success(
        f"Predicted Status: {prediction[0]}"
    )

st.markdown("---")

st.write(
    "Model Used: Optimized Random Forest"
)

st.write(
    "Source: Task 09 Model Optimization Project"
)
