
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("xgboost_churn_model.pkl")

st.title("Customer Churn Prediction System")

tenure = st.slider("Tenure", 0, 72, 12)

monthly = st.number_input(
    "Monthly Charges",
    value=50.0
)

total = st.number_input(
    "Total Charges",
    value=500.0
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

input_df = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly],
    "TotalCharges": [total],
    "Contract": [contract]
})

if st.button("Predict"):
    st.write("Prediction running...")
