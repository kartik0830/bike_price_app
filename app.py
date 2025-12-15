import streamlit as st
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load("bike_price_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Bike Price & Profit Predictor", page_icon="🏍️")

st.title("🏍️ Bike Resale Price & Profit Prediction")
st.write("Enter bike details to predict resale price and profit")

st.warning("⚠️ This app is for educational purposes only.")

# -------- User Inputs --------
brand = st.selectbox(
    "Bike Brand",
    sorted([
        "Bajaj", "Royal Enfield", "Yamaha", "Honda",
        "Hero", "TVS", "KTM", "Suzuki", "Other"
    ])
)

owner = st.selectbox(
    "Owner Type",
    ["First Owner", "Second Owner", "Third Owner", "Fourth Owner"]
)

kms_driven = st.number_input("Kilometers Driven", 0, 300000, 20000)
age = st.number_input("Age of Bike (years)", 0, 30, 3)
power = st.number_input("Engine Power (CC)", 50, 2000, 350)

buying_price = st.number_input("Your Buying Price (₹)", 10000, 500000, 80000)

# -------- Prepare Input --------
input_df = pd.DataFrame({
    "kms_driven": [kms_driven],
    "age": [age],
    "power": [power],
    "brand": [brand],
    "owner": [owner]
})

# One-hot encode
input_df = pd.get_dummies(input_df)

# Align with training columns
model_features = model.get_booster().feature_names
for col in model_features:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[model_features]

# Scale numerical columns
num_cols = ["kms_driven", "age", "power"]
input_df[num_cols] = scaler.transform(input_df[num_cols])

# -------- Prediction --------
if st.button("Predict"):
    predicted_price = model.predict(input_df)[0]
    profit = predicted_price - buying_price

    st.success(f"💰 Predicted Resale Price: ₹{predicted_price:,.0f}")

    if profit >= 0:
        st.success(f"📈 Expected Profit: ₹{profit:,.0f}")
    else:
        st.error(f"📉 Expected Loss: ₹{abs(profit):,.0f}")
