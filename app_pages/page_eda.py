import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def page_eda_body():
    data_raw = pd.read_csv("outputs/datasets/raw/mountains_vs_beaches_preferences.csv")
    data_processed = pd.read_csv("outputs/datasets/processed/balanced_mountains_vs_beaches_preferences.csv")
    
    st.title("Exploratory Data Analysis")
    st.write("This page provides basic exploratory data analysis on your dataset.")

    st.subheader("Raw Data")
    st.write("Preview of the dataset:")
    st.dataframe(data_raw.head())

    st.subheader("Summary Statistics")
    st.write("A quick look at numerical summaries of the dataset:")
    st.write(data_raw.describe())

    st.subheader("Categorical Feature Distributions")
    categorical_cols = data_raw.select_dtypes(include=['object', 'category']).columns
    for col in categorical_cols:
        st.write(f"Distribution of **{col}**")
        st.bar_chart(data_raw[col].value_counts())
    
    st.subheader("Target Variable Distribution")
    st.write("Distribution of the target variable:")
    st.bar_chart(data_raw['Preference'].value_counts())

    st.subheader("Correlation Heatmap")
    st.write("Correlation between numerical features:")
    plt.figure(figsize=(10, 6))
    sns.heatmap(data_processed.corr(numeric_only=True), annot=True, cmap="coolwarm")
    st.pyplot(plt.gcf())

    st.subheader("Pair Plot")
    numeric_cols = data_raw.select_dtypes(include=['float64', 'int']).columns
    st.write("Pairwise relationships between selected numerical features:")
    sns.pairplot(data_raw[numeric_cols])
    st.pyplot(plt.gcf())

