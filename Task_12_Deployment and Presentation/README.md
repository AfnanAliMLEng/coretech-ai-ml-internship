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

# Machine Learning Model Development

Multiple supervised Machine Learning algorithms were trained and evaluated to identify the most effective model for customer churn prediction.

Each model was trained using the same preprocessed dataset and evaluated based on multiple performance metrics to ensure a fair comparison.

## Models Evaluated

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* Gradient Boosting Classifier

The comparative analysis helped determine the model that provided the best balance between predictive accuracy, stability, and generalization performance.

---

# Model Performance

| Model                 |   Accuracy |
| --------------------- | ---------: |
| Logistic Regression   |     79.60% |
| Decision Tree         |     72.70% |
| Random Forest         |     78.80% |
| **Gradient Boosting** | **80.34%** |

## Final Selected Model

After evaluating all machine learning models, **Gradient Boosting Classifier** achieved the best overall performance and was selected as the final deployment model.

### Final Evaluation Metrics

| Metric                 | Score      |
| ---------------------- | ---------- |
| Accuracy               | **80.34%** |
| Cross Validation Score | **80.20%** |
| ROC-AUC Score          | **84.23%** |

The final model demonstrated strong predictive capability while maintaining stable performance on unseen data.

---

# Model Optimization

To further improve model performance and reliability, **GridSearchCV** was used to perform hyperparameter tuning on the Gradient Boosting Classifier.

Different parameter combinations were evaluated systematically to identify the optimal configuration.

The optimized model was validated using **Cross-Validation**, ensuring that the results were consistent across multiple data splits and reducing the likelihood of overfitting.

---

# Model Evaluation

The final model was evaluated using several performance assessment techniques to ensure robustness and reliability.

Evaluation methods included:

* Accuracy Score
* Cross Validation
* ROC-AUC Score
* Classification Metrics
* Feature Importance Analysis

These evaluation techniques confirmed that the model generalized well and was suitable for deployment in a real-world customer churn prediction system.

---

# Explainable AI

To improve transparency and business interpretability, **Feature Importance Analysis** was performed.

This analysis identified the most influential factors contributing to customer churn, enabling business stakeholders to understand **why** predictions were made rather than simply receiving a prediction.

The most influential features included:

* Contract Type
* Contract Score
* Risk Score
* Monthly Charges
* Online Security
* Technical Support
* Loyalty Score

This explainable approach transforms the model into a valuable business decision-support tool rather than a simple prediction system.

---
# Streamlit Web Application

A professional **Streamlit-based Customer Churn Intelligence Dashboard** was developed to deploy the trained machine learning model and enable real-time churn prediction through an interactive web interface.

The application is designed to be user-friendly while providing meaningful business intelligence for decision-makers.

## Features

* Interactive Customer Information Form
* Real-Time Customer Churn Prediction
* Churn Probability Calculation
* Customer Risk Category Assessment
* Customer Profile Summary
* Business Recommendations
* Retention Strategy Suggestions
* Professional Business Intelligence Dashboard

---

# Running the Application Locally

Follow these steps to run the project on your local machine.

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Customer-Churn-Intelligence-Platform.git
cd Customer-Churn-Intelligence-Platform
```

## Step 2: Install Required Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Launch the Streamlit Application

```bash
streamlit run app.py
```

## Step 4: Open in Browser

Once the application starts, open your browser and visit:

```text
http://localhost:8501
```

---

# Technologies Used

### Programming Language

* Python

### Libraries & Frameworks

* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

### Machine Learning Techniques

* Feature Engineering
* Label Encoding
* Feature Scaling
* GridSearchCV
* Cross Validation
* Gradient Boosting Classifier

---

# 📂 Repository Structure

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
├── Dataset/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── Graphs/
│   ├── churn_distribution.png
│   ├── correlation_heatmap.png
│   ├── monthly_charges_vs_churn.png
│   ├── risk_categories.png
│   ├── roc_curve.png
│   ├── seniorcitizen_vs_churn.png
│   └── tenure_distribution.png
│
├── Streamlit/
│   └── Interface.pdf (Google Drive Link)
│
└── Demo_Video/
    └── Demo Video (Google Drive Link)
```

---

# Business Impact

This platform provides practical value for businesses by:

* Predicting customer churn before it occurs.
* Identifying customers with high churn risk.
* Supporting targeted customer retention strategies.
* Reducing customer acquisition costs.
* Improving long-term customer satisfaction.
* Assisting management with data-driven business decisions.

Instead of relying on manual analysis, organizations can use this intelligent system to proactively reduce customer loss and strengthen customer relationships.

---

# Future Enhancements

Potential improvements for future versions include:

* Real-time database integration.
* Cloud deployment using Streamlit Community Cloud or Microsoft Azure.
* REST API integration for enterprise applications.
* Explainable AI using SHAP values.
* Interactive dashboards using Power BI or Tableau.
* Automated customer retention campaign recommendations.

---

# Results

The final Customer Churn Intelligence Platform successfully predicts customer churn while providing actionable business insights through an interactive dashboard.

The project combines machine learning, feature engineering, business intelligence, explainable AI, and deployment into a complete end-to-end solution capable of supporting real-world customer retention strategies.

---

# Conclusion

This project demonstrates the complete Machine Learning lifecycle, including data preprocessing, exploratory data analysis, feature engineering, model development, optimization, evaluation, explainability, deployment, and business decision support.

By combining predictive analytics with business intelligence, the **CoreTech AI Customer Churn Intelligence Platform** delivers more than a churn prediction model—it provides a practical decision-support system that enables organizations to identify at-risk customers, improve retention strategies, and make informed, data-driven decisions.

---

# Acknowledgements

This project was developed as part of the **CoreTech AI & Machine Learning Internship Program**.

I would like to express my sincere gratitude to the mentors and instructors of the internship for providing valuable guidance, practical learning opportunities, and the experience of working on a real-world Machine Learning project.
