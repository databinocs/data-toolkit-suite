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
            "Hướng dẫn sử dụng",
            "Giới thiệu dự án",
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
    elif menu == "ℹ️ Giới thiệu dự án":
        st.markdown("# ℹ️ Giới thiệu Data Toolkit Suite")
        st.markdown("""
        ### 🎯 Mục tiêu dự án
        - Hỗ trợ cộng đồng học dữ liệu (data learner) có thể làm việc với dữ liệu nhanh chóng
        - Tối giản thao tác – không cần code
        - Giao diện thân thiện, nhẹ, dễ dùng ngay cả khi mới bắt đầu học

        ### 🧱 Công nghệ sử dụng
        - **Python**
        - **Streamlit** – xây dựng giao diện web nhanh gọn
        - **Scikit-learn** – xử lý outlier, anomaly, modeling
        - **Plotly / Pandas / Matplotlib** – trực quan hóa và phân tích
        - **Deploy bằng Streamlit Cloud**

        ### 🧩 Các module chính
        - Cleaning, EDA, Visualization
        - Outlier / Anomaly Detection
        - Clustering, Time Series, Modeling, Export
        - Tài liệu hướng dẫn tích hợp ngay trong app

        ### 💡 Vì sao tôi tạo tool này?
        - Tôi từng là người mới học ngành và biết việc "clean & khám phá dữ liệu" là trở ngại ban đầu
        - Tool này là cách tôi chia sẻ kinh nghiệm & hỗ trợ cộng đồng
        - Đồng thời thể hiện kỹ năng fullstack mini-data app để làm nổi bật hồ sơ cá nhân

        ### 🚀 Hướng phát triển tiếp theo
        - Hỗ trợ nhiều file hoặc định dạng khác (Excel, JSON)
        - Lưu lịch sử thao tác người dùng
        - Cho phép phân tích đa biến, feature selection
        - Kết nối Google Sheets / API

        ---
        👨‍💻 **Người phát triển:** [databinocs](https://github.com/databinocs)  
        📧 Mọi góp ý: databinocs@gmail.com  
        ⭐ Đừng quên **star repo nếu thấy hữu ích** nhé!
        """)









