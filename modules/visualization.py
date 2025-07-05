import streamlit as st
import plotly.express as px
import pandas as pd

def visualize_data(df):
    st.subheader("📈 Data Visualization")

    numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()
    all_cols = df.columns.tolist()

    if len(numeric_cols) < 1:
        st.warning("Không có đủ cột số để vẽ biểu đồ.")
        return

    chart_type = st.selectbox("Chọn loại biểu đồ", ["Scatter", "Bar", "Line"])
    x_col = st.selectbox("Chọn cột X", all_cols)
    y_col = st.selectbox("Chọn cột Y", numeric_cols)

    if st.button("📊 Vẽ biểu đồ"):
        if chart_type == "Scatter":
            fig = px.scatter(df, x=x_col, y=y_col, title=f"{chart_type} Plot")
        elif chart_type == "Bar":
            fig = px.bar(df, x=x_col, y=y_col, title=f"{chart_type} Chart")
        elif chart_type == "Line":
            fig = px.line(df, x=x_col, y=y_col, title=f"{chart_type} Chart")
        st.plotly_chart(fig, use_container_width=True)
