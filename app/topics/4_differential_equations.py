import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.integrate import odeint


# ---- Epidemic Models ----
def sir_model(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


def seir_model(y, t, N, beta, sigma, gamma):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt


def sidr_model(y, t, N, beta, gamma, theta):
    S, I, D, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - (gamma + theta) * I
    dDdt = theta * I
    dRdt = gamma * I
    return dSdt, dIdt, dDdt, dRdt


def seird_model(y, t, N, beta, sigma, gamma, theta):
    S, E, I, D, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - (gamma + theta) * I
    dDdt = theta * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dDdt, dRdt


st.markdown(
    """<style> .katex-html { text-align: left; } </style>""", unsafe_allow_html=True
)

st.title("Differential Equations")

st.write(r"""
         Differential equations can be used to model and predict various real-world phenomena, 
         including expansion of the universe, climate change, pandemic models, financial markets,
         and much more. It is also central to many fundamental debates such as is the future 
         deterministic (Laplace's demon)? Does free will exist or not? For more in-depth discussion, 
         please refer to **Dr. Sabine Hossenfelder**'s YouTube video about Differential Equations: 
         https://www.youtube.com/watch?v=Em339AlejIs 
         """)

st.write(r"""
         There are two main type of solutions to differential equations: analytical solutions and numerical solutions.
         Analytical solutions are closed-form expressions that exactly satisfy the differential equation, while numerical 
         solutions are approximations obtained through discretized methods.

         - Analytical Solutions: several methods (e.g., guess-and-check, energy conservation, series expansion, 
         Laplace transform or Hamitonian flow) are explained in this video: https://www.youtube.com/watch?v=0kY3Wpvutfs 

         - Numerical Solutions: descrete methods replacing derivatives with finite differences. Common techniques 
         include Euler's method for simple approximations, Runge-Kutta methods for high-accuracy temporal 
         evolution, and finite-difference methods for boundary value problems. Python Scipy's 'odeint' is
         used here to solve the epidemic models. 
         """)

st.subheader("Epidemic Models (SIR, SEIR, SIDR, SEIRD)")

st.write(r"""A concrete example of differential equations is to model the spread of infectious diseases. 
         There are four common models: SIR, SEIR, SIDR, and SEIRD, where SEIRD models more factors to 
         determine the rate of change of each compartment over time: """)
st.markdown(
    r" - **Susceptible (S)**: $$\frac{dS}{dt} = - \beta \frac{S I}{N}$$, where $$\beta$$ is the infection rate"
)
st.markdown(
    r" - **Exposed (E)**: $$\frac{dE}{dt} = \beta \frac{S I}{N} - \sigma E$$, where $$\sigma$$ is the incubation rate (only in SEIR/SEIRD)"
)
st.markdown(
    r" - **Infected (I)**: $$\frac{dI}{dt} = \sigma E - (\gamma + \theta) I$$, where recovered and deceased leave this compartment"
)
st.markdown(
    r" - **Recovered (R)**: $$\frac{dR}{dt} = \gamma I$$, where $$\gamma$$ is the recovery rate"
)
st.markdown(
    r" - **Deceased (D)**: $$\frac{dD}{dt} = \theta I$$, where $$\theta$$ is the mortality rate. (only in SIDR/SEIRD)"
)

st.subheader("Set Parameters of a Given Disease:")

in_col1, in_col2 = st.columns(2)
with in_col1:
    beta = st.slider(
        r"Infection Rate $\beta$", min_value=0.0, max_value=2.0, value=0.6, step=0.1
    )
    sigma = st.slider(
        r"Incubation Rate $\sigma$ (for SEIR/SEIRD)",
        min_value=0.0,
        max_value=1.0,
        value=1.0 / 5.0,
        step=0.01,
    )
with in_col2:
    gamma = st.slider(
        r"Recovery Rate $\gamma$",
        min_value=0.0,
        max_value=1.0,
        value=1.0 / 7.0,
        step=0.01,
    )
    theta = st.slider(
        r"Mortality Rate $\theta$ (for SIDR/SEIRD)",
        min_value=0.0,
        max_value=0.5,
        value=0.02,
        step=0.01,
    )

# ============ Plot: Epidemic Model ============
st.subheader("Epidemic Simulation:")

st.write(r"""Given the disease parameters and initial conditions, we use scipy's odeint function to 
         integrate the differential equations, which gives us the number of individuals in each 
         compartment over time.""")

col1, col2 = st.columns([0.33, 0.63])
with col1:
    model_choice = st.selectbox(
        "Select Model:", ["SIR", "SEIR", "SIDR", "SEIRD"], index=3
    )
    N = st.number_input(
        "Total Population (N)", min_value=2, max_value=200000, value=100000, step=10
    )
    days = st.slider("Simulation Days", min_value=10, max_value=365, value=180, step=10)

    st.write("Initial condition: 1 infected, 0 recovered/deceased/exposed")
    I0 = 1
    R0 = 0
    D0 = 0
    E0 = 0

    t = np.linspace(0, days - 1, days)  # e.g., days=90 -> t=0..89
    # Ensure initial sums don't exceed N
    sum_init = I0 + R0 + D0 + E0
    if sum_init > N:
        st.warning("Initial states exceed total population. Clamping E0 to fit.")
        E0 = max(0, N - (I0 + R0 + D0))

    S0 = N - I0 - R0 - D0 - E0
    # ---- Solve the chosen model ----
    if model_choice == "SIR":
        y0 = (S0, I0, R0)
        result = odeint(sir_model, y0, t, args=(N, beta, gamma))
        S, I, R = result.T
        E = np.zeros_like(S)
        D = np.zeros_like(S)
    elif model_choice == "SEIR":
        y0 = (S0, E0, I0, R0)
        result = odeint(seir_model, y0, t, args=(N, beta, sigma, gamma))
        S, E, I, R = result.T
        D = np.zeros_like(S)
    elif model_choice == "SIDR":
        y0 = (S0, I0, D0, R0)
        result = odeint(sidr_model, y0, t, args=(N, beta, gamma, theta))
        S, I, D, R = result.T
        E = np.zeros_like(S)
    elif model_choice == "SEIRD":
        y0 = (S0, E0, I0, D0, R0)
        result = odeint(seird_model, y0, t, args=(N, beta, sigma, gamma, theta))
        S, E, I, D, R = result.T

with col2:
    fig, ax = plt.subplots(figsize=(6, 4))
    # plt.ylim(-1, 5)
    # plt.xlim(0, max(x_arr))
    ax.plot(t, S, label="Susceptible", color="blue")
    ax.plot(t, I, label="Infected", color="red")
    ax.plot(t, R, label="Recovered", color="green")
    if model_choice in ("SEIR", "SEIRD"):
        ax.plot(t, E, label="Exposed", color="orange")
    if model_choice in ("SIDR", "SEIRD"):
        ax.plot(t, D, label="Deceased", color="black")
    ax.set_xlabel("days")
    ax.set_ylabel("Population")
    ax.set_title(f"{model_choice} Simulation (Population={N})")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)
