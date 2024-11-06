from app_pages.multipage import MultiPage

# load pages
from app_pages.page_summary import page_summary_body
from app_pages.page_eda import page_eda_body
from app_pages.page_hypotheses import page_hypotheses_body
from app_pages.page_predictor import page_predictor_body
from app_pages.page_decision_tree_model import page_decision_tree_model_body
from app_pages.page_conclusions import page_conclusions_body

# Initialize the app
app = MultiPage(app_name="Mountain vs Beach Preferences Classifier")

# Add pages to the app
app.add_page("Project Summary", page_summary_body)
app.add_page("Exploratory Data Analysis", page_eda_body)
app.add_page("Project Hypotheses", page_hypotheses_body)
app.add_page("Preference Predictor", page_predictor_body)
app.add_page("Decision Tree Model", page_decision_tree_model_body)
app.add_page("Project Conclusions", page_conclusions_body)

# Run the app
app.run()