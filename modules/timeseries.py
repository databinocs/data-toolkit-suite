import streamlit as st
import pandas as pd
import plotly.express as px

def time_series_app(df):
    st.subheader("⏱ Time Series Explorer")

    all_cols = df.columns.tolist()
    numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()

    time_col = st.selectbox("🕒 Chọn cột thời gian", all_cols)
    value_col = st.selectbox("🔢 Chọn cột giá trị số", numeric_cols)

    freq = st.radio("📅 Tần suất", ["Ngày", "Tháng"])

    if st.button("📈 Vẽ biểu đồ thời gian"):
        try:
            df[time_col] = pd.to_datetime(df[time_col])
        except Exception:
            st.error("❌ Không thể chuyển cột thành dạng thời gian.")
            return

        df_sorted = df.sort_values(by=time_col)

        if freq == "Tháng":
            df_grouped = df_sorted.groupby(df_sorted[time_col].dt.to_period("M"))[value_col].mean()
            df_grouped.index = df_grouped.index.to_timestamp()
        else:
            df_grouped = df_sorted.groupby(df_sorted[time_col].dt.date)[value_col].mean()

        fig = px.line(df_grouped, title=f"Time Series - {value_col} theo {freq.lower()}")
        st.plotly_chart(fig, use_container_width=True)
