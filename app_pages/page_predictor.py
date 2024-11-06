import streamlit as st
import pickle
import numpy as np

# Load the model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

def page_predictor_body():
    st.title("Mountain vs. Beach Preference Predictor")

    # Input features
    age = st.slider("Age", 18, 100, 25)
    gender = st.selectbox("Gender", ["male", "female", "non-binary"])
    income = st.number_input("Income", 10000, 200000, step=5000)
    travel_frequency = st.slider("Travel Frequency per Year", 0, 12, 1)
    vacation_budget = st.number_input("Vacation Budget", 100, 20000, step=100)
    favorite_season = st.selectbox("Favorite Season", ["summer", "fall", "winter", "spring"])
    proximity_to_mountains = st.number_input("Proximity to Mountains (km)", 0, 300, step=5)
    proximity_to_beaches = st.number_input("Proximity to Beaches (km)", 0, 300, step=5)

    if st.button("Predict Preference"):
        input_features = np.array([[age, gender, income, travel_frequency, vacation_budget, 
                                    favorite_season, proximity_to_mountains, proximity_to_beaches]])
        prediction = model.predict(input_features)
        preference = "Beach" if prediction[0] == 1 else "Mountain"
        st.write(f"The model predicts: {preference}")
