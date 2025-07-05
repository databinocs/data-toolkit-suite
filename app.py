import streamlit as st
import pandas as pd

from modules.cleaning import clean_data
from modules.eda import show_eda
from modules.visualization import visualize_data
from modules.export import download_data
from modules.outliers import detect_outliers
from modules.anomaly import anomaly_detection
from modules.clustering import clustering_app
from modules.timeseries import time_series_app
from modules.modeling import run_model

st.title("🧰 Data Toolkit Suite")

uploaded_file = st.sidebar.file_uploader("📤 Tải file CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # ⬇️ Thêm menu chọn chức năng
    menu = st.sidebar.selectbox(
        "📂 Chọn chức năng",
        [
            "Cleaning",
            "EDA",
            "Visualization",
            "Outliers",
            "Anomaly Detection",
            "Clustering",
            "Time Series",
            "Modeling",
            "Export"
        ]
    )

    # ⬇️ Xử lý điều hướng theo menu
    if menu == "Cleaning":
        df = clean_data(df)
    elif menu == "EDA":
        show_eda(df)
    elif menu == "Visualization":
        visualize_data(df)
    elif menu == "Export":
        download_data(df)
    elif menu == "Outliers":
        df = detect_outliers(df)
    elif menu == "Anomaly Detection":
        df = anomaly_detection(df)
    elif menu == "Clustering":
        df = clustering_app(df)
    elif menu == "Time Series":
        time_series_app(df)
    elif menu == "Modeling":
        run_model(df)








