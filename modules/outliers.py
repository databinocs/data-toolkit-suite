import streamlit as st
import numpy as np
import pandas as pd

def detect_outliers(df):
    st.subheader("⚠️ Outlier Detection (Z-score / IQR)")

    num_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()
    if not num_cols:
        st.info("No Numeric Columns Available.")
        return df

    col = st.selectbox("Select Column", num_cols)
    method = st.radio("Select Method", ["Z-score", "IQR"])

    if method == "Z-score":
        threshold = st.slider("Z-score Threshold", 1.0, 5.0, 3.0)
        z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
        outliers = df[z_scores > threshold]
    else:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]

    st.write(f"Found {len(outliers)} outliers in the Column {col}")
    st.dataframe(outliers)

    if st.checkbox("❌ Remove Outliers"):
        df = df.drop(outliers.index)
        st.success(f"{len(outliers)} Anomalous Rows Removed.")

    return df
