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
st.set_page_config(page_title="Data Toolkit Suite", layout="wide")
st.title("🧰 Data Toolkit Suite – Công cụ xử lý & khám phá dữ liệu")

# Init state
if "df" not in st.session_state:
    st.session_state.df = None

# Nếu chưa có dữ liệu: hiển thị phần Hướng dẫn + Giới thiệu + Import
if st.session_state.df is None:
    st.markdown("## Hướng dẫn sử dụng")
    st.markdown("""
    **1. Tải file `.csv` từ máy bạn để bắt đầu phân tích**  
    **2. Sau khi tải lên, sidebar sẽ hiển thị các module xử lý**

    👉 Dữ liệu mẫu gợi ý: `iris.csv`, `titanic.csv`, `sales.csv`
    """)

    with st.expander("Giới thiệu dự án"):
        st.markdown("""
        - **🧰 Data Toolkit Suite** là công cụ web hỗ trợ làm sạch và khám phá dữ liệu cho người học ngành data
        - Dùng các thư viện: Streamlit, Pandas, Scikit-learn
        - Không cần viết code – chỉ cần tải dữ liệu và chọn module

        **Nguồn sở hữu:** [databinocs](https://github.com/databinocs)
        """)

    # Hiển thị upload file
    st.markdown("### 📤 Tải dữ liệu CSV")
    uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
        st.success("✅ Dữ liệu đã tải thành công!")
        st.dataframe(df, use_container_width=True)

# Nếu đã có dữ liệu: hiển thị sidebar + module xử lý
else:
    df = st.session_state.df

    # Sidebar chọn chức năng xử lý
    menu = st.sidebar.selectbox(
        "🔧 Chọn chức năng xử lý dữ liệu",
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

    # Giao diện theo chức năng
    if menu == "Cleaning":
        st.header("🧹 Làm sạch dữ liệu")
        clean_data(df)

    elif menu == "EDA Processing":
        st.header("📊 Phân tích tổng quan dữ liệu")
        show_eda(df)

    elif menu == "Visualization":
        st.header("📈 Tạo biểu đồ tương tác")
        visualize_data(df)

    elif menu == "Outlier Detection":
        st.header("🕵️ Phát hiện Outlier")
        detect_outliers(df)

    elif menu == "Anomaly Detection":
        st.header("⚠️ Phát hiện bất thường")
        anomaly_detection(df)

    elif menu == "Clustering":
        st.header("🧩 Gom cụm (Clustering)")
        clustering_app(df)

    elif menu == "Time Series":
        st.header("⏱ Phân tích chuỗi thời gian")
        time_series_app(df)

    elif menu == "Modeling":
        st.header("🤖 Huấn luyện mô hình dự đoán")
        run_model(df)

    # Hiển thị phần Export sau module xử lý
    st.markdown("---")
    st.subheader("📥 Tải xuống dữ liệu sau xử lý")
    download_data(df)






