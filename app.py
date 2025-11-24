import streamlit as st
import pickle
import numpy as np
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ydata_profiling import ProfileReport
import pandas as pd

df = pd.read_csv("credit_card_data.csv")
profile = ProfileReport(df, title="Credit Card Fraud Report", explorative=True)
profile.to_file("credit_card_fraud_report.html")


st.title("Credit Card Fraud Detection App")
st.write("Predict whether a transaction is Legitimate or Fraudulent using a Decision Tree model.")

# Load Model
model = pickle.load(open("decision_tree_entropy_model.pkl", "rb"))

# UI Inputs
amount = st.number_input("Transaction Amount", min_value=0.0)
time_sec = st.number_input("Transaction Time (seconds since midnight)", min_value=0.0, max_value=86400.0)
account_age = st.number_input("Account Age (days)", min_value=0.0)
merchant_risk = st.slider("Merchant Risk Score", 0.0, 1.0, 0.0)
velocity = st.number_input("Transaction Velocity (transactions/hour)", min_value=0.0)

# Prediction
if st.button("Predict"):
    features = np.array([[amount, time_sec, account_age, merchant_risk, velocity]])
    result = model.predict(features)[0]
    
    if result == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:

        st.success("✅ Legitimate Transaction")
