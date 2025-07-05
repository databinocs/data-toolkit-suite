import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def clean_data(df):
    st.subheader("🧹 Data Cleaning")

    if df.isnull().sum().sum() > 0:
        st.markdown("### ❗ Missing Values Detected")
        st.write(df.isnull().sum())

        col_to_fix = st.selectbox("Chọn cột để xử lý missing", df.columns[df.isnull().any()])
        method = st.radio("Phương pháp xử lý", ["Mean", "Median", "Mode", "Drop rows with missing"])

        if st.button("Áp dụng xử lý missing"):
            if method == "Mean":
                df[col_to_fix].fillna(df[col_to_fix].mean(), inplace=True)
            elif method == "Median":
                df[col_to_fix].fillna(df[col_to_fix].median(), inplace=True)
            elif method == "Mode":
                df[col_to_fix].fillna(df[col_to_fix].mode()[0], inplace=True)
            else:
                df.dropna(subset=[col_to_fix], inplace=True)
            st.success("Đã xử lý missing value cho cột: " + col_to_fix)

    if st.checkbox("🧹 Xoá các dòng trùng lặp"):
        before = df.shape[0]
        df.drop_duplicates(inplace=True)
        after = df.shape[0]
        st.success(f"Đã xoá {before - after} dòng trùng lặp.")

    if st.checkbox("🔤 Mã hoá các cột dạng text (Label Encoding)"):
        text_cols = df.select_dtypes(include='object').columns.tolist()
        if len(text_cols) == 0:
            st.info("Không có cột dạng text để mã hoá.")
        else:
            cols_to_encode = st.multiselect("Chọn cột để mã hoá", text_cols)
            le = LabelEncoder()
            for col in cols_to_encode:
                df[col] = le.fit_transform(df[col].astype(str))
            st.success("Đã mã hoá thành công.")

    return df
