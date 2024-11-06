import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_churned_customer_study import page_destination_customer_study_body
from app_pages.page_prospect import page_prospect_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_churn import page_predict_prospect_body

app = MultiPage(app_name= "Destination DNA")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Exploratory Data Analysis", page_destination_customer_study_body)
app.add_page("Prospect Destination Preference", page_prospect_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Prospect Preference", page_predict_prospect_body)

app.run() # Run the  app