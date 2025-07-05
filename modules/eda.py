import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show_eda(df):
    st.subheader("📊 Exploratory Data Analysis (EDA)")

    if st.checkbox("📋 Hiển thị thống kê mô tả"):
        st.write(df.describe())

    if st.checkbox("📈 Vẽ biểu đồ phân phối"):
        numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()
        if numeric_cols:
            col = st.selectbox("Chọn cột số để hiển thị histogram", numeric_cols)
            bins = st.slider("Số lượng bins", 5, 100, 20)
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, bins=bins, ax=ax)
            st.pyplot(fig)
        else:
            st.info("Không có cột số trong dữ liệu.")

    if st.checkbox("🔗 Hiển thị ma trận tương quan"):
        numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()
        if len(numeric_cols) >= 2:
            fig, ax = plt.subplots(figsize=(10, 6))
            corr = df[numeric_cols].corr()
            sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
        else:
            st.info("Cần ít nhất 2 cột số để tính tương quan.")
