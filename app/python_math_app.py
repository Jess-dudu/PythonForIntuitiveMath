import streamlit as st

# --- PAGE SETUP ---

home_page = st.Page(
    page="topics/home.py",
    title="About This App",
    icon=":material/home:",
    default=True,
)

topic1_hyperbolic = st.Page(
    page="topics/1_hyperbolic_functions.py",
    title="Hyperbolic Functions",
    icon=":material/interactive_space:",
)

topic2_analytic_geometry = st.Page(
    page="topics/2_analytic_geometry.py",
    title="Analytic Geometry",
    icon=":material/interactive_space:",
)

topic3_polynomial = st.Page(
    page="topics/3_quadratics_and_optimization.py",
    title="Quadratics and Optimization",
    icon=":material/interactive_space:",
)


# --- Navigation Setup with Sections ---
pg = st.navigation(
    {
        "Info": [home_page],
        "Topics": [topic1_hyperbolic, topic2_analytic_geometry, topic3_polynomial],
    }
)

# --- Run Navigation ---
pg.run()