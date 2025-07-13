import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_polynomial_standard(a0, a1, a2=0, a3=0, a4=0, a5=0):
    x = np.linspace(-10,10,num=1000)
    func = lambda x : a5 * x**5 + a4 * x**4 + a3 * x**3 + a2 * x**2 + a1 * x + a0

    fig = plt.figure(figsize=(6, 4))
    plt.ylim(-20, 20)
    plt.xlim(-8, 8)
    plt.axvline(color='black')
    plt.axhline(color='black')
    plt.plot(x, func(x), lw=3, color ='blue')
    plt.grid()
    # plt.show()

    return fig

def plot_polynomial_factor(a, r1, r2):
    x = np.linspace(-10,10,num=1000)
    func = lambda x : a * (x - r1) * (x - r2)

    fig = plt.figure(figsize=(6, 4))
    plt.ylim(-20, 20)
    plt.xlim(-8, 8)
    plt.axvline(color='black')
    plt.axhline(color='black')
    plt.plot(x, func(x), lw=3, color ='green')
    plt.grid()
    # plt.show()

    return fig

st.markdown('''<style> .katex-html { text-align: left; } </style>''', unsafe_allow_html=True)

st.title("Quadratics and Optimization")

st.markdown('''<style> .katex-html { text-align: left; } </style>''', unsafe_allow_html=True)

st.header("Standard Form and Factor Form")

st.write("Polynomial function in standard form:")
st.latex(r'''
    \qquad f(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0, \qquad \quad a_i \in \mathbb{R}, i \in [0, n]
    ''')

st.write("Polynomial function in factor form:")
st.latex(r'''
    \qquad f(x) = a (x - r_{n}) (x - r_{n-1}) \cdots (x - r_1), \qquad \quad a, r_i \in \mathbb{R}, i \in [1, n]
    ''')
