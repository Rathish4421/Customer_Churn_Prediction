import streamlit as st
import joblib

model = joblib.load("Models/churn_model.pkl")
scaler = joblib.load("Models/scaler.pkl")

st.title("Customer Churn Prediction")
st.write("Predict whether a customer is likely to churn.")

st.subheader("Customer Details")
col1,col2,col3 = st.columns(3)

with col1:
    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )
    
with col2:
    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=50.0
    )

with col3:
    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=600.0
    )

st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

with col2:
    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

st.subheader("Additional Services")

col1, col2 = st.columns(2)

with col1:
    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

with col2:
    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )

st.subheader("Contract & Payment")

col1, col2 = st.columns(2)

with col1:
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

with col2:
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )

gender_value = 1 if gender == "Male" else 0
senior_citizen_value= 1 if senior_citizen == "Yes" else 0
partner_value=1 if partner == "Yes" else 0
dependents_value =1 if dependents == "Yes" else 0
phone_service_value =1 if phone_service == "Yes" else 0
paperless_billing_value =1 if paperless_billing == "Yes" else 0

multiple_lines_no_phone= 1 if multiple_lines == "No_phone_Service" else 0
multiple_lines_yes =1 if multiple_lines == "Yes" else 0

internet_service_fiber =1 if internet_service == "Fiber Optic" else 0
internet_service_no =1 if internet_service == "No" else 0

online_security_no_internet= 1 if online_security == "No internet service" else 0
online_security_yes=1 if online_security == "Yes" else 0

online_backup_no_internet=1 if online_backup == "No internet service" else 0
online_backup_yes=1 if online_backup == "Yes" else 0

device_protection_no_internet=1 if device_protection == "No internet service" else 0
device_protection_yes=1 if device_protection == "Yes" else 0

tech_support_no_internet = 1 if tech_support == "No internet service" else 0
tech_support_yes = 1 if tech_support == "Yes" else 0

streaming_tv_no_internet = 1 if streaming_tv == "No internet service" else 0
streaming_tv_yes = 1 if streaming_tv == "Yes" else 0

streaming_movies_no_internet = 1 if streaming_movies == "No internet service" else 0
streaming_movies_yes = 1 if streaming_movies == "Yes" else 0

contract_one_year = 1 if contract == "One year" else 0
contract_two_year = 1 if contract == "Two year" else 0

payment_credit_card = 1 if payment_method == "Credit card (automatic)" else 0
payment_electronic_check = 1 if payment_method == "Electronic check" else 0
payment_mailed_check = 1 if payment_method == "Mailed check" else 0

import pandas as pd

input_data = pd.DataFrame([{
    "gender": gender_value,
    "SeniorCitizen": senior_citizen_value,
    "Partner": partner_value,
    "Dependents": dependents_value,
    "tenure": tenure,
    "PhoneService": phone_service_value,
    "PaperlessBilling": paperless_billing_value,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,

    "MultipleLines_No phone service": multiple_lines_no_phone,
    "MultipleLines_Yes": multiple_lines_yes,

    "InternetService_Fiber optic": internet_service_fiber,
    "InternetService_No": internet_service_no,

    "OnlineSecurity_No internet service": online_security_no_internet,
    "OnlineSecurity_Yes": online_security_yes,

    "OnlineBackup_No internet service": online_backup_no_internet,
    "OnlineBackup_Yes": online_backup_yes,

    "DeviceProtection_No internet service": device_protection_no_internet,
    "DeviceProtection_Yes": device_protection_yes,

    "TechSupport_No internet service": tech_support_no_internet,
    "TechSupport_Yes": tech_support_yes,

    "StreamingTV_No internet service": streaming_tv_no_internet,
    "StreamingTV_Yes": streaming_tv_yes,

    "StreamingMovies_No internet service": streaming_movies_no_internet,
    "StreamingMovies_Yes": streaming_movies_yes,

    "Contract_One year": contract_one_year,
    "Contract_Two year": contract_two_year,

    "PaymentMethod_Credit card (automatic)": payment_credit_card,
    "PaymentMethod_Electronic check": payment_electronic_check,
    "PaymentMethod_Mailed check": payment_mailed_check
}])

st.write(input_data)

input_scaled = scaler.transform(input_data)

if st.button("Predict Churn"):

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0][1]
    
    st.subheader("Prediction Result")
    
    if prediction == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is likely to stay.")
        
    st.write(f"Churn Probablility: {probability:.2%}")
    st.progress(probability)
    
