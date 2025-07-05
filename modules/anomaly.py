import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

def anomaly_detection(df):
    st.subheader("🚨 Anomaly Detection (Isolation Forest)")

    numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()

    if len(numeric_cols) < 2:
        st.warning("At Least Two Numeric Columns Required.")
        return df

    cols = st.multiselect("Select Numeric Columns", numeric_cols, default=numeric_cols[:2])
    contamination = st.slider("Contamination Ratio (Anomaly Proportion)", 0.01, 0.2, 0.05)

    if st.button("🔍 Perform Anomaly Detection"):
        model = IsolationForest(contamination=contamination, random_state=42)
        df['anomaly'] = model.fit_predict(df[cols])
        df['anomaly'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0)

        st.success(f"{df['anomaly'].sum()} Anomalies Detected.")

        fig = px.scatter(df, x=cols[0], y=cols[1], color=df['anomaly'].astype(str),
                         title="Scatter Plot with Anomaly Highlight",
                         labels={"color": "Anomaly"})
        st.plotly_chart(fig, use_container_width=True)

        if st.checkbox("❌ Remove Anomalous Rows"):
            df = df[df['anomaly'] == 0].drop(columns='anomaly')
            st.success("Anomalous Rows Removed.")
        else:
            st.dataframe(df[df['anomaly'] == 1])

    return df
