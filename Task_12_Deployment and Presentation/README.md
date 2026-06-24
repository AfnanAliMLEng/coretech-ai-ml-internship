# CoreTech AI Customer Churn Intelligence Platform

## Overview

The CoreTech AI Customer Churn Intelligence Platform is an end-to-end Machine Learning solution designed to predict customer churn and assist businesses in improving customer retention strategies.

The system analyzes customer demographics, subscription services, billing information, contract details, and behavioral patterns to determine whether a customer is likely to leave the company. Along with churn prediction, the platform provides risk assessment and business recommendations to support decision-making.

---

## Problem Statement

Customer churn is one of the biggest challenges for subscription-based businesses. Losing existing customers leads to reduced revenue and increased acquisition costs.

The objective of this project is to build an intelligent system capable of identifying customers at risk of churning before they leave, allowing businesses to take proactive retention measures.

---

## Dataset Information

**Dataset:** Telco Customer Churn Dataset

**Source:** Kaggle

**Total Records:** 7,043 Customers

**Target Variable:** Churn

The dataset contains customer demographics, service subscriptions, billing details, contract information, and account history.

---

## Data Preprocessing

The following preprocessing techniques were applied:

* Missing Value Analysis
* Duplicate Value Detection
* Data Cleaning
* Label Encoding
* Feature Scaling
* Feature Engineering
* Train-Test Split

### Engineered Features

To improve predictive performance, several business-oriented features were created:

* Customer Lifetime Value
* Contract Score
* Loyalty Score
* Revenue Segment
* Risk Score
* Risk Category
* Premium Customer Indicator

---

## Exploratory Data Analysis (EDA)

Comprehensive EDA was performed to identify customer behavior patterns.

### Visualizations

* Customer Churn Distribution
* Contract Type vs Churn
* Monthly Charges vs Churn
* Tenure Distribution
* Senior Citizen Analysis
* Correlation Heatmap
* Risk Category Analysis
* Feature Importance Analysis

### Key Findings

* Month-to-month customers are more likely to churn.
* Customers with shorter tenure exhibit higher churn risk.
* Higher monthly charges contribute to increased churn probability.
* Online Security and Tech Support services improve customer retention.
* Long-term customers demonstrate significantly lower churn rates.

---

## Machine Learning Models

The following algorithms were trained and evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting

### Final Selected Model

**Gradient Boosting Classifier**

| Metric                 | Score  |
| ---------------------- | ------ |
| Accuracy               | 80.34% |
| Cross Validation Score | 80.20% |
| ROC-AUC Score          | 84.23% |

The model demonstrated strong predictive capability and stable generalization performance.

---

## Streamlit Web Application

A professional Streamlit-based web application was developed for real-time churn prediction.

### Features

* Interactive Customer Information Form
* Real-Time Churn Prediction
* Churn Probability Calculation
* Risk Category Assessment
* Customer Profile Summary
* Business Recommendations
* User-Friendly Interface

---

## Business Recommendations

Based on model insights:

* Encourage long-term contract adoption.
* Offer targeted retention campaigns for high-risk customers.
* Promote Online Security and Tech Support services.
* Implement loyalty rewards for long-term subscribers.
* Monitor customers with high monthly charges and low tenure.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

---

## Project Structure

```text
Customer-Churn-Intelligence-Platform/

├── README.md
├── app.py
├── requirements.txt
├── Customer_Churn_Project.ipynb
│ 
├── customer_churn_model.pkl
├── scaler.pkl
├── feature_columns.pkl
│ 
├── Streamlit
│   ├── Interface.pdf (Google Drive Link)
│ 
├── Graphs/
│   ├── churn_distribution.png
│   ├── confusion_matrix.png
│   └── roc_curve.png
│
└── Demo_Video.mp4
```

---

## Results

The final system successfully predicts customer churn and provides actionable business insights. The project combines machine learning, data analytics, and deployment into a complete business intelligence solution.

---

## Conclusion

This project demonstrates the complete Machine Learning lifecycle, including data preprocessing, exploratory analysis, feature engineering, model training, evaluation, deployment, and business decision support.

The CoreTech AI Customer Churn Intelligence Platform provides organizations with a practical tool to identify churn risk, improve customer retention, and make data-driven business decisions.
