
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, chi2

df = pd.read_csv("employee_data.csv")

df["Salary"] = df["Salary"].fillna(df["Salary"].median())

df = df.drop_duplicates()

le = LabelEncoder()

df["Department"] = le.fit_transform(df["Department"])
df["Promoted"] = le.fit_transform(df["Promoted"])

df = pd.get_dummies(df, columns=["City"])

scaler = StandardScaler()

df[["Age","Salary"]] = scaler.fit_transform(df[["Age","Salary"]])

X = df.drop("Promoted", axis=1)
y = df["Promoted"]

X_positive = X - X.min() + 1

selector = SelectKBest(score_func=chi2, k=3)
selector.fit(X_positive, y)

df.to_csv("cleaned_employee_data.csv", index=False)

before = 6
after = len(df)

plt.figure(figsize=(6,4))
plt.bar(["Before","After"], [before, after])
plt.title("Data Cleaning Comparison")
plt.savefig("comparison_chart.png")
plt.show()

print("Task Completed")
