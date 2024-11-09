import streamlit as st
import pandas as pd
import os
from src.data_management import load_pkl_file
from sklearn.pipeline import Pipeline

model_pipeline_path = os.path.join(os.path.dirname(__file__), "../outputs/pipeline/model.pkl")
model_pipeline = load_pkl_file(model_pipeline_path)

def page_predictor_body():
    st.title("Mountain vs. Beach Preference Predictor")
    st.write("Predict whether a user prefers mountains or beaches based on their characteristics.")
    
    input_data = get_user_input()

    if st.button("Predict Preference"):
        prediction = predict_preference(input_data, model_pipeline)
        display_result(prediction)

def get_user_input():
    # Mapping dictionaries for user-friendly display
    gender_mapping = {"male": 1, "female": 0, "non-binary": 2}
    education_level_mapping = {"high school": 0, "associate": 1, "bachelor": 2, "master": 3}
    preferred_activities_mapping = {"skiing": 1, "hiking": 2, "swimming": 3}
    location_mapping = {"urban": 0, "suburban": 1, "rural": 2}
    favorite_season_mapping = {"summer": 0, "fall": 1, "winter": 2, "spring": 3}
    pets_mapping = {"No": 0, "Yes": 1}
    environmental_concerns_mapping = {"No": 0, "Yes": 1}
    age_group_mapping = {"18-25": 0, "26-35": 1, "36-50": 2, "50+": 3}

    # Collect user input with descriptive labels
    gender = st.selectbox("Gender", list(gender_mapping.keys()))
    income = st.number_input("Income", min_value=10000, max_value=200000, step=5000)
    education_level = st.selectbox("Education Level", list(education_level_mapping.keys()))
    travel_frequency = st.slider("Travel Frequency per Year", 0, 12, 1)
    preferred_activities = st.selectbox("Preferred Activities", list(preferred_activities_mapping.keys()))
    vacation_budget = st.number_input("Vacation Budget", min_value=100, max_value=20000, step=100)
    location = st.selectbox("Location", list(location_mapping.keys()))
    proximity_to_mountains = st.number_input("Proximity to Mountains (km)", 0, 300, step=5)
    proximity_to_beaches = st.number_input("Proximity to Beaches (km)", 0, 300, step=5)
    favorite_season = st.selectbox("Favorite Season", list(favorite_season_mapping.keys()))
    pets = st.selectbox("Do you have Pets?", list(pets_mapping.keys()))
    environmental_concerns = st.selectbox("Environmental Concerns", list(environmental_concerns_mapping.keys()))
    age_group = st.selectbox("Age Group", list(age_group_mapping.keys()))

    # Convert user input to numerical format for the model
    input_data = pd.DataFrame([{
        "Gender": gender_mapping[gender],
        "Income": income,
        "Education_Level": education_level_mapping[education_level],
        "Travel_Frequency": travel_frequency,
        "Preferred_Activities": preferred_activities_mapping[preferred_activities],
        "Vacation_Budget": vacation_budget,
        "Location": location_mapping[location],
        "Proximity_to_Mountains": proximity_to_mountains,
        "Proximity_to_Beaches": proximity_to_beaches,
        "Favorite_Season": favorite_season_mapping[favorite_season],
        "Pets": pets_mapping[pets],
        "Environmental_Concerns": environmental_concerns_mapping[environmental_concerns],
        "AgeGroup": age_group_mapping[age_group]
    }])

    return input_data

def predict_preference(input_data, model_pipeline):
    if isinstance(model_pipeline, Pipeline):
        try:
            prediction = model_pipeline.predict(input_data)
            return prediction
        except Exception as e:
            st.error(f"Error making prediction: {e}")
            return None
    else:
        st.error("The model pipeline is not a valid sklearn pipeline.")
        return None

def display_result(prediction):
    if prediction is not None:
        preference = "Mountains" if prediction[0] == 1 else "Beach"
        st.markdown(f"<h2 style='font-size: 36px;'>The person is likely to make a vacation at the <b>{preference}</b></h2>", unsafe_allow_html=True)
    else:
        st.write("There was an error making the prediction.")