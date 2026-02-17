import pandas as pd
import plotly.express as px
import streamlit as st
import us


def load_crime_dataframe(csv_name: str) -> pd.DataFrame:
    """Load crime data from a CSV file."""
    df = pd.read_csv(csv_name)

    # Ensure Year is integer on the working copy
    df.loc[:, "Year"] = df["Year"].astype(int)

    # state_code: USPS two-letter codes (used by Plotly's USA-states locationmode)
    STATE_TO_USPS = us.states.mapping("name", "abbr", states=us.STATES + [us.states.DC])
    df = df.assign(state_code=df["State"].map(STATE_TO_USPS))

    missing_codes = df.loc[df["state_code"].isna(), "State"].unique()
    if len(missing_codes) > 1:
        # 'United States' should be missing, warn if more missing
        print(f"Warning: some states will be skipped: {missing_codes}")
    df = df.dropna(subset=["state_code"])

    return df


# App UI
st.title("US Crime Rate Explorer")

st.markdown(
    "Data Source: [CORGIS Dataset Project - State Crime Data](https://corgis-edu.github.io/corgis/csv/state_crime/)"
)

state_crime = load_crime_dataframe("data/us_states/state_crime.csv")

st.markdown(
    "This csv file contains crime data from 1960 to 2019 of all US states. Select a year and crime metric to visualize the crime rates across US states."
)

metric_candidates = []  # always offer population as a metric
if "Crime_Rate" in state_crime.columns:
    metric_candidates.append("Crime_Rate")

metric_candidates += [
    c for c in state_crime.columns if (c.startswith("Data.Rates.") and "All" in c)
]
metric_candidates.append("Data.Population")

avail_years = sorted(state_crime["Year"].unique())
min_year, max_year = int(min(avail_years)), int(max(avail_years))

# color_scale = st.selectbox(
#         "Color scale",
#         options=["YlOrRd", "Viridis", "Plasma", "Cividis", "Blues"],
#         index=0,
#     )

col1, col2 = st.columns([1, 2])

# Select the data to be visualized
with col1:
    selected_year = st.slider(
        "Year to visualize",
        min_value=min_year,
        max_value=max_year,
        value=max_year,
        step=1,
    )

    color_metric = st.selectbox("Metric to color", options=metric_candidates, index=0)
    color_scale = "YlOrRd"

with col2:
    st.write("Data preview:")
    st.dataframe(state_crime.head(3))

# Filter for selected year and coerce metric to numeric
yr_df = state_crime[state_crime["Year"] == int(selected_year)].copy()
yr_df.loc[:, color_metric] = pd.to_numeric(yr_df[color_metric], errors="coerce")

# Choropleth
fig = px.choropleth(
    yr_df,
    locations="state_code",
    locationmode="USA-states",
    color=color_metric,
    scope="usa",
    color_continuous_scale=color_scale,
    hover_name="State",
    labels={color_metric: color_metric},
    title=f"US Crime: {color_metric} - {selected_year}",
)
st.plotly_chart(fig, width="stretch")

# Top-10 bar chart using st.bar_chart (DataFrame indexed by State)
show_top10 = st.checkbox("Show top 10 states")

if show_top10:
    top10 = (
        yr_df.loc[yr_df[color_metric].notna()]
        .sort_values(by=color_metric, ascending=False)
        .head(10)
    )
    if top10.empty:
        st.write("No numeric data available for the selected metric/year.")
    else:
        bar_df = top10.set_index("State")[[color_metric]].astype(float)
        bar_df = bar_df.rename(columns={color_metric: "value"})
        # enforce display order
        ordered_states = bar_df.index.tolist()
        bar_df.index = pd.CategoricalIndex(
            bar_df.index, categories=ordered_states, ordered=True
        )
        st.bar_chart(bar_df)
