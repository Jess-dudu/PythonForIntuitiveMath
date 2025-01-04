import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_hyperbolic_funcs(a, option='tanh'): # cosh/sinh/tanh
    x = np.linspace(-10, 10, num=1000)
    func_cosh = lambda x : a * np.cosh(x / a)
    func_sinh = lambda x : a * np.sinh(x / a)
    func_tanh = lambda x : a * np.tanh(x / a)
    func_exp_p = lambda x : a * np.exp(x / a) / 2
    func_exp_n = lambda x : - a * np.exp( -x / a) / 2

    fig = plt.figure(figsize=(6, 4))
    plt.ylim(-5, 5)
    plt.xlim(-5, 5)

    if option == 'sinh': # sinh
        plt.plot(x, func_exp_p(x), 'k:', lw = 1) 
        plt.plot(x, func_exp_n(x), 'k--', lw = 1) 
        plt.plot(x, func_sinh(x), lw=2, color ='red')   # sinh
        plt.legend(['  a * exp(x/a) / 2', '- a * exp(-x/a) / 2', '  a * sinh(x/a)']) 
    elif option == 'cosh': # cosh
        plt.plot(x, func_exp_p(x), 'k:', lw = 1) 
        plt.plot(x, -func_exp_n(x), 'k--', lw = 1) 
        plt.plot(x, func_cosh(x), lw=2, color ='blue')  # cosh
        plt.legend(['  a * exp(x/a) / 2', '  a * exp(-x/a) / 2', '  a * cosh(x/a)']) 
    else: # tanh
        plt.plot(x, func_sinh(x), 'k:', lw=2, color ='red')   # sinh
        plt.plot(x, func_cosh(x), 'k--', lw=2, color ='blue')  # cosh
        plt.plot(x, func_tanh(x), lw=2, color ='green') # tanh
        plt.legend(['  a * sinh(x/a)', '  a * cosh(x/a)', '  a * tanh(x/a)'])

    plt.grid()
    # plt.show()

    return fig


# st.set_page_config(layout='wide')

st.title("Hyperbolic Functions")

st.markdown('''<style> .katex-html { text-align: left; } </style>''', unsafe_allow_html=True)

st.header("Definition of Hyperbolic Functions")

st.latex(r'''
    \qquad y = \sinh(x) = \frac{e^x - e^{-x}}{2}, \qquad \qquad \qquad \quad x \in (-\inf, \inf), y \in (-\inf, \inf) \\
    \quad \\
    \qquad y = \cosh(x) = \frac{e^x + e^{-x}}{2}, \qquad \qquad \qquad \quad x \in (-\inf, \inf), y \in (1, \inf) \\
    \quad \\
    \qquad y = \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} = \frac{\sinh(x)}{\cosh(x)}, \qquad x \in (-\inf, \inf), y \in (-1, 1)
    ''')

st.write("\n")

option = st.selectbox(
    'Select the hyperbolic function to plot?',
    ('cosh', 'sinh', 'tanh'),
    index = 2 # default tanh
    )

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    fig = plot_hyperbolic_funcs(1.0, option)
    # ...
    st.pyplot(fig) # instead of plt.show()

st.write("\n")
st.header("Hyperbolic Functions in Real Life")

ex_col1, ex_col2 = st.columns(2)

with ex_col1:
    st.write("**Hanging Cable**")
    st.latex(r"y = c + a \cosh(x/a)")
    st.write("Cable's potential energy is minimizzed")
    st.image("assets/images/hyperbolic/HangingCable.png", width = 300)

with ex_col2:
    st.write("**Soap Film between Rings**")
    st.latex(r"y = c + a \cosh(x/a)")
    st.write("Film's surface area is minimized")
    st.image("assets/images/hyperbolic/SoapFilmBetweenRings.png", width = 275)

st.write("\n")
st.header("Trigonometric vs. Hyperbolic Functions")

st.subheader("Unit Circle vs. Hyperbola:")

