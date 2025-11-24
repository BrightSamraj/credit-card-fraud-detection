📌 Credit Card Fraud Detection – Streamlit App

A machine-learning powered real-time fraud detection web application built using Streamlit and a Decision Tree Classifier.
The app predicts whether a credit card transaction is Legitimate or Fraudulent based on key transaction attributes.

🚀 Project Overview

This project demonstrates an end-to-end pipeline:

Data Collection & Analysis
Using a credit-card transaction dataset and YData Profiling to explore fraud patterns.

Model Training
Two Decision Tree models were trained using:

Entropy (Information Gain)

Gini Impurity

Model Exporting
Both models were saved as .pkl files.

Frontend Development with Streamlit
The app provides a clean UI that takes transaction details and predicts fraud probability.

🎯 Features of the App

✔ Load trained ML models (.pkl)
✔ Input transaction details manually
✔ Instant prediction: Legitimate or Fraudulent
✔ Display prediction confidence
✔ View data profiling report inside the app (optional)
✔ Simple, fast, and deploy-ready UI

🧠 Machine Learning Models

Two trained models are included:

Model Name	Criterion	File
Decision Tree – Entropy	Information Gain	decision_tree_entropy_model.pkl
Decision Tree – Gini	Gini Impurity	decision_tree_gini_model.pkl

The default model used in the app is the Entropy version.

📁 Project Structure
credit-card-fraud-app/
│── app.py                            # Streamlit web application
│── decision_tree_entropy_model.pkl   # Trained model
│── decision_tree_gini_model.pkl      # Trained model
│── credit_card_data.csv              # Dataset (optional)
│── credit_card_fraud_report.html     # Profiling report (optional)
│── requirements.txt                  # Python dependencies
│── README.md                         # Project documentation

📦 Installation
1. Clone the repository
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection

2. Install dependencies
pip install -r requirements.txt

▶ Run the Streamlit App
streamlit run app.py


The app will open at:
👉 http://localhost:8501

🛠 How It Works

The model takes these five features:

Transaction Amount

Transaction Time (seconds since midnight)

Account Age (days)

Merchant Risk Score

Transaction Velocity (transactions/hour)

These inputs are passed into the Decision Tree model, which predicts:

0 → Legitimate Transaction

1 → Fraudulent Transaction

Probabilities are shown if available.

🌐 Deployment

You can easily deploy this project on:

Streamlit Cloud

Render

HuggingFace Spaces

Quick Deploy on Streamlit Cloud:

Push this project to GitHub

Go to https://share.streamlit.io

Select your repo

Choose app.py

Deploy 🎉