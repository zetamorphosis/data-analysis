# ❤️ Heart Disease Prediction Using Machine Learning

This project focuses on predicting heart disease using supervised machine learning algorithms.  
The dataset used is the Cleveland Heart Disease dataset, and the objective is to classify whether a patient has heart disease (binary classification).

---

## Project Overview

This project includes:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Scaling
- Model Training & Evaluation
- Model Comparison

Three machine learning models were implemented:

- Decision Tree
- Logistic Regression
- Naive Bayes (GaussianNB)

---

## Dataset

Dataset: Cleveland Heart Disease Dataset  
Features include:

- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Rest ECG (restecg)
- Maximum Heart Rate (thalach)
- Exercise Induced Angina (exang)
- Oldpeak
- Slope
- Number of Major Vessels (ca)
- Thalassemia (thal)

Target variable:
- 0 = No Heart Disease
- 1 = Heart Disease

---

## Data Preprocessing

- Converted multi-class target into binary classification
- Handled missing values in `ca` and `thal`
- Converted non-numeric values into numeric
- Applied StandardScaler for feature scaling
- Split dataset into training and testing set (80:20)

---

## Models Used

### Decision Tree Classifier
- Non-linear classification model
- Evaluated using confusion matrix & accuracy

### Logistic Regression
- Linear classification model
- Suitable for binary classification

### Naive Bayes (GaussianNB)
- Probabilistic classification approach
- Fast and effective baseline model

---

## Evaluation Metrics

- Accuracy (Training & Testing)
- Confusion Matrix

Model performance comparison helps determine the most suitable classifier for this dataset.

---

## Tools & Libraries

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn
- Jupyter Notebook
