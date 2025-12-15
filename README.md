🏍️ Bike Resale Price & Profit Prediction App

This project is an end-to-end Machine Learning application that predicts the resale price of a used bike and calculates the expected profit or loss based on the buying price.
The model is trained using XGBoost Regressor and deployed as an interactive Streamlit web application.

🚀 Live Demo

🔗 Streamlit App: (Add your Streamlit Cloud link here)

📌 Project Objectives

Predict the resale price of a used bike

Calculate profit or loss for buyers and sellers

Demonstrate a real-world business use case of Machine Learning

Build and deploy a complete ML pipeline

🧠 Machine Learning Details

Problem Type: Regression

Algorithm Used: XGBoost Regressor

Evaluation Metrics:

MAE ≈ ₹15,000

RMSE ≈ ₹48,000

R² Score ≈ 0.88

📊 Dataset Description

The dataset contains used bike listings with the following features:

🔹 Input Features

Brand – Manufacturer of the bike

Owner – Ownership count (First, Second, etc.)

Kilometers Driven – Total distance traveled

Age – Age of the bike in years

Power – Engine power (CC)

🔹 Target Variable

Price – Resale price of the bike

Duplicate records were removed to improve data quality, and high-cardinality features such as city names were excluded to prevent overfitting.

🛠️ Tech Stack

Python

Pandas & NumPy

Scikit-learn

XGBoost

Joblib

Streamlit

⚙️ How the System Works

User enters bike details through the web interface

Input data is preprocessed (encoding + scaling)

Trained XGBoost model predicts resale price

Profit or loss is calculated using buying price

Results are displayed instantly in the app

▶️ Run Locally
# Clone the repository
git clone https://github.com/your-username/bike-price-prediction.git

# Navigate to project folder
cd bike-price-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

⚠️ Disclaimer

This application is created for educational purposes only and should not be used as a financial or commercial decision-making tool.

📌 Future Improvements

Add brand-wise price trends

Improve UI with charts and visuals

Add confidence intervals for predictions

Integrate location-based pricing logic

👤 Author

Kartik Jadhav
🔗 GitHub: https://github.com/kartik0830

⭐ Acknowledgements

Kaggle Datasets

UCI Machine Learning Repository

Streamlit Community

XGBoost Documentation
