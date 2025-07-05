import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

def anomaly_detection(df):
    st.subheader("🚨 Anomaly Detection (Isolation Forest)")

    numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()

    if len(numeric_cols) < 2:
        st.warning("Cần ít nhất 2 cột số để phát hiện bất thường.")
        return df

    cols = st.multiselect("Chọn cột số để phân tích", numeric_cols, default=numeric_cols[:2])
    contamination = st.slider("Tỷ lệ nghi ngờ bất thường (contamination)", 0.01, 0.2, 0.05)

    if st.button("🔍 Phát hiện bất thường"):
        model = IsolationForest(contamination=contamination, random_state=42)
        df['anomaly'] = model.fit_predict(df[cols])
        df['anomaly'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0)

        st.success(f"Đã phát hiện {df['anomaly'].sum()} điểm bất thường.")

        fig = px.scatter(df, x=cols[0], y=cols[1], color=df['anomaly'].astype(str),
                         title="Scatter Plot với Anomaly Highlight",
                         labels={"color": "Anomaly"})
        st.plotly_chart(fig, use_container_width=True)

        if st.checkbox("❌ Xoá dòng bất thường khỏi dữ liệu"):
            df = df[df['anomaly'] == 0].drop(columns='anomaly')
            st.success("Đã xoá dòng bất thường.")
        else:
            st.dataframe(df[df['anomaly'] == 1])

    return df
