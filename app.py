import streamlit as st
import joblib
import numpy as np

# Load model files
pipeline =joblib.load ("model3.pkl")


st.set_page_config(page_title="Insurance Cost Predictor")

# Title
st.title("💰 Health Insurance Cost Prediction App")
st.write("Enter details to predict insurance charges")

# Inputs
age = st.slider("Age", 18, 100, 25)
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
children = st.slider("Children", 0, 5, 0)

sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northwest", "northeast", "southwest", "southeast"])

# Convert to model input
input_data = [age, bmi, children]

# One-hot encoding manually
for col in columns[3:]:
    if col == f"sex_{sex}":
        input_data.append(1)
    elif col == f"smoker_{smoker}":
        input_data.append(1)
    elif col == f"region_{region}":
        input_data.append(1)
    else:
        input_data.append(0)

# Prediction
if st.button("Predict"):
    input_array = np.array([input_data])
    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)

    st.success(f"Estimated Insurance Cost: ${prediction[0]:.2f}")
