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
    v0 = st.number_input("Initial velocity (m/s)", value=2.0, step=0.25)
with in_col2:
    a = st.number_input("Acceleration (m/s²)", value=1.0, step=0.25)
with in_col3:
    t_max = st.number_input("Total time (s)", min_value=1.0, max_value=10.0, value=3.0, step=1.0)

st.write("\n")
col1, col2 = st.columns([0.5, 0.5])
with col1:
    st.write("Customize the graph X/Y Axes\n")
    # op_y = st.selectbox("Y Axis", ("Position", "Velocity", "Acceleration"))
    op_y = st.radio(
        "Y Axis:",
        options=["Position", "Velocity", "Acceleration"],
        index=0,  # Velocity will be pre-selected
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


st.subheader("Understanding UAM with Velocity-Time Graphs")

st.markdown(r'''There are five variables in uniformly accelerated motion (UAM). They are 
    initial velocity ($v_0$), final velocity ($v_t$), acceleration ($a$), time of 
    acceleration ($t$), and displacement ($\Delta x$). The graph forms a trapezoid, 
    where the area of shaded region is the total displacement. 
    ''')

col1, col2 = st.columns([0.5, 0.5])
with col1:
    st.markdown(r"- $v_0$ = " + rf"{v0} (trapezoid top)")
    st.markdown(r"- $v_t$ = " + rf"{v[-1]} (trapezoid base)")
    st.markdown(r"- $a$ = " + rf"{a} (velocity slope)")
    st.markdown(r"- $t$ = " + rf"{t_max} (trapezoid height)")
    st.markdown(r"- $\Delta x$ = " + rf"{x[-1]} (trapezoid area)")
    st.markdown(r"Given any three variables, the trapezoid is decided and the other two variables can be calculated.")
with col2:
    x_arr = t
    y_arr = v
    fig, ax = plt.subplots(figsize=(6, 4))
    plt.ylim(-1, 6)
    plt.xlim(0, max(x_arr)+0.15)
    ax.fill_between(x_arr, 0, y_arr, color='lightblue')
    ax.plot(x_arr, y_arr, label=f"Velocity (m/s)")
    ax.set_xlabel(f"Time (s)")
    ax.set_ylabel(f"Velocity (m/s)")
    ax.set_title(f"Velocity (m/s) vs. Time (s)")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)

st.subheader("Derivation of Common UAM Equations")

st.markdown(r'''Starting from rest: $v_0 = 0$, trapezoid simplifies to a right angle triangle''')
st.markdown(r'''- $v_t = a t \qquad \quad$ ($v_t$ is triangle height and $t$ is triangle base)''')
st.markdown(r'''- $\Delta x = \frac{1}{2} v_t t = \frac{1}{2} a t^2 \quad$ ($\Delta x$ is triangle area)''')
st.markdown(r'''General case: $v_0 \neq 0$''')
st.markdown(r'''- $v_t = v_0 + a t \quad \Leftrightarrow \quad a = (v_t - v_0)/t$''')
st.markdown(r'''- $\Delta x = v_0 t + \frac{1}{2} a t^2 \quad$ (sum of rectangle and triangle area)''')
st.markdown(r'''- $\Delta x = \frac{1}{2} (v_0 + v_t) t \quad$ (trapezoid area)''')
st.markdown(r'''- $2 a \Delta x = (v_0 + v_t) a t = (v_t + v_0) (v_t - v_0)= {v_t}^2 - {v_0}^2\quad$ (substritute $t = (v_t - v_0)/a$)''')
