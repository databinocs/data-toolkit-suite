import streamlit as st
import pandas as pd

def download_data(df):
    st.subheader("💾 Export Dữ Liệu")

    st.markdown("Bạn có thể tải dữ liệu đã xử lý về máy:")

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Tải CSV",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
