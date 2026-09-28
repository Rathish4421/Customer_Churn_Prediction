import streamlit as st
import joblib
import pandas as pd


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# LOAD MODEL AND SCALER
# =========================================================

model = joblib.load("Models/churn_model.pkl")
scaler = joblib.load("Models/Scaler.pkl")


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main application background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Main content width */
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ================= HEADER ================= */

    .main-header {
        background: linear-gradient(
            135deg,
            #0f172a,
            #1e3a8a
        );

        padding: 30px 35px;
        border-radius: 18px;
        margin-bottom: 25px;

        box-shadow:
            0 8px 25px rgba(15, 23, 42, 0.15);
    }

    .main-title {
        color: white;
        font-size: 36px;
        font-weight: 700;
        margin: 0;
    }

    .main-subtitle {
        color: #dbeafe;
        font-size: 17px;
        margin-top: 8px;
    }

    /* ================= SECTION TITLES ================= */

    .section-title {
        font-size: 23px;
        font-weight: 700;
        color: #0f172a;

        margin-top: 25px;
        margin-bottom: 8px;
    }

    .section-description {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 15px;
    }

    /* ================= INPUT LABELS ================= */

    .stNumberInput label,
    .stSelectbox label {
        color: #0f172a !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }

    /* ================= NUMBER INPUT ================= */

    .stNumberInput input {
        color: #0f172a !important;
        background-color: white !important;
    }

    /* ================= SELECT BOX ================= */

    .stSelectbox div[data-baseweb="select"] {
        background-color: white !important;
    }

    .stSelectbox div[data-baseweb="select"] span {
        color: #0f172a !important;
    }

    /* ================= BUTTON ================= */

    .stButton > button {
        background: linear-gradient(
            135deg,
            #2563eb,
            #1d4ed8
        );

        color: white !important;

        border: none;
        border-radius: 12px;

        padding: 12px 25px;

        font-size: 17px;
        font-weight: 700;

        box-shadow:
            0 5px 15px rgba(37, 99, 235, 0.25);
    }

    .stButton > button:hover {
        background: linear-gradient(
            135deg,
            #1d4ed8,
            #1e40af
        );
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="main-header">

    <div class="main-title">
            📊 Customer Churn Predictor
        </div>

    <div class="main-subtitle">
            Predict whether a customer is likely to churn
            using Machine Learning.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# INTRODUCTION
# =========================================================

st.info(
    "Enter the customer's details below and click "
    "Predict Churn to estimate the customer's "
    "churn probability."
)


# =========================================================
# CUSTOMER DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">📈 Customer Details</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    "Enter the customer's tenure and billing information."
    "</div>",
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


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
        value=50.0,
        step=1.0
    )


with col3:

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=600.0,
        step=10.0
    )


# =========================================================
# CUSTOMER INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">👤 Customer Information</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    "Provide basic customer and service information."
    "</div>",
    unsafe_allow_html=True
)


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


# =========================================================
# ADDITIONAL SERVICES
# =========================================================

st.markdown(
    '<div class="section-title">🌐 Additional Services</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    "Select the services currently used by the customer."
    "</div>",
    unsafe_allow_html=True
)


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


# =========================================================
# CONTRACT AND PAYMENT
# =========================================================

st.markdown(
    '<div class="section-title">📄 Contract & Payment</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    "Choose the customer's contract and payment method."
    "</div>",
    unsafe_allow_html=True
)


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


# =========================================================
# FEATURE ENCODING
# =========================================================

gender_value = 1 if gender == "Male" else 0

senior_citizen_value = (
    1 if senior_citizen == "Yes" else 0
)

partner_value = (
    1 if partner == "Yes" else 0
)

dependents_value = (
    1 if dependents == "Yes" else 0
)

phone_service_value = (
    1 if phone_service == "Yes" else 0
)

paperless_billing_value = (
    1 if paperless_billing == "Yes" else 0
)


# =========================================================
# MULTIPLE LINES
# =========================================================

multiple_lines_no_phone = (
    1 if multiple_lines == "No phone service" else 0
)

multiple_lines_yes = (
    1 if multiple_lines == "Yes" else 0
)


# =========================================================
# INTERNET SERVICE
# =========================================================

internet_service_fiber = (
    1 if internet_service == "Fiber optic" else 0
)

internet_service_no = (
    1 if internet_service == "No" else 0
)


# =========================================================
# ONLINE SECURITY
# =========================================================

online_security_no_internet = (
    1 if online_security == "No internet service" else 0
)

online_security_yes = (
    1 if online_security == "Yes" else 0
)


# =========================================================
# ONLINE BACKUP
# =========================================================

online_backup_no_internet = (
    1 if online_backup == "No internet service" else 0
)

online_backup_yes = (
    1 if online_backup == "Yes" else 0
)


# =========================================================
# DEVICE PROTECTION
# =========================================================

device_protection_no_internet = (
    1 if device_protection == "No internet service" else 0
)

device_protection_yes = (
    1 if device_protection == "Yes" else 0
)


# =========================================================
# TECH SUPPORT
# =========================================================

