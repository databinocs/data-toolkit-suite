import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

def clustering_app(df):
    st.subheader("📌 Clustering (KMeans)")

    numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()
    if len(numeric_cols) < 2:
        st.warning("Cần ít nhất 2 cột số để phân cụm.")
        return df

    col_x = st.selectbox("Chọn trục X", numeric_cols, index=0)
    col_y = st.selectbox("Chọn trục Y", numeric_cols, index=1)
    k = st.slider("Số lượng cụm (k)", 2, 10, 3)

    if st.button("📍 Chạy phân cụm"):
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        df['cluster'] = model.fit_predict(df[[col_x, col_y]])

        fig = px.scatter(df, x=col_x, y=col_y, color=df['cluster'].astype(str),
                         title=f"KMeans Clustering (k={k})",
                         labels={"color": "Cluster"})
        st.plotly_chart(fig, use_container_width=True)

        if st.checkbox("❌ Xoá cột 'cluster' sau khi xem"):
            df.drop(columns="cluster", inplace=True)

    return df
