import streamlit as st

# --- PAGE SETUP ---

home_page = st.Page(
    page="topics/home.py",
    title="Python for Intuitive Math",
    icon=":material/home:",
    default=True,
)

ds1_visualize_us_data = st.Page(
    page="ds_tasks/1_visualize_us_data.py",
    title="Visualize US Population",
    icon=":material/database_search:",
)

ds2_visualize_crime_data = st.Page(
    page="ds_tasks/2_vis_us_crime_data.py",
    title="Visualize US Crime Data",
    icon=":material/database_search:",
)

sim1_fastest_rolling_car = st.Page(
    page="simulation/1_fastest_rolling_car.py",
    title="Fastest Rolling Car",
    icon=":material/speed:",
)

topic1_hyperbolic = st.Page(
    page="topics/1_hyperbolic_functions.py",
    title="Hyperbolic Functions",
    icon=":material/book_ribbon:",
)

topic2_analytic_geometry = st.Page(
    page="topics/2_analytic_geometry.py",
    title="Analytic Geometry",
    icon=":material/book_ribbon:",
)

topic3_quadratics = st.Page(
    page="topics/3_quadratics_and_optimization.py",
    title="Quadratics and Optimization",
    icon=":material/book_ribbon:",
)

topic4_differential = st.Page(
    page="topics/4_differential_equations.py",
    title="Differential Equations",
    icon=":material/book_ribbon:",
)

topic5_markov_pagerank = st.Page(
    page="topics/5_markov_pagerank.py",
    title="Markov Chain and PageRank",
    icon=":material/book_ribbon:",
)

topic11_uam = st.Page(
    page="topics/11_physics_uam.py",
    title="Uniformly Accelerated Motion",
    icon=":material/book_ribbon:",
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
        "Data Science": [
            ds1_visualize_us_data,
            ds2_visualize_crime_data,
        ],
        "Simulations": [
            sim1_fastest_rolling_car,
        ],
        "Math Topics": [
            topic3_quadratics,
            topic1_hyperbolic,
            topic2_analytic_geometry,
            topic4_differential,
            topic5_markov_pagerank,
            topic11_uam,
        ],
        "Tools": [
            tool1_loan_calculator,
        ],
    }
)

# --- Run Navigation ---
pg.run()
