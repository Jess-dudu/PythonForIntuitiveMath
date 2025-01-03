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


# --- Navigation Setup with Sections ---
pg = st.navigation(
    {
        "Info": [home_page],
        "Topics": [topic1_hyperbolic],
    }
)

# --- Run Navigation ---
pg.run()