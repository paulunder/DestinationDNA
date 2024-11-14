import streamlit as st


def page_conclusions_body():
    """
    This function generates the content for the Conclusions page.
    """
    st.write("### Project Conclusions")

    st.write(
        "The project was a succcess - it can predict wether a person is "
        "likely to make a vacation in the mountains or at the beach."
    )

    st.success(
        "#### Business Requirements\n\n"
        "Understanding the relationship between the destination and the "
        "customer persona "
        "At the Data Analysis stage, I found that the destination and the "
        "customer persona are related - plots and graphs were used. "
        "The Decision Tree model was able to predict the preference of a "
        "customer based on their persona. "

    )

    st.info(
        "#### Project Outcomes\n\n"
        "The project was able to predict the preference of a customer "
        "based on their persona.\n"
        "I found out that most features are not that important in "
        "predicting the preference of the customer\n"
    )
