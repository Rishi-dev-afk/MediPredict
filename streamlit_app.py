import streamlit as st
import requests

st.title("Heart Disease Prediction")

# Input fields
Age = st.number_input("Age", min_value=0, max_value=120)
Sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
ChestPainType = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
RestingBP = st.number_input("Resting Blood Pressure")
Cholesterol = st.number_input("Cholesterol")
FastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
RestingECG = st.selectbox("Resting ECG", [0, 1, 2])
MaxHR = st.number_input("Max Heart Rate")
ExerciseAngina = st.selectbox("Exercise Angina", [0, 1])
Oldpeak = st.number_input("Oldpeak (ST depression)")
ST_Slope = st.selectbox("ST Slope", [0, 1, 2])

if st.button("Predict"):
    input_data = {
        "Age": Age,
        "Sex": Sex,
        "ChestPainType": ChestPainType,
        "RestingBP": RestingBP,
        "Cholesterol": Cholesterol,
        "FastingBS": FastingBS,
        "RestingECG": RestingECG,
        "MaxHR": MaxHR,
        "ExerciseAngina": ExerciseAngina,
        "Oldpeak": Oldpeak,
        "ST_Slope": ST_Slope
    }

    response = requests.post("http://localhost:5000/predict", json=input_data)

    if response.status_code == 200:
        result = response.json()['prediction']
        st.success("💔 Heart Disease Detected" if result == 1 else "❤️ No Heart Disease Detected")
    else:
        st.error(f"Error: {response.json().get('error', 'Unknown error')}")
