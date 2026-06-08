
# Task 05: Supervised Learning Classification

## Objective
Build classification models to predict project status using supervised machine learning techniques.

## Models Used
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

## Steps Performed
1. Loaded the dataset
2. Preprocessed the data
3. Split data into training and testing sets
4. Trained Logistic Regression model
5. Trained Decision Tree model
6. Trained Random Forest model
7. Evaluated models using Accuracy Score, Confusion Matrix, and Classification Report
8. Visualized Confusion Matrix using Heatmap
9. Compared model performance

## Results
- Logistic Regression Accuracy: 0.85  
- Decision Tree Accuracy: 1.00
- Random Forest Accuracy: 1.00

## Models Evaluation
Supervised Learning Classification

### Evaluation Metrics
The models were evaluated using:
- Accuracy Score
- Confusion Matrix
- Classification Report

### Best Model

#### Random Forest Classifier

Random Forest was selected as the best-performing model because it achieved the highest accuracy score among all tested models. It also produced fewer classification errors in the confusion matrix and demonstrated better precision, recall, and F1-score.

#### Why Random Forest is Best

- It combines multiple decision trees, reducing overfitting.
- It provides more stable and accurate predictions than a single Decision Tree.
- It handles complex relationships in the data effectively.
- It achieved the best overall performance on the test dataset.

## Files Included
- classification_task.ipynb
- confusion_matrix_heatmap.png
- README.md
- CoreTech_Project_Status.csv

## Author
Afnan Ali
CoreTech AI/ML Internship

## Short Analysis
Three classification models were trained to predict project status: Logistic Regression, Decision Tree, and Random Forest. Performance was evaluated using Accuracy Score, Confusion Matrix, and Classification Report. Random Forest achieved the highest accuracy and showed fewer misclassifications in the confusion matrix. Therefore, Random Forest was selected as the best model because it combines multiple decision trees and generally provides better generalization on unseen data.






with open("README.md", "w") as f:
    f.write(readme_content)
