from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# Title
st.title("World IQ Data 2022")

st.markdown(
    "Data Source: [World Data 2022 collection](https://www.kaggle.com/datasets/moekhaledx/countries-of-the-world)"
)

st.write("""This Kaggle dataset contains various metrics (e.g., GDP, HDI, IQ, ...) 
         for countries around the world. Here is some basic visualization of the 
         dataset.
         """)

# Load data (robust relative path)
DATA_PATH = Path("data") / "world_data_2022" / "final.csv"
if not DATA_PATH.exists():
    st.error(f"Data file not found at {DATA_PATH}")
    st.stop()

df = pd.read_csv(DATA_PATH)

# Identify IQ column: prefer 'iq_rate' then 'iq'
if "iq_rate" in df.columns:
    df["iq"] = df["iq_rate"]
elif "iq" not in df.columns:
    st.error("Could not find an IQ column (expected 'iq_rate' or 'iq')")
    st.stop()

# Clean IQ values
df["iq"] = pd.to_numeric(df["iq"], errors="coerce")
df = df.dropna(subset=["iq"])

# Dataset overview
st.subheader("Dataset Overview")
# st.write(f"Shape: {df.shape}")
st.dataframe(df.head())

plot_df = df

# Choropleth map
fig_map = px.choropleth(
    plot_df,
    locations="country",
    locationmode="country names",
    color="iq",
    hover_name="country",
    hover_data={"iq": ":.2f", "country": False},
    color_continuous_scale="Viridis",
    title="World IQ Data 2022",
)
fig_map.update_layout(
    geo=dict(showland=True, landcolor="rgb(243, 243, 243)"), height=500
)
st.plotly_chart(fig_map, use_container_width=True)

# Optional: show top 10 countries by IQ
show_top10 = st.checkbox("Show top 10 countries by IQ", value=True)
if show_top10:
    top10 = plot_df.sort_values(by="iq", ascending=False).head(10)
    fig_top10 = px.bar(
        top10,
        x="iq",
        y="country",
        orientation="h",
        title="Top 10 countries by IQ",
        color="iq",
        color_continuous_scale="Viridis",
        category_orders={"country": top10["country"].tolist()},
    )
    fig_top10.update_layout(
        height=500, yaxis={"categoryorder": "array", "automargin": True}
    )
    st.plotly_chart(fig_top10, use_container_width=True)
