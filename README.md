# Customer Churn Prediction

## Project Overview

This project predicts whether a customer is likely to churn or stay using Machine Learning.

The project includes data cleaning, exploratory data analysis, feature engineering, model training, model evaluation, hyperparameter tuning, and a Streamlit web application.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

## Machine Learning Models

- Logistic Regression
- Random Forest
- Gradient Boosting

## Best Model

The final model is a tuned Logistic Regression model with class balancing and feature scaling.

## Application

A Streamlit web application allows users to enter customer details and receive:

- Churn prediction
- Churn probability

## Project Workflow

Dataset
→ Data Cleaning
→ Exploratory Data Analysis
→ Feature Engineering
→ Train/Test Split
→ Model Training
→ Model Evaluation
→ Hyperparameter Tuning
→ Model Saving
→ Streamlit Deployment

## Model Performance

| Model | Accuracy | Churn Recall | Churn F1 | ROC-AUC |
|---|---:|---:|---:|---:|
| Balanced Logistic Regression | 73% | 80% | 61% | 83.50% |
| Random Forest | 77% | 65% | 60% | 82.01% |
| Gradient Boosting | 80% | 53% | 58% | 84.07% |

## Installation

Clone the repository:

```bash
git clone https://github.com/Rathish4421/Customer_Churn_Prediction.git