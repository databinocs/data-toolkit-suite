import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def run_model(df):
    st.subheader("🧠 Machine Learning - Classification")

    all_cols = df.columns.tolist()
    numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()

    target_col = st.selectbox("🎯 Chọn cột target", all_cols)
    feature_cols = st.multiselect("🔢 Chọn các cột đặc trưng (features)", numeric_cols)

    if not feature_cols or not target_col:
        st.info("⚠️ Vui lòng chọn đầy đủ feature và target.")
        return

    test_size = st.slider("📎 Tỉ lệ test", 0.1, 0.5, 0.2)

    if st.button("🚀 Huấn luyện mô hình"):
        try:
            X = df[feature_cols]
            y = df[target_col]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            preds = model.predict(X_test)

            acc = accuracy_score(y_test, preds)
            st.success(f"🎯 Accuracy: {acc:.2%}")

            report = classification_report(y_test, preds, output_dict=True)
            st.dataframe(pd.DataFrame(report).transpose())

        except Exception as e:
            st.error(f"❌ Lỗi khi train mô hình: {e}")
