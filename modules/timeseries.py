import streamlit as st
import pandas as pd
import plotly.express as px

def time_series_app(df):
    st.subheader("⏱ Time Series Explorer")

    all_cols = df.columns.tolist()
    numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()

    time_col = st.selectbox("🕒 Select Time Column", all_cols)
    value_col = st.selectbox("🔢 Select Numeric Value Column", numeric_cols)

    freq = st.radio("📅 Frequency", ["Day", "Month"])

    if st.button("📈 Plot Time Series Chart"):
        try:
            df[time_col] = pd.to_datetime(df[time_col])
        except Exception:
            st.error("❌ Unable to Convert Column to Time Format.")
            return

        df_sorted = df.sort_values(by=time_col)

        if freq == "Month":
            df_grouped = df_sorted.groupby(df_sorted[time_col].dt.to_period("M"))[value_col].mean()
            df_grouped.index = df_grouped.index.to_timestamp()
        else:
            df_grouped = df_sorted.groupby(df_sorted[time_col].dt.date)[value_col].mean()

        fig = px.line(df_grouped, title=f"Time Series - {value_col} theo {freq.lower()}")
        st.plotly_chart(fig, use_container_width=True)
