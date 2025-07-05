import streamlit as st
import numpy as np
import pandas as pd

def detect_outliers(df):
    st.subheader("⚠️ Outlier Detection (Z-score / IQR)")

    num_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()
    if not num_cols:
        st.info("Không có cột số để phân tích.")
        return df

    col = st.selectbox("Chọn cột để kiểm tra outlier", num_cols)
    method = st.radio("Chọn phương pháp", ["Z-score", "IQR"])

    if method == "Z-score":
        threshold = st.slider("Ngưỡng Z-score", 1.0, 5.0, 3.0)
        z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
        outliers = df[z_scores > threshold]
    else:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]

    st.write(f"Tìm thấy {len(outliers)} outliers trong cột {col}")
    st.dataframe(outliers)

    if st.checkbox("❌ Xoá các outlier khỏi dữ liệu"):
        df = df.drop(outliers.index)
        st.success(f"Đã xoá {len(outliers)} dòng bất thường.")

    return df
