import streamlit as st
import pandas as pd


DATASET_DF = pd.read_csv(
    "outputs/datasets/raw/mountains_vs_beaches_preferences.csv").head(5)


def page_summary_body():
    """
    This function generates the content for the Summary page.
    """
    st.write(
        "* [Project Summary](#project-summary)\n"
        "* [Project Dataset](#project-dataset)\n"
        "* [Feature Terminology](#feature-terminology)\n"
        "* [Business Requirements](#business-requirements)"
    )

    st.write("### Project Summary")

    st.write(
        "Tourism offices and agencies are highly interested in "
        "understanding the preferences of their customers. This project "
        "aims to analyze the preferences "
        "of customers for mountains and beaches, and to predict the "
        "preferences of individual customers.\n\n"
    )

    st.info(
        "#### **Project Dataset**\n\n"
        "**Dataset**: A publically available dataset sourced from "
        "[Kaggle](https://www.kaggle.com/datasets/jahnavipaliwal/mountains-vs-beaches-preference)"
        "was used for this project.\n\n"
        "The dataset contains 14 attributes, with 'Preference' "
        "as the target. The dataset contains a total of 52445 rows.\n\n"
        "**Dataset Observations**: The dataset contains a "
        "total of 918 observations."
    )

    st.dataframe(DATASET_DF)

    st.info(
        "#### **Feature Terminology**\n\n"
        "* **Age** - Age of the individual (numerical).\n"
        "* **Gender** - Gender identity of the individual "
        "(categorical: male, female, non-binary).\n"
        "* **Income** - Annual income of the individual (numerical).\n"
        "* **Education_Level** - Highest level of education attained "
        "(categorical: high school, bachelor, master, doctorate).\n"
        "* **Travel_Frequency** - Number of vacations taken per "
        "year (numerical).\n"
        "* **Preferred_Activities** - Activities preferred during "
        "vacations (categorical: hiking, swimming, skiing, sunbathing).\n"
        "* **Vacation_Budget** - Budget allocated for vacations (numerical).\n"
        "* **Location** - Type of residence (categorical: urban, "
        "suburban, rural).\n"
        "* **Proximity_to_Mountains** - Distance from the nearest "
        "mountains (numerical, in miles).\n"
        "* **Proximity_to_Beaches** - Distance from the nearest "
        "beaches (numerical, in miles).\n"
        "* **Favorite_Season** - Preferred season for vacations "
        "(categorical: summer, winter, spring, fall).\n"
        "* **Pets** - Ownership of pets (binary: 0 = No, 1 = Yes).\n"
        "* **Environmental_Concerns** - Environmental concerns "
        "(binary: 0 = No, 1 = Yes).\n"
    )

    st.success(
        "#### **Business Requirements**\n\n"
        "**Business Requirement 1** - The customer wants to understand the "
        "relationship between the destination and the customer persona.\n\n"
        "**Business Requirement 2** - The customer wants to predict the "
        "probability of a customer booking a "
        "destination based on their persona."
    )
