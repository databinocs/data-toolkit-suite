# 🧰 Data Toolkit Suite

A lightweight, web-based data cleaning & exploration toolkit for beginners and data learners – built with [Streamlit](https://streamlit.io/) 💻

👉 [Try now (Live Demo)](https://data-toolkit-suite.streamlit.app/)  
📦 [Source Code](https://github.com/databinocs/data-toolkit-suite)

---

## ✨ Main Functions

| Module                | Brief Description (lang: vi)                                  |
|----------------------|--------------------------------------------------|
| 📤 Upload CSV         | Tải lên tập dữ liệu định dạng `.csv`            |
| 🧹 Cleaning            | Xử lý missing values, encode categorical        |
| 📊 EDA                 | Tổng quan dữ liệu, phân phối, tương quan        |
| 📈 Visualization       | Biểu đồ scatter, bar, line                      |
| 🕵️ Outlier Detection   | Z-score & IQR filtering                        |
| ⚠️ Anomaly Detection   | Isolation Forest phát hiện bất thường          |
| 🧩 Clustering          | Gom cụm với KMeans (tùy chọn số cụm)            |
| ⏱ Time Series         | Biểu đồ chuỗi thời gian (ngày/tháng)           |
| 🤖 Modeling            | Train/test mô hình Random Forest               |
| 📥 Export              | Tải xuống dữ liệu sau khi xử lý                 |

---

## 🛠 How to run locally

```bash
git clone https://github.com/databinocs/data-toolkit-suite.git
cd data-toolkit-suite
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
streamlit run app.py
