import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def page_eda_body():
    st.title("Exploratory Data Analysis")
    data = pd.read_csv("outputs/datasets/processed/balanced_mountains_vs_beaches_preferences.csv")
    
    st.write("Dataset Overview")
    st.write(data.head())
    
    st.write("Correlation Heatmap")
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    st.pyplot()
