import streamlit as st
import pandas as pd


DATASET_DF = pd.read_csv(
    f"outputs/datasets/raw/mountains_vs_beaches_preferences.csv").head(5)


def page_project_summary_body():

    st.write(
        f"* [Project Summary](#project-summary)\n"
        f"* [Project Dataset](#project-dataset)\n"
        f"* [Feature Terminology](#feature-terminology)\n"
        f"* [Business Requirements](#business-requirements)"
    )

    st.write("### Project Summary")

    st.write(
        f"Tourism offices and agencies are highly interested in understanding the preferences of their customers. This project aims to analyze the preferences of customers for mountains and beaches, and to predict the preferences of individual customers.\n\n"
    )

    st.info(
        f"#### **Project Dataset**\n\n"
        f"**Dataset**: A publically available dataset sourced from [Kaggle](https://www.kaggle.com/datasets/jahnavipaliwal/mountains-vs-beaches-preference) was used for this project.\n\n"
        f"The dataset contains 14 attributes, with 'Preference' as the target. The dataset contains a total of 52445 rows.\n\n"        f"**Dataset Observations**: The dataset contains a total of 918 observations."
    )

    st.dataframe(DATASET_DF)

    st.info(
        f"#### **Feature Terminology**\n\n"
        f"* **Age** - Age of the individual (numerical).\n"
        f"* **Gender** - Gender identity of the individual (categorical: male, female, non-binary).\n"
        f"* **Income** - Annual income of the individual (numerical).\n"
        f"* **Education_Level** - Highest level of education attained (categorical: high school, bachelor, master, doctorate).\n"
        f"* **Travel_Frequency** - Number of vacations taken per year (numerical).\n"
        f"* **Preferred_Activities** - Activities preferred during vacations (categorical: hiking, swimming, skiing, sunbathing).\n"
        f"* **Vacation_Budget** - Budget allocated for vacations (numerical).\n"
        f"* **Location** - Type of residence (categorical: urban, suburban, rural).\n"
        f"* **Proximity_to_Mountains** - Distance from the nearest mountains (numerical, in miles).\n"
        f"* **Proximity_to_Beaches** - Distance from the nearest beaches (numerical, in miles).\n"
        f"* **Favorite_Season** - Preferred season for vacations (categorical: summer, winter, spring, fall).\n"
        f"* **Pets** - Ownership of pets (binary: 0 = No, 1 = Yes).\n"
        f"* **Environmental_Concerns** - Environmental concerns (binary: 0 = No, 1 = Yes).\n"
    )

    st.success(
        f"#### **Business Requirements**\n\n"
        f"**Business Requirement 1** - The customer wants to understand the relationship between the destination and the customer persona.\n\n"
        f"**Business Requirement 2** - The customer wants to predict the probability of a customer booking a destination based on their persona."
    )