st.write("\n")

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    a0 = st.slider(f'Standard form: $a_0$ ', min_value=-10.0, max_value=10.0, value=-4.0, step=0.1)
    a1 = st.slider(f'Standard form: $a_1$:', min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
    a2 = st.slider(f'Standard form: $a_2$:', min_value=-2.0, max_value=2.0, value=1.0, step=0.1)

    fig = plot_polynomial_standard(a0, a1, a2)
    # ...
    st.pyplot(fig) # instead of plt.show()

with fig_col2:
    r1 = st.slider(f'Factor form: $r_1$', min_value=-10.0, max_value=10.0, value=-2.0, step=0.1)
    r2 = st.slider(f'Factor form: $r_2$', min_value=-10.0, max_value=10.0, value=2.0, step=0.1)
    a  = st.slider(f'Factor form: $a$', min_value=-2.0, max_value=2.0, value=1.0, step=0.1)

    fig2 = plot_polynomial_factor(a, r1, r2)
    # ...
    st.pyplot(fig2) # instead of plt.show()

st.header("Optimization Using Quadratic Functions")

st.markdown(r'''Quadratic functions have global min/max values for specific $x$. Many real-world problems 
            can be formulated as quadratic functions, hence we can find specific $x$ value to optimize
            (i.e., minimize or maximize) the output.
            ''')

st.markdown("Problem 1: &nbsp;&nbsp;&nbsp;&nbsp;what is the biggest possible area of a rectangle formed by 100m fence with one side against the cliff?")
st.latex(r'''\qquad Area = x \cdot y, \quad 2x + y = 100, \quad x, y > 0''')
st.write("\n")

st.markdown("Problem 2: &nbsp;&nbsp;&nbsp;&nbsp;prove that arithmetic mean is greater than or equal to geometric mean.")
st.latex(r'''\qquad \frac{x + y}{2} \geq \sqrt{xy}, \quad x, y > 0''')
st.write("\n")

st.header("Principal Square Root")

st.markdown(r'''A square root of $x$ is a number $r$ whose square is $x$ (i.e., $r^2 = x$). Every positive 
            number has two square roots (e.g., both $+5$ and $-5$ are sqaure roots of $25$). 
            ''')

st.markdown(r'''When working with unknowns, it gets a bit tricky since we don't know the value of the unknown 
            yet. The principal square root of unknown variable needs to take the absolute value:
            ''')

st.latex(r'''\qquad \sqrt{a^2} = |a|, \quad a \in \mathbb{R}''')

st.markdown(r'''The following problems are designed to test your understanding of the principal square root and its properties:
            ''')

st.markdown("**Problem 3: &nbsp;&nbsp;&nbsp;&nbsp;AMC10 2022 A (6)**")
st.markdown(r"Which expression is equal to $\left| a-2-\sqrt{(a-1)^2} \right|$ for $a<0?$")
st.latex(r'''\qquad \textbf{(A) } 3-2a \qquad \textbf{(B) } 1-a \qquad \textbf{(C) } 1 \qquad \textbf{(D) } a+1 \qquad \textbf{(E) } 3''')
st.write("\n")

st.markdown("**Problem 4: &nbsp;&nbsp;&nbsp;&nbsp;AMC10 2000 (9) (slightly modified version)**")
st.markdown(r"If $(x-2)^2 = p$, where $x<2$, then $x - \sqrt{p} = ?$")
st.latex(r'''\qquad \textbf{(A)}\ -2 \qquad\textbf{(B)}\ 2 \qquad\textbf{(C)}\ 2-2 \sqrt{p} \qquad\textbf{(D)}\ 2 \sqrt{p}-2 \qquad\textbf{(E)}\ |2 \sqrt{p}-2|''')
st.write("\n")

st.header("Vieta's Formulas")

st.text("By expanding the factor form of a polynomial function to standard form, we can find the relationship between coefficients and the roots.")
st.latex(r'''
    f(x) = a_n x^n + \dotsb + a_1 x + a_0 = a_n (x-r_1)(x-r_2) \dotsb (x-r_n) = 0
    ''')

st.text("Vieta's formulas can be expressed as follows:")
st.latex(r'''\qquad r_1 + r_2 + \dotsb + r_n = (-1)^1 \cdot \frac{a_{n-1}}{a_n},''')
st.latex(r'''\qquad r_1 r_2 + r_1 r_3 + \dotsb + r_{n-1} r_n = (-1)^2 \cdot \frac{a_{n-2}}{a_n},''')
st.latex(r'''\qquad \dotsb''')
st.latex(r'''\qquad r_1 r_2 \dotsb r_n = (-1)^n \cdot \frac{a_0}{a_n}''')

st.markdown(r"**Problem 5**: &nbsp;&nbsp;&nbsp;&nbsp;$r_1$, $r_2$ and $r_3$ are the roots of $2 x^3 + 6 x^2 - 5 x + 2 = 0$, answer the following questions:")
st.latex(r'''\qquad r_1 + r_2 + r_3 = ?''')
st.latex(r'''\qquad r_1 \cdot r_2 \cdot r_3 = ?''')
st.latex(r'''\qquad r_1 \cdot r_2 + r_1 \cdot r_3 + r_2 \cdot r_3 = ?''')
st.latex(r'''\qquad \frac{1}{r_1} + \frac{1}{r_2} + \frac{1}{r_3} = ?''')
st.latex(r'''\qquad  r_1 ^2 + r_2 ^2 + r_3 ^ 2 = ?''')
st.latex(r'''\qquad  r_1 ^3 + r_2 ^3 + r_3 ^3 = ? \qquad \text{hint: Power reduction trick}''')
st.write("\n")

st.subheader("Related problems from AMC 10/12")

st.markdown("**AMC10 2002 A (14)**")
st.markdown(r"Both roots of the quadratic equation $x^2 - 63x + k = 0$ are prime numbers. The number of possible values of $k$ is")
st.latex(r'''\qquad \text{(A)}\ 0 \qquad \text{(B)}\ 1 \qquad \text{(C)}\ 2 \qquad \text{(D)}\ 4 \qquad \text{(E) more than 4}''')
st.write("\n")

st.markdown("**AMC10 2002 B (10)**")
st.markdown(r"Suppose that $a$ and $b$ are nonzero real numbers, and that the equation $x^2+ax+b=0$ has solutions $a$ and $b$. What is the pair $(a,b)$?")
st.latex(r'''\qquad \mathrm{(A) \ } (-2,1)\qquad \mathrm{(B) \ } (-1,2)\qquad \mathrm{(C) \ } (1,-2)\qquad \mathrm{(D) \ } (2,-1)\qquad \mathrm{(E) \ } (4,4)''')
st.write("\n")

st.markdown("**AMC10 2022 B (7)**")
st.markdown(r"For how many values of the constant $k$ will the polynomial $x^{2}+kx+36$ have two distinct integer roots?")
st.latex(r'''\qquad \textbf{(A)}\ 6 \qquad\textbf{(B)}\ 8 \qquad\textbf{(C)}\ 9 \qquad\textbf{(D)}\ 14 \qquad\textbf{(E)}\ 16''')
st.write("\n")

st.markdown("**AMC10 2006 B (14)**")
st.markdown(r"Let $a$ and $b$ be the roots of the equation $x^2-mx+2=0$. Suppose that $a+(1/b)$ and $b+(1/a)$ are the roots of the equation $x^2-px+q=0$. What is $q$?")
st.latex(r'''\qquad \mathrm{(A) \ } \frac{5}{2}\qquad \mathrm{(B) \ } \frac{7}{2}\qquad \mathrm{(C) \ } 4\qquad \mathrm{(D) \ } \frac{9}{2}\qquad \mathrm{(E) \ } 8''')
st.write("\n")

st.markdown("**AMC10 2022 A (16)**")
st.markdown(r"The roots of the polynomial $10x^3 - 39x^2 + 29x - 6$ are the height, length, and width of a rectangular box (right rectangular prism). A new rectangular box is formed by lengthening each edge of the original box by $2$ units. What is the volume of the new box?")
st.latex(r'''\qquad \textbf{(A) } \frac{24}{5} \qquad \textbf{(B) } \frac{42}{5} \qquad \textbf{(C) } \frac{81}{5} \qquad \textbf{(D) } 30 \qquad \textbf{(E) } 48''')
st.write("\n")

st.markdown("**AMC10 2000 (24)**")
st.markdown(r"Let $f$ be a function for which $f(\frac{x}{3}) = x^2 + x + 1$. Find the sum of all values of $z$ for which $f(3z) = 7$")
st.latex(r"\qquad \textbf{(A)}\ -\frac{1}{3} \qquad\textbf{(B)}\ -\frac{1}{9} \qquad\textbf{(C)}\ 0 \qquad\textbf{(D)}\ \frac{5}{9} \qquad\textbf{(E)}\ \frac{5}{3}")
st.write("\n")


