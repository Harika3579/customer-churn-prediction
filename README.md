# Customer Churn Prediction System

## Overview

This project predicts whether a telecom customer is likely to leave the service (churn) using Machine Learning algorithms.

The system analyzes customer behavior, billing information, internet services, contract types, and account details to identify customers at risk of churn.

This is a complete end-to-end Machine Learning project including:
- data cleaning
- exploratory data analysis
- feature engineering
- preprocessing pipelines
- model training
- hyperparameter tuning
- evaluation metrics
- model saving
- XGBoost implementation

---

## Problem Statement

Customer churn is a major business problem in telecom companies because losing customers directly impacts revenue and growth.

The goal of this project is to predict customer churn early so businesses can improve retention strategies and reduce customer loss.

---

## Dataset

Dataset Used:
Telco Customer Churn Dataset

Source:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

---

## Features Used

### Customer Information
- gender
- SeniorCitizen
- Partner
- Dependents

### Service Information
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies

### Billing Information
- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges

### Target Variable
- Churn

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib

---

## Machine Learning Workflow

### 1. Data Cleaning
- Removed customerID column
- Converted TotalCharges to numeric
- Handled missing values

### 2. Exploratory Data Analysis
Performed:
- churn distribution analysis
- tenure analysis
- monthly charges visualization
- customer behavior analysis

### 3. Feature Engineering
Created custom features:
- AvgChargePerMonth
- LongTermCustomer

### 4. Data Preprocessing
Used:
- OneHotEncoding
- StandardScaler
- ColumnTransformer
- Pipeline preprocessing

### 5. Machine Learning Models
Implemented:
- Random Forest Classifier
- XGBoost Classifier

### 6. Hyperparameter Tuning
Used:
- GridSearchCV
- cross-validation

### 7. Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- Classification Report
- ROC Curve

---

## Project Results

The project successfully predicted customer churn using advanced machine learning techniques.

### Random Forest
- strong classification performance
- balanced handling of churn classes
- robust feature learning

### XGBoost
- improved prediction capability
- better optimization
- high ROC-AUC performance

The models identified important churn-driving factors such as:
- contract type
- monthly charges
- internet services
- tenure

---

## Feature Engineering

Custom features created:

### AvgChargePerMonth
Average customer spending behavior.

### LongTermCustomer
Identifies customers with long service duration.

---

## Hyperparameter Tuning

GridSearchCV was used for:
- optimal tree depth
- number of estimators
- learning rate optimization
- split condition optimization

This improved overall model performance.

---

## Model Saving

Trained models were saved using Joblib:
- churn_model.pkl
- xgboost_churn_model.pkl

This allows deployment without retraining.
