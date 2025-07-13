import streamlit as st

# --- PAGE SETUP ---

home_page = st.Page(
    page="topics/home.py",
    title="Python for Intuitive Math",
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

topic3_quadratics = st.Page(
    page="topics/3_quadratics_and_optimization.py",
    title="Quadratics and Optimization",
    icon=":material/interactive_space:",
)

tool1_loan_calculator = st.Page(
    page="tools/1_loan_calculator.py",
    title="Loan Calculator",
    icon=":material/attach_money:",
)


# --- Navigation Setup with Sections ---
pg = st.navigation(
    {
        "Home": [home_page],
        "Topics": [topic3_quadratics, topic1_hyperbolic, topic2_analytic_geometry],
        "Tools": [tool1_loan_calculator],
    }
)

# --- Run Navigation ---
pg.run()