col1, col2 = st.columns(2)

with col1:
    st.write("**Trigonometric (Points on Unit Circle)**")
    st.latex(r"\qquad x^2 \textcolor{red}{+} y^2 = 1")
    st.image("assets/images/hyperbolic/TrigFunctions.png", width=250)
    st.latex(r'''
             \qquad Area(red) = a/2 \\
             \quad \\
             \qquad x = \cos(a) = \cos(2A)\\
             \quad \\
             \qquad y = \sin(a) = \sin(2A) \\
             \quad \\
             \qquad \cos^2(a) \textcolor{red}{+} \sin^2(a) = 1 \\
             \quad \\
             ''')

with col2:
    st.write("**Hyperbolic Trig (Points on Hyperbola)**")
    st.latex(r"\qquad x^2 \textcolor{red}{-} y^2 = 1")
    st.image("assets/images/hyperbolic/HyperbolicFunctions.png", width=300)
    st.latex(r'''
             \qquad Area(red) = a/2 \\
             \quad \\
             \qquad x = \cosh(a) = \cosh(2A) \\
             \quad \\
             \qquad y = \sinh(a) = \sinh(2A) \\
             \quad \\
             \qquad \cosh^2(a) \textcolor{red}{-} \sinh^2(a) = 1 \\
             \quad \\
             ''')

st.subheader("Identity Functions:")

id_col1, id_col2 = st.columns(2)

with id_col1:
    st.write("**Trigonometric Identities**")
    st.latex(r'''
                \qquad \sin(-x) = -\sin(x) \\
                \quad \\
                \qquad \cos(-x) = \cos(x) \\
                \quad \\
                \qquad \cos^2(x) \textcolor{red}{+} \sin^2(x) = 1 \\
                \quad \\
                \qquad 1 \textcolor{red}{+} \tan^2(x) = \sec^2(x) \\
                \quad \\
                \qquad \sin(x + y) = \\
                \qquad \quad \sin(x)\cos(y) + \cos(x)\sin(y) \\
                \quad \\
                \qquad \cos(x + y) = \\
                \qquad \quad \cos(x)\cos(y) \textcolor{red}{-} \sin(x)\sin(y) \\
                \quad \\
                ''')

with id_col2:
    st.write("**Hyperbolic Trig. Identities**")
    st.latex(r'''
                \qquad \sinh(-x) = -\sinh(x) \\
                \quad \\
                \qquad \cosh(-x) = \cosh(x) \\
                \quad \\
                \qquad \cosh^2(x) \textcolor{red}{-} \sinh^2(x) = 1 \\
                \quad \\
                \qquad 1 \textcolor{red}{-} \tanh^2(x) = \operatorname{sech}^2(x) \\
                \quad \\
                \qquad \sinh(x + y) = \\
                \qquad \quad \sinh(x)\cosh(y) + \cosh(x)\sinh(y) \\
                \quad \\
                \qquad \cosh(x + y) = \\
                \qquad \quad \cosh(x)\cosh(y) \textcolor{red}{+} \sinh(x)\sinh(y) \\
                \quad \\
                ''')

st.subheader("Derivatives:")

dx_col1, dx_col2 = st.columns(2)

with dx_col1:
    st.write("**Trigonometric Derivatives**")
    st.latex(r'''
                \qquad \sin^{\prime}(x) = \cos(x) \\
                \quad \\
                \qquad \cos^{\prime}(x) = \textcolor{red}{-} \sin(x) \\
                \quad \\
                \qquad \tan^{\prime}(x) = \sec^2(x) \\
                ''')

with dx_col2:
    st.write("**Hyperbolic Trig. Derivatives**")
    st.latex(r'''
                \qquad \sinh^{\prime}(x) = \cosh(x) \\
                \quad \\
                \qquad \cosh^{\prime}(x) = \sinh(x) \\
                \quad \\
                \qquad \tanh^{\prime}(x) = \operatorname{sech}^2(x) \\
                ''')

