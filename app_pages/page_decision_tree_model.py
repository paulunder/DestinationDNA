import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def page_decision_tree_model_body():
    st.title("Decision Tree Model")

    # Sidebar parameters for model configuration
    max_depth = st.sidebar.slider("Max Depth", 1, 20, 5)
    min_samples_split = st.sidebar.slider("Min Samples Split", 2, 10, 2)

    df = pd.read_csv("outputs/datasets/processed/balanced_mountains_vs_beaches_preferences.csv")
    X = df.drop(columns=['Preference'])
    y = df['Preference']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # Train model and show results
    if st.button("Train Decision Tree Model"):
        model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split, random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate accuracy
        accuracy = accuracy_score(y_test, model.predict(X_test))
        st.write(f"Model Accuracy: {accuracy:.4f}")

        plt.figure(figsize=(10, 6))
        plot_tree(model, feature_names=X.columns, filled=True, class_names=['Beach', 'Mountain'])
        st.pyplot(plt.gcf())