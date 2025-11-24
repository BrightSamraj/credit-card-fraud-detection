import streamlit as st
import pickle
import numpy as np
import pandas as pd
import pathlib

st.set_page_config(page_title="Credit Card Fraud Detection", page_icon="💳")

# ---------------------------------------------------------------------
# 👉 TITLE SECTION
# ---------------------------------------------------------------------
st.title("Credit Card Fraud Detection App")
st.write("Predict whether a transaction is Legitimate or Fraudulent using a Decision Tree model.")


# ---------------------------------------------------------------------
# 👉 SHOW HTML PROFILING REPORT (WITHOUT ydata-profiling)
# ---------------------------------------------------------------------
st.subheader("📊 Data Profiling Report")

report_path = pathlib.Path("credit_card_fraud_report.html")

if report_path.exists():
    with open(report_path, "r", encoding="utf-8") as f:
        html = f.read()
    st.components.v1.html(html, height=600, scrolling=True)
else:
    st.info("⚠️ Profiling report not found. Upload 'credit_card_fraud_report.html' to the project folder.")


# ---------------------------------------------------------------------
# 👉 LOAD MODEL (NO ProfileReport, NO ydata-profiling)
# ---------------------------------------------------------------------
try:
    model = pickle.load(open("decision_tree_entropy_model.pkl", "rb"))
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()


# ---------------------------------------------------------------------
# 👉 INPUT FIELDS
# ---------------------------------------------------------------------
st.subheader("🔧 Enter Transaction Details")

amount = st.number_input("Transaction Amount", min_value=0.0)
time_sec = st.number_input("Transaction Time (seconds since midnight)", min_value=0.0, max_value=86400.0)
account_age = st.number_input("Account Age (days)", min_value=0.0)
merchant_risk = st.slider("Merchant Risk Score", 0.0, 1.0, 0.0)
velocity = st.number_input("Transaction Velocity (transactions/hour)", min_value=0.0)


# ---------------------------------------------------------------------
# 👉 PREDICTION BUTTON
# ---------------------------------------------------------------------
if st.button("Predict"):
    features = np.array([[amount, time_sec, account_age, merchant_risk, velocity]])

    try:
        result = model.predict(features)[0]

        if result == 1:
            st.error("🚨 Fraudulent Transaction Detected!")
        else:
            st.success("✅ Legitimate Transaction")
    except Exception as e:
        st.error(f"❌ Prediction Error: {e}")


