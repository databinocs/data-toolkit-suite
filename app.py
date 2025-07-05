import streamlit as st
import pandas as pd

from modules.cleaning import clean_data
from modules.eda import show_eda
from modules.visualization import visualize_data
from modules.outliers import detect_outliers
from modules.anomaly import anomaly_detection
from modules.clustering import clustering_app
from modules.timeseries import time_series_app
from modules.modeling import run_model
from modules.export import download_data

# Page config
st.title("🧰 Data Toolkit Suite")
st.markdown("<small>Data Processing and Exploration Tool.</small>", unsafe_allow_html=True)

# Init state
if "df" not in st.session_state:
    st.session_state.df = None

# Sidebar layout
with st.sidebar:
    st.subheader("📤 Import CSV File")
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
        st.success("✅ Successful!")

    menu = st.selectbox(
        "📂 Select function:",
        [
            "Cleaning",
            "EDA Processing",
            "Visualization",
            "Outlier Detection",
            "Anomaly Detection",
            "Clustering",
            "Time Series",
            "Modeling"
        ]
    )

    st.markdown("---")
    st.subheader("💾 Export CSV File")

    if st.session_state.get("df") is not None:
        from modules.export import download_data
        download_data(st.session_state.df)
    else:
        st.info("⏳ Data Must Be Uploaded Before Export")

# Trang chính
if st.session_state.df is None:
    st.markdown("## User Guide")
    st.markdown("""
    **1. Upload a .csv file from your device to start analysis**  
    **2. After uploading, the sidebar will display processing modules**

    👉 Suggested sample data files: `iris.csv`, `titanic.csv`, `sales.csv`
    """)

    with st.expander("Introduction"):
        st.markdown("""
        **🧰 Data Toolkit Suite* is a web-based tool supporting data cleaning and exploration for data learners  
        - Uses libraries: Streamlit, Pandas, Scikit-learn  
        - No coding required – Runs directly in the browser  
        - Simply upload data and select a module  

        **Author**: [Nhat Thien An](https://databinocs.com/about/)  
        **Source**: [databinocs](https://github.com/databinocs/)
        """)
else:
    df = st.session_state.df

    if menu == "Cleaning":
        clean_data(df)
    elif menu == "EDA Processing":
        show_eda(df)
    elif menu == "Visualization":
        visualize_data(df)
    elif menu == "Outlier Detection":
        detect_outliers(df)
    elif menu == "Anomaly Detection":
        anomaly_detection(df)
    elif menu == "Clustering":
        clustering_app(df)
    elif menu == "Time Series":
        time_series_app(df)
    elif menu == "Modeling":
        run_model(df)





