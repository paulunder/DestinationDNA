# import streamlit as st
# import pandas as pd
# import numpy as np
# import os
# from src.data_management import load_pkl_file

# # Load model pipeline (includes pre-processing and model)
# model_pipeline_path = os.path.join(os.path.dirname(__file__), "../outputs/pipeline/model.pkl")
# model_pipeline11 = load_pkl_file(model_pipeline_path)

# model_pipeline = load_pkl_file(
#         f"outputs/pipeline/model.pkl"
#     )

# def page_predictor_body():
#     st.title("Mountain vs. Beach Preference Predictor")
#     st.write("Predict whether a user prefers mountains or beaches based on their characteristics.")

#     input_data = get_user_input()

#     if st.button("Predict Preference"):
#         prediction = make_prediction(input_data, model_pipeline)
#         display_result(prediction)

# def get_user_input():
#     input_data = pd.DataFrame(columns=[
#         "Age", "Gender", "Income", "Travel_Frequency", "Vacation_Budget",
#         "Favorite_Season", "Proximity_to_Mountains", "Proximity_to_Beaches"
#     ])

#     # Set up user input widgets
#     age = st.slider("Age", 18, 100, 25)
#     gender = st.selectbox("Gender", ["male", "female", "non-binary"])
#     income = st.number_input("Income", 10000, 200000, step=5000)
#     travel_frequency = st.slider("Travel Frequency per Year", 0, 12, 1)
#     vacation_budget = st.number_input("Vacation Budget", 100, 20000, step=100)
#     favorite_season = st.selectbox("Favorite Season", ["summer", "fall", "winter", "spring"])
#     proximity_to_mountains = st.number_input("Proximity to Mountains (km)", 0, 300, step=5)
#     proximity_to_beaches = st.number_input("Proximity to Beaches (km)", 0, 300, step=5)

#     input_data.loc[0] = [
#         age, gender, income, travel_frequency, vacation_budget,
#         favorite_season, proximity_to_mountains, proximity_to_beaches
#     ]
    
#     return input_data

# def make_prediction(input_data, model_pipeline):
#     """
#     Passes user input data through the pre-trained model pipeline for prediction.
#     """
#     prediction = model_pipeline.predict(input_data)
#     return prediction

# def display_result(prediction):
#     """
#     Display prediction result in the Streamlit app.
#     """
#     preference = "Beach" if prediction[0] == 1 else "Mountain"
#     st.write(f"The model predicts: **{preference}**")

import streamlit as st
import pandas as pd
import numpy as np
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
    input_data = pd.DataFrame(columns=[
        "Gender", "Income", "Education_Level", "Travel_Frequency", "Preferred_Activities", "Vacation_Budget", 
        "Location", "Proximity_to_Mountains", "Proximity_to_Beaches", "Favorite_Season", "Pets", 
        "Environmental_Concerns", "AgeGroup"
    ])

    # Create widgets for user input
    gender = st.selectbox("Gender", [1, 0, 2])
    income = st.number_input("Income", min_value=10000, max_value=200000, step=5000)
    education_level = st.selectbox("Education Level", [0, 1, 2, 3])
    travel_frequency = st.slider("Travel Frequency per Year", 0, 12, 1)
    preferred_activities = st.selectbox("Preferred Activities", [1, 2, 3]) 
    vacation_budget = st.number_input("Vacation Budget", min_value=100, max_value=20000, step=100)
    location = st.selectbox("Location", [0, 1, 2])  
    proximity_to_mountains = st.number_input("Proximity to Mountains (km)", 0, 300, step=5)
    proximity_to_beaches = st.number_input("Proximity to Beaches (km)", 0, 300, step=5)
    favorite_season = st.selectbox("Favorite Season", [0, 1, 2, 3])  
    pets = st.selectbox("Do you have Pets?", [0, 1])
    environmental_concerns = st.selectbox("Environmental Concerns", [0, 1])  
    age_group = st.selectbox("Age Group", [0, 1, 2, 3]) 

    input_data.loc[0] = [
        gender, income, education_level, travel_frequency, preferred_activities,
        vacation_budget, location, proximity_to_mountains, proximity_to_beaches,
        favorite_season, pets, environmental_concerns, age_group
    ]
    
    return input_data

def predict_preference(input_data, model_pipeline):
    """
    Custom function to make the prediction for user preference (Mountain or Beach)
    using the pre-trained model pipeline.
    """

    # Check if the model pipeline is a valid sklearn pipeline with a model
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
    """
    Display the prediction result (Mountain or Beach) in the Streamlit app.
    """
    if prediction is not None:
        # Interpret the prediction (assuming the model outputs 1 for Beach and 0 for Mountain)
        preference = "Beach" if prediction[0] == 1 else "Mountain"
        st.write(f"The model predicts: **{preference}**")
    else:
        st.write("There was an error making the prediction.")
