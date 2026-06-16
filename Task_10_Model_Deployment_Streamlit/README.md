# Task 10: AI Model Deployment with Streamlit

## Intern
: **Name:** Afnan Ali

---

## Project Overview

This project demonstrates the deployment of a machine learning model using **Streamlit**. The optimized **Random Forest Classifier** developed in Task 09 was saved using Joblib and integrated into an interactive web application for real-time project status prediction.

The application allows users to enter project-related information and receive instant predictions through a simple and user-friendly interface.

---

## Model Information

**Model Used:** Random Forest Classifier

**Source:** Optimized Model from Task 09

**Prediction Target:** Project Status

Possible Predictions:

* Completed
* Delayed
* Failed

---

## Application Features

* Interactive Streamlit Web Interface
* User Input Form
* Real-Time Project Status Prediction
* Pre-trained Model Loading using Joblib
* Simple and Professional User Experience
* Reusable Machine Learning Deployment Workflow

---

## Input Parameters

The application accepts the following project-related inputs:

* Employees
* Annual Revenue
* Projects Completed
* Years With Company
* Customer Satisfaction

These features are passed to the trained model to generate project status predictions.

---

## Deployment Workflow

1. Load the optimized model from Task 09.
2. Create a Streamlit user interface.
3. Accept project information from users.
4. Generate predictions using the trained model.
5. Display results in real time.

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Google Colab
* GitHub

---

## Repository Structure

```text
Task_10/
│
├── app.py
├── project_status_model.pkl
├── requirements.txt
└── README.md
```

---

## Objective Achievement

The objective of this task was to deploy a trained machine learning model using Streamlit and create an interactive prediction application.

This objective was successfully achieved by integrating the optimized Random Forest model into a web-based interface capable of generating real-time project status predictions without requiring model retraining.

---

## Conclusion

This project successfully transformed a trained machine learning model into a deployable application. By integrating the optimized Random Forest model with Streamlit, a practical and user-friendly prediction system was developed. The project demonstrates the final stage of the machine learning lifecycle, where predictive models are deployed for real-world use and decision support.

---
