# CoreTech AI Customer Churn Intelligence Platform

## Project Overview

This project presents an end-to-end AI-powered Customer Churn Intelligence Platform designed to predict customer churn and provide actionable business insights. The solution combines machine learning, feature engineering, business analytics, visualization, model optimization, and deployment into a single intelligent system.

Unlike a traditional churn prediction project that focuses only on model accuracy, this project emphasizes business value, explainability, and decision support.

---

## Dataset

**Dataset:** Telco Customer Churn Dataset

**Total Records:** 7,043 Customers

The dataset contains customer demographics, service subscriptions, billing information, contract details, and churn status.

---

## Project Workflow

* Data Cleaning & Validation
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Customer Segmentation
* Machine Learning Model Comparison
* Hyperparameter Optimization
* Feature Importance Analysis
* Business Intelligence Reporting
* Streamlit Deployment

---

## Unique Features of This Project

### Custom Feature Engineering

Instead of using only raw dataset features, several business-oriented features were created:

* Customer Lifetime Value (CLV)
* Contract Score
* Loyalty Score
* Risk Score
* Revenue Segment
* Risk Category
* Premium Customer Classification

These engineered features improved business understanding and model interpretability.

### Multi-Model Evaluation

Four machine learning models were compared:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting

The best-performing model was selected based on objective evaluation metrics rather than assumptions.

### Model Optimization

Gradient Boosting was further optimized using GridSearchCV hyperparameter tuning and validated through cross-validation to ensure stability and reliability.

### Explainable AI Approach

Feature importance analysis identified the strongest drivers of customer churn, enabling business stakeholders to understand why customers leave rather than simply receiving predictions.

### Business Intelligence Layer

The project goes beyond prediction and provides:

* Churn Risk Analysis
* Customer Segmentation
* Retention Recommendations
* Business Insights
* Decision Support Metrics

### Deployment Ready Solution

A complete Streamlit application was developed to allow real-time customer churn prediction and risk assessment through an interactive user interface.

---

## Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 79.6%    |
| Decision Tree       | 72.7%    |
| Random Forest       | 78.8%    |
| Gradient Boosting   | 80.3%    |

### Final Model Results

* Best Model: Gradient Boosting
* Accuracy: ~80%
* ROC-AUC Score: ~0.84
* Cross Validation Score: ~0.80

These results indicate strong predictive capability and stable performance on unseen data.

---

## Key Business Findings

The most influential factors affecting customer churn were:

* Contract Type
* Contract Score
* Risk Score
* Monthly Charges
* Online Security
* Technical Support
* Loyalty Score

The analysis revealed that customers with short-term contracts, lower loyalty, and higher risk profiles are significantly more likely to churn.

---

## Streamlit Application Features

* Customer Information Form
* Real-Time Churn Prediction
* Churn Probability Score
* Risk Category Assessment
* Customer Profile Summary
* Business Recommendations
* Retention Strategy Suggestions

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

---

## Conclusion

This project successfully transforms raw customer data into an intelligent churn prediction and business decision-support platform.

By combining advanced feature engineering, machine learning optimization, explainable AI techniques, business intelligence insights, and interactive deployment, the project delivers significantly more value than a standard churn prediction model and demonstrates a complete real-world AI/ML workflow from data analysis to deployment.
