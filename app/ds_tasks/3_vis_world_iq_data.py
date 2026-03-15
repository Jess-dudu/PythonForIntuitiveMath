from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Title
st.title("World IQ Data 2022")

st.markdown(
    "Data Source: [World Data 2022 collection](https://www.kaggle.com/datasets/moekhaledx/countries-of-the-world)"
)

# Column descriptions (brief)
st.write(
    """
    This Kaggle dataset contains the following key columns in the dataset (check original source for exact definitions):
    - `health_index`: Composite health index (higher is better).
    - `obese_rate`: Percentage of population classified as obese.
    - `suicide_rate`: Suicide rate (reported in dataset; check source for exact units).
    - `democracies_rate`: Democracy score/index (higher indicates more democratic).
    - `hdr_rate`: Human Development Index (HDI), typically 0–1 where higher is better.
    - `life_Exp`: Life expectancy (years).
    - `gpi`: Global Peace Index or similar peace-related score (higher may indicate less peaceful); verify with original source if needed.
    - `iq` / `iq_rate`: Average IQ score or IQ rate for the country.
    - `Deaths per 1,000 live births`: Infant mortality (deaths per 1,000 live births).
    - `gdp_usd`: GDP per capita (USD) or total GDP depending on source — commonly per-capita in similar datasets.
    """
)

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

df.drop("iq_rate", axis=1, inplace=True, errors="ignore")
df.drop("Ipc", axis=1, inplace=True, errors="ignore")
df.drop("region", axis=1, inplace=True, errors="ignore")

# Clean IQ values
df["iq"] = pd.to_numeric(df["iq"], errors="coerce")
df = df.dropna(subset=["iq"])

# Dataset overview
st.subheader("Dataset Overview")
# st.write(f"Shape: {df.shape}")
st.dataframe(df.head(3))

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
show_top10 = True  # st.checkbox("Show top 10 countries by IQ", value=True)
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

    # Correlation analysis
    st.subheader("Correlation between IQ and other numeric columns")

    # Identify numeric columns (exclude IQ itself)
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    numeric_cols = [c for c in numeric_cols if (c != "iq") and (c != "iq_rate")]

    if not numeric_cols:
        st.info("No other numeric columns found in the dataset to correlate with IQ.")
    else:
        cols_to_check = st.multiselect(
            "Select columns to compare with IQ (leave empty to auto-show top correlations)",
            options=numeric_cols,
            max_selections=1,
            default=[],
        )

        # If user left empty, compute correlations for all numeric columns and show top ones
        if not cols_to_check:
            corrs = []
            for c in numeric_cols:
                s = pd.to_numeric(df[c], errors="coerce")
                pair = df[["iq"]].join(s)
                pair = pair.dropna()
                if pair.shape[0] < 3:
                    corr = np.nan
                else:
                    corr = pair["iq"].corr(pair[c])
                corrs.append((c, corr))
            corr_df = pd.DataFrame(corrs, columns=["column", "pearson_corr"]).dropna()
            corr_df["abs_corr"] = corr_df["pearson_corr"].abs()
            corr_df = corr_df.sort_values("abs_corr", ascending=False)
            st.write("Top correlations with IQ (by absolute Pearson correlation):")
            st.dataframe(corr_df.reset_index(drop=True))

        else:
            # Show correlations for user-selected columns
            results = []
            for c in cols_to_check:
                s = pd.to_numeric(df[c], errors="coerce")
                pair = df[["iq"]].join(s)
                pair = pair.dropna()
                if pair.shape[0] < 3:
                    corr = np.nan
                else:
                    corr = pair["iq"].corr(pair[c])
                results.append((c, corr, pair.shape[0]))
            results_df = pd.DataFrame(
                results, columns=["column", "pearson_corr", "n_samples"]
            ).dropna()
            st.dataframe(
                results_df.sort_values("pearson_corr", ascending=False).reset_index(
                    drop=True
                )
            )

            # Scatter plots with regression lines for each selected column
            st.write("Scatter plots (IQ vs selected columns)")
            for c in cols_to_check:
                s = pd.to_numeric(df[c], errors="coerce")
                pair = df[["country", "iq"]].join(s)
                pair = pair.dropna()
                if pair.shape[0] < 3:
                    st.write(
                        f"Not enough data for column {c} to show scatter (need >=3 rows)"
                    )
                    continue

                x = pair[c].values
                y = pair["iq"].values
                # fit linear regression
                slope, intercept = np.polyfit(x, y, 1)
                line_x = np.linspace(x.min(), x.max(), 100)
                line_y = slope * line_x + intercept

                fig_scatter = go.Figure()
                fig_scatter.add_trace(
                    go.Scatter(
                        x=x,
                        y=y,
                        mode="markers",
                        name="data",
                        marker=dict(size=6),
                        text=pair["country"],
                    )
                )
                fig_scatter.add_trace(
                    go.Scatter(
                        x=line_x,
                        y=line_y,
                        mode="lines",
                        name=f"fit: y={slope:.2f}x+{intercept:.2f}",
                    )
                )
                fig_scatter.update_layout(
                    title=f"IQ vs {c}", xaxis_title=c, yaxis_title="IQ", height=450
                )
                st.plotly_chart(fig_scatter, use_container_width=True)

        # Correlation heatmap for numeric columns (including IQ)
        st.write("Correlation matrix (numeric columns)")
        corr_matrix = df.select_dtypes(include=[np.number]).corr()
        if corr_matrix.shape[0] >= 2:
            fig_heat = px.imshow(
                corr_matrix,
                text_auto=True,
                color_continuous_scale="RdBu",
                origin="lower",
                aspect="auto",
                title="Correlation matrix (numeric columns)",
            )
            fig_heat.update_layout(height=600)
            st.plotly_chart(fig_heat, use_container_width=True)
