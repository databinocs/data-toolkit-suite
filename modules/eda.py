import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show_eda(df):
    st.subheader("📊 Exploratory Data Analysis (EDA)")

    if st.checkbox("📋 Display Descriptive Statistics"):
        st.write(df.describe())

    if st.checkbox("📈 Plot Distribution Chart"):
        numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()
        if numeric_cols:
            col = st.selectbox("Select Numeric Column", numeric_cols)
            bins = st.slider("Number of Bins", 5, 100, 20)
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, bins=bins, ax=ax)
            st.pyplot(fig)
        else:
            st.info("No Numeric Columns.")

    if st.checkbox("🔗 Display Correlation Matrix"):
        numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()
        if len(numeric_cols) >= 2:
            fig, ax = plt.subplots(figsize=(10, 6))
            corr = df[numeric_cols].corr()
            sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
        else:
            st.info("At Least Two Numeric Columns Required.")