tech_support_no_internet = (
    1 if tech_support == "No internet service" else 0
)

tech_support_yes = (
    1 if tech_support == "Yes" else 0
)


# =========================================================
# STREAMING TV
# =========================================================

streaming_tv_no_internet = (
    1 if streaming_tv == "No internet service" else 0
)

streaming_tv_yes = (
    1 if streaming_tv == "Yes" else 0
)


# =========================================================
# STREAMING MOVIES
# =========================================================

streaming_movies_no_internet = (
    1 if streaming_movies == "No internet service" else 0
)

streaming_movies_yes = (
    1 if streaming_movies == "Yes" else 0
)


# =========================================================
# CONTRACT
# =========================================================

contract_one_year = (
    1 if contract == "One year" else 0
)

contract_two_year = (
    1 if contract == "Two year" else 0
)


# =========================================================
# PAYMENT METHOD
# =========================================================

payment_credit_card = (
    1 if payment_method == "Credit card (automatic)"
    else 0
)

payment_electronic_check = (
    1 if payment_method == "Electronic check"
    else 0
)

payment_mailed_check = (
    1 if payment_method == "Mailed check"
    else 0
)


# =========================================================
# CREATE INPUT DATAFRAME
# =========================================================

input_data = pd.DataFrame(
    [
        {
            "gender": gender_value,

            "SeniorCitizen": senior_citizen_value,

            "Partner": partner_value,

            "Dependents": dependents_value,

            "tenure": tenure,

            "PhoneService": phone_service_value,

            "PaperlessBilling": paperless_billing_value,

            "MonthlyCharges": monthly_charges,

            "TotalCharges": total_charges,

            "MultipleLines_No phone service":
                multiple_lines_no_phone,

            "MultipleLines_Yes":
                multiple_lines_yes,

            "InternetService_Fiber optic":
                internet_service_fiber,

            "InternetService_No":
                internet_service_no,

            "OnlineSecurity_No internet service":
                online_security_no_internet,

            "OnlineSecurity_Yes":
                online_security_yes,

            "OnlineBackup_No internet service":
                online_backup_no_internet,

            "OnlineBackup_Yes":
                online_backup_yes,

            "DeviceProtection_No internet service":
                device_protection_no_internet,

            "DeviceProtection_Yes":
                device_protection_yes,

            "TechSupport_No internet service":
                tech_support_no_internet,

            "TechSupport_Yes":
                tech_support_yes,

            "StreamingTV_No internet service":
                streaming_tv_no_internet,

            "StreamingTV_Yes":
                streaming_tv_yes,

            "StreamingMovies_No internet service":
                streaming_movies_no_internet,

            "StreamingMovies_Yes":
                streaming_movies_yes,

            "Contract_One year":
                contract_one_year,

            "Contract_Two year":
                contract_two_year,

            "PaymentMethod_Credit card (automatic)":
                payment_credit_card,

            "PaymentMethod_Electronic check":
                payment_electronic_check,

            "PaymentMethod_Mailed check":
                payment_mailed_check
        }
    ]
)


# =========================================================
# PREDICT BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

button_col1, button_col2, button_col3 = st.columns(
    [1, 2, 1]
)


with button_col2:

    predict_button = st.button(
        "🔮 Predict Churn",
        use_container_width=True
    )


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    # Scale input using the scaler
    input_scaled = scaler.transform(input_data)

    # Predict class
    prediction = model.predict(input_scaled)[0]

    # Get churn probability
    probability = model.predict_proba(
        input_scaled
    )[0][1]


    # =====================================================
    # PREDICTION RESULT
    # =====================================================

    st.markdown(
        '<div class="section-title">📊 Prediction Result</div>',
        unsafe_allow_html=True
    )


    if prediction == 1:

        st.error(
            "🔴 HIGH CHURN RISK\n\n"
            "This customer is likely to churn "
            "based on the provided information."
        )

    else:

        st.success(
            "🟢 LOW CHURN RISK\n\n"
            "This customer is likely to stay "
            "based on the provided information."
        )


    # =====================================================
    # CHURN PROBABILITY
    # =====================================================

    st.markdown("### 📈 Churn Probability")


    st.metric(
        label="Customer Churn Probability",
        value=f"{probability:.2%}"
    )


    st.progress(
        probability,
        text=f"Churn Probability: {probability:.2%}"
    )


    # =====================================================
    # RISK INTERPRETATION
    # =====================================================

    if probability >= 0.70:

        st.warning(
            "⚠️ High probability of churn. "
            "This customer may require "
            "retention attention."
        )

    elif probability >= 0.40:

        st.info(
            "ℹ️ Moderate churn probability. "
            "This customer may need "
            "additional monitoring."
        )

    else:

        st.success(
            "✅ Low churn probability. "
            "The customer is currently "
            "less likely to churn."
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div style="
        text-align: center;
        color: #64748b;
        font-size: 13px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #e2e8f0;
    ">

        Customer Churn Prediction • Machine Learning Project
        <br>
        Built with Python • Scikit-learn • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)