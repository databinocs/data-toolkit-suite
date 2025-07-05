import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def run_model(df):
    st.subheader("🧠 Machine Learning - Classification")

    all_cols = df.columns.tolist()
    numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()

    target_col = st.selectbox("🎯 Select Target Column", all_cols)
    feature_cols = st.multiselect("🔢 Select Feature Columns", numeric_cols)

    if not feature_cols or not target_col:
        st.info("⚠️ Please Select All Features and Target.")
        return

    test_size = st.slider("📎 Test Split Ratio", 0.1, 0.5, 0.2)

    if st.button("🚀 Train Model"):
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
            st.error(f"❌ Error During Model Training: {e}")
