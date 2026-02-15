import pandas as pd
import plotly.express as px
import streamlit as st

st.title("US Population Visualization")

# 1. Load and prepare your data
state_population = pd.read_csv("data/us_states/us_pop_by_state.csv")
# Drop any summary/total rows where state_code is not a 2-letter code
state_population = state_population[
    state_population["state_code"].str.len() == 2
].copy()

# 2. Two-column layout: data preview and controls
st.write("Data preview:")
col1, col2 = st.columns([2, 1])

with col1:
    st.dataframe(state_population.head(4), hide_index=True)

with col2:
    # Let the user choose which metric to visualize
    metric = st.selectbox(
        "Choose metric to visualize",
        options=["2020_census", "percent_of_total"],
        format_func=lambda x: (
            "Population (2020)" if x == "2020_census" else "Percent of total"
        ),
    )

    color_scale = st.selectbox(
        "Color scale",
        options=["Viridis", "Plasma", "Inferno", "Cividis", "Blues"],
        index=0,
    )

# 3. Create the choropleth figure using state 2-letter codes
fig = px.choropleth(
    state_population,
    locations="state_code",
    locationmode="USA-states",
    color=metric,
    scope="usa",
    color_continuous_scale=color_scale,
    hover_data=["state", "2020_census", "percent_of_total"],
    labels={"2020_census": "Population (2020)", "percent_of_total": "Share of U.S."},
)

# 4. Display in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Optional: show top/bottom states by the chosen metric
if st.checkbox("Show top 10 states by selected metric"):
    desc = state_population.sort_values(by=metric, ascending=False).head(10)
    st.bar_chart(desc.set_index("state")[metric])
