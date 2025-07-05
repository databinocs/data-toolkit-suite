import streamlit as st
import pandas as pd

def download_data(df):

    st.markdown("You Can Download the Processed Data to Your Device:")

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV File",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
