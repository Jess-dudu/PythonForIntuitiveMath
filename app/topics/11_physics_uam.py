import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_uam_data(v0, a, t_max):
    t = np.linspace(0, t_max, 200)
    v = v0 + a * t
    x = v0 * t + 0.5 * a * t**2
    return t, v, x

st.title("Uniformly Accelerated Motion")

st.markdown('''<style> .katex-html { text-align: left; } </style>''', unsafe_allow_html=True)

st.subheader("Graphing Uniformly Accelerated Motion")

st.latex(r"\qquad v(t) = v_0 + a t")
st.latex(r"\qquad x(t) = v_0 t + \frac{1}{2} a t^2")
st.write("\n")

in_col1, in_col2, in_col3 = st.columns(3)
with in_col1:
    v0 = st.number_input("Initial velocity (m/s)", value=-0.5, step=0.25)
with in_col2:
    a = st.number_input("Acceleration (m/s²)", value=1.0, step=0.25)
with in_col3:
    t_max = st.number_input("Total time (s)", min_value=1.0, max_value=10.0, value=3.0, step=1.0)

st.write("\n")
col1, col2 = st.columns([0.33, 0.67])
with col1:
    st.write("Customize the graph X/Y Axes\n")
    # op_y = st.selectbox("Y Axis", ("Position", "Velocity", "Acceleration"))
    op_y = st.radio(
        "Y Axis:",
        options=["Position", "Velocity", "Acceleration"],
        index=0,  # Position will be pre-selected
    )

    # op_x = st.selectbox("X Axis", ("Time", "Position"))
    op_x = st.radio(
        "X Axis:",
        options=["Time", "Position"],
        index=0,  # Time will be pre-selected
    )

with col2:
    t, v, x = generate_uam_data(v0, a, t_max)

    x_arr = t
    if op_x == "Position":
        x_arr = x
    y_arr = x
    if op_y == "Velocity":
        y_arr = v
    elif op_y == "Acceleration":
        y_arr = np.full_like(t, a)

    fig, ax = plt.subplots(figsize=(6, 4))
    # plt.ylim(-1, 5)
    # plt.xlim(0, max(x_arr))
    ax.plot(x_arr, y_arr, label=f"{op_y}")
    ax.set_xlabel(f"{op_x}")
    ax.set_ylabel(f"{op_y}")
    ax.set_title(f"{op_y} vs. {op_x}")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)


