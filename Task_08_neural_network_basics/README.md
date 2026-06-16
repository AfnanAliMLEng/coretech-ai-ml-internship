# Task 08: Neural Network Basics with Keras — Project Status Prediction

## Intern Information

**Name:** Afnan Ali
**Education:** 2nd Year Information Technology Student
**City:** Kazi Ahmed, Sindh, Pakistan

---

# Project Overview

This project demonstrates the implementation of an Artificial Neural Network (ANN) using TensorFlow and Keras for project status prediction. The objective is to classify project outcomes based on various client and project-related features using deep learning techniques.

A custom dataset was created to simulate realistic business scenarios involving project management and client performance metrics. The project covers the complete machine learning workflow, including data preprocessing, neural network development, model training, evaluation, visualization, and comparison with a traditional machine learning model.

---

# Problem Statement

Predicting project outcomes is an important challenge for organizations. Factors such as customer satisfaction, company size, project history, and business performance can influence whether a project is completed successfully, delayed, or fails.

The objective of this project is to build an intelligent prediction system capable of classifying project status into:

* Completed
* Delayed
* Failed

using Artificial Neural Networks and comparing the results with a Random Forest classifier.

---

# Dataset Description

A custom dataset named **coretech_project_dataset.csv** was created specifically for this project to simulate realistic project management scenarios.

### Dataset Features

| Feature               | Description                                  |
| --------------------- | -------------------------------------------- |
| Client_ID             | Unique client identifier                     |
| Employees             | Total number of employees                    |
| Annual_Revenue        | Annual company revenue                       |
| Projects_Completed    | Number of completed projects                 |
| Years_With_Company    | Client relationship duration                 |
| Customer_Satisfaction | Customer satisfaction score                  |
| Project_Status        | Target variable (Completed, Delayed, Failed) |

### Dataset Characteristics

* 300 simulated project records
* Structured business dataset
* Multiple project outcome categories
* Suitable for classification and deep learning tasks

---

# Project Workflow

## 1. Data Preparation

The dataset was loaded and inspected to understand its structure and feature distribution.

### Preprocessing Steps

* Feature Selection
* Label Encoding of Target Variable
* Standardization using StandardScaler
* Train-Test Split

These steps ensured that the dataset was properly prepared for neural network training.

---

## 2. Exploratory Analysis

A project status distribution chart was generated to understand the balance of target classes and identify overall project outcome trends.

---

## 3. Artificial Neural Network Development

A Sequential Neural Network was built using TensorFlow and Keras.

### Network Architecture

* Input Layer
* Hidden Layer 1 → 64 Neurons (ReLU)
* Hidden Layer 2 → 32 Neurons (ReLU)
* Hidden Layer 3 → 16 Neurons (ReLU)
* Output Layer → Softmax Activation

### Training Configuration

* Optimizer: Adam
* Loss Function: Sparse Categorical Crossentropy
* Epochs: 50
* Batch Size: 16

This architecture allows the model to learn complex nonlinear relationships between project features and project outcomes.

---

## 4. Model Training and Evaluation

The neural network was trained using the prepared dataset and evaluated on unseen test data.

### Evaluation Metrics

* Accuracy Score
* Classification Report
* Confusion Matrix

These metrics provide insights into prediction quality and overall model performance.

---

## 5. Learning Curves Analysis

Two important visualizations were generated during training:

### Accuracy Curve

Shows the progression of training and validation accuracy throughout the learning process.

### Loss Curve

Displays how prediction error decreases as the model learns from data.

These curves help assess model convergence and generalization capability.

---

## 6. Traditional Machine Learning Comparison

To evaluate the effectiveness of deep learning, a Random Forest classifier was trained on the same dataset.

### Comparison Objective

The purpose of this comparison was to analyze whether a neural network provides better predictive performance than a traditional machine learning algorithm on structured business data.

### Comparison Result

Random Forest achieved slightly higher accuracy than the Artificial Neural Network.

This outcome is expected because the dataset is relatively small and consists of structured numerical features, where ensemble tree-based methods often perform exceptionally well.

Despite achieving slightly lower accuracy, the ANN successfully learned meaningful patterns and demonstrated strong predictive capability.

This comparison highlights an important machine learning principle: model selection should be based on dataset characteristics and problem requirements rather than model complexity alone.

---

# Visualizations Generated

The following visual outputs were generated during the project:

* Project Status Distribution Chart
* Training Accuracy Curve
* Validation Accuracy Curve
* Training Loss Curve
* Validation Loss Curve
* Confusion Matrix
* ANN vs Random Forest Comparison Chart

These visualizations provide a comprehensive understanding of model behavior and performance.

---

# Key Findings

### Project Prediction Performance

* The Artificial Neural Network achieved strong classification performance.
* The model successfully learned patterns from business-related project features.
* Customer satisfaction proved to be one of the most influential indicators of project outcomes.

### Model Comparison

* Random Forest achieved the highest accuracy on the current dataset.
* ANN demonstrated strong learning capability and effective generalization.
* Results confirm that traditional machine learning models can outperform deep learning models on smaller structured datasets.

---

# Business Insights

The developed predictive system can support organizations in identifying projects that may be delayed or at risk of failure.

Early prediction of project outcomes can help management:

* Improve resource allocation
* Reduce project risks
* Enhance customer satisfaction
* Optimize project planning strategies

Such predictive systems can contribute significantly to data-driven decision-making in project management environments.

---

# Technologies Used

* Python
* Pandas
* NumPy
* TensorFlow
* Keras
* Scikit-Learn
* Matplotlib
* Seaborn
* Google Colab
* GitHub

---

# Repository Structure

```text
Task_08/
│
├── task_08_neural_network_basics.ipynb
├── coretech_project_dataset.csv
├── class_distribution.png
├── accuracy_curve.png
├── loss_curve.png
├── confusion_matrix.png
├── model_comparison.png
└── README.md
```

---

# Learning Outcomes

Through this project, I gained practical experience in:

* Deep Learning Fundamentals
* Artificial Neural Networks
* TensorFlow and Keras
* Data Preprocessing
* Feature Scaling
* Classification Problems
* Model Evaluation
* Confusion Matrix Analysis
* Deep Learning Visualization
* Model Comparison Techniques

---

# Conclusion

This project successfully implemented a complete deep learning workflow using TensorFlow and Keras for project status prediction. A multi-layer Artificial Neural Network was developed, trained, and evaluated using industry-standard practices. The model demonstrated strong predictive performance and was further compared with a Random Forest classifier to analyze the strengths of deep learning versus traditional machine learning approaches.

The results highlight the importance of selecting models based on data characteristics and demonstrate how Artificial Neural Networks can be applied to solve real-world business prediction problems.


