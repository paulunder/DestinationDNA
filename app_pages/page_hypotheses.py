import streamlit as st


def page_hypotheses_body():
    """
    This function generates the content for the Hypotheses page.
    """
    st.write("### Project Hypotheses")

    st.write(
        "* [Hypothesis 1](#hypothesis-1)\n"
        "* [Hypothesis 2](#hypothesis-2)\n"
    )

    st.write("### Hypothesis 1")
    st.warning(
        "* We suspect that people which are living "
        "near beaches are more likely to prefer beach vacations."
    )
    st.success(
        " * According to the data analysis, this hypothesis is true."
        " * People living near beaches are more likely to prefer "
        "beach vacations."
        " * People living near mountains are more likely to prefer "
        "mountain vacations."
    )

    st.write("---")

    st.write("### Hypothesis 2")
    st.warning(
        "* We suspect that the preferred activities have "
        "heavy influence on the destination choice."
    )
    st.success(
        " * That was also true. The preferred activities "
        "have a heavy influence on the destination choice."
    )

    st.write("---")

    st.write("### Hypothesis 3")
    st.warning(
        "* We suspect that environmental concerns have "
        "an influence on the correlation between proximity "
        "to the destination and the preference."
    )
    st.error(
        " * That was not true. The environmental "
        "concerns do not have a "
        "influence on the correlation between "
        "the proximity of the destination."
    )
