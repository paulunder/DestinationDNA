import streamlit as st


def page_conclusions_body():

    st.write("### Project Conclusions")

    st.write(
        f"The project was a succcess - it can predict wether a person is likely to make a vacation in the mountains or at the beach."
    )
    
    st.success(
        f"#### Business Requirements\n\n"
        f"*Business Requirement 1* -Relationship between the destination and the customer persona\n"
        f"At the Data Analysis stage, we found that the destination and the customer persona are related - plots and graphs were used. "
        f"*Business Requirement 2* -Predict the probability of a customer booking a destination type based on their persona"
        f"The Decision Tree model was able to predict the preference of a customer based on their persona."

    )

    st.info(
        f"#### Project Outcomes\n\n"
        f"The project was able to predict the preference of a customer based on their persona\n"
        f"I found out that not most features are not that important in predicting the preference of a customer\n"
    )
