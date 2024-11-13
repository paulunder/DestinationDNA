import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style("whitegrid")


def page_hypotheses_body():

    st.write("### Project Hypotheses")

    st.write(
        "* [Hypothesis 1](#hypothesis-1)\n"
        "* [Hypothesis 2](#hypothesis-2)\n"
    )

    st.write("### Hypothesis 1")
    st.warning(
        "* We suspect that people which are living near beaches are more likely to prefer beach vacations."
    )
    st.success(
        " * According tio the data analysis, this hypothesis is true."
        " * People living near beaches are more likely to prefer beach vacations."
        " * People living near mountains are more likely to prefer mountain vacations."
    )

    st.write("---")

    st.write("### Hypothesis 2")
    st.warning(
        "* We suspect that the preferred activities have heavy influence on the destination choice."
    )
    st.success(
        " * That was also true. The preferred activities have a heavy influence on the destination choice."
    )

    st.write("---")
