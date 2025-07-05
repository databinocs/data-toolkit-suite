import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

def clustering_app(df):
    st.subheader("📌 Clustering (KMeans)")

    numeric_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()
    if len(numeric_cols) < 2:
        st.warning("At Least Two Numeric Columns Required.")
        return df

    col_x = st.selectbox("Select X-Axis", numeric_cols, index=0)
    col_y = st.selectbox("Select Y-Axis", numeric_cols, index=1)
    k = st.slider("Number of Clusters (k)", 2, 10, 3)

    if st.button("📍 Run Clustering"):
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        df['cluster'] = model.fit_predict(df[[col_x, col_y]])

        fig = px.scatter(df, x=col_x, y=col_y, color=df['cluster'].astype(str),
                         title=f"KMeans Clustering (k={k})",
                         labels={"color": "Cluster"})
        st.plotly_chart(fig, use_container_width=True)

        if st.checkbox("❌ Delete 'cluster' Column After Viewing"):
            df.drop(columns="cluster", inplace=True)

    return df
