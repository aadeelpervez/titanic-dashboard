
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Titanic Dashboard",
    page_icon="🚢",
    layout="wide"
)

st.title("🚢 Titanic Data Analysis Dashboard")
st.write("Explore passenger information and survival patterns.")

file_path = Path(__file__).parent / "titanic.csv"
df = pd.read_csv(file_path)

col1, col2, col3 = st.columns(3)

col1.metric("Total Passengers", len(df))

if "Survived" in df.columns:
    survived = int((df["Survived"] == 1).sum())
    col2.metric("Survived", survived)
    col3.metric(
        "Survival Rate",
        f"{survived / len(df) * 100:.1f}%" if len(df) else "0%"
    )

st.subheader("Passenger Dataset")
st.dataframe(df, use_container_width=True)

if "Survived" in df.columns:
    st.subheader("Survival Analysis")
    survival_counts = (
        df["Survived"]
        .map({0: "Did Not Survive", 1: "Survived"})
        .value_counts()
        .reset_index()
    )
    survival_counts.columns = ["Status", "Passengers"]

    fig = px.bar(
        survival_counts,
        x="Status",
        y="Passengers",
        color="Status",
        title="Passenger Survival"
    )
    st.plotly_chart(fig, use_container_width=True)
