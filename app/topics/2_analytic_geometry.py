import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.markdown('''<style> .katex-html { text-align: left; } </style>''', unsafe_allow_html=True)

st.title("Analytic Geometry")
st.subheader("Cartesian Coordinate System")

st.markdown(r''' 
            Define cartesian coordinate system:
            - Its origin $O$
            - Its axes: direction and unit distance (e.g., $x$, $y$, $z$ axes in 3D space)
            ''')

st.markdown(r'''
            In physical world, a point $\boldsymbol{P}$ is defined by its coordinate $[x, y]$ in 2D or $[x, y, z]$ in 3D. \
            In data science, data points are described by $[x_1, x_2, \ldots, x_n]$ in high dimensional feature space.
            ''')

st.write("\n")
st.subheader("Arithmetic Operations on Vectors")

st.markdown(r'''
            Given $P_1 = [x_1, y_1, z_1]$ and $P_2 = [x_2, y_2, z_2]$:
            - **Add/Subtract**: $\boldsymbol{P_1} + \boldsymbol{P_2} = [x_1 + x_2, y_1 + y_2, z_1 + z_2] \quad$ \
            e.g., multiple foreces/velocities can be added to get total impact and speed.
            - **Multiply by scalar**: $k \boldsymbol{P_1} = [k x_1, k y_1, k z_1] \quad$ \
            e.g., displacement can be calculated as velocity multplied by time.
            - **Cross product**: $\boldsymbol{P_1} \times \boldsymbol{P_2} = \left \| \boldsymbol{P_1} \right \| \left \| \boldsymbol{P_2} \right \| \sin(\theta) \, \boldsymbol{n} \quad$ \
            e.g., parallelogram area or torque can be calculated with cross product.
            - Dot product (return value is a scalar): $\boldsymbol{P_1} \cdot \boldsymbol{P_2} = \left \| \boldsymbol{P_1} \right \| \left \| \boldsymbol{P_2} \right \| \cos(\theta) = x_1 x_2 + y_1 y_2 \quad$ \
            e.g., total work done is calculated by dot product between the force and the displacement.
            ''')

st.write("\n")
st.subheader("Relation to Geometric Concepts")

st.markdown(r'''
            - **Length**: $\left \| \boldsymbol{P_1} \boldsymbol{P_2} \right \| = \sqrt{(\boldsymbol{P_2} - \boldsymbol{P_1}) \cdot (\boldsymbol{P_2} - \boldsymbol{P_1})} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
                - Circle (given center $\boldsymbol{P_1}$ & radius $R$): $\quad \left \| \boldsymbol{P_1} \boldsymbol{P} \right \|^2 = (x - x_1)^2 + (y - y_1)^2 = R^2$
                - Ellipse (given center $\boldsymbol{P_1}$ & semi-major/minor axes $a$ & $b$): $\quad \frac{(x - x_1)^2}{a^2} + \frac{(y - y_1)^2}{b^2} = 1$
            - **Angle in 2-D space**:
                - Angle between $\boldsymbol{OP_1}$ and x-axis: $\quad \theta = \arctan({y_1} / {x_1})$
                - Perpendicular between $\boldsymbol{OP_1}$ and $\boldsymbol{OP_2}$: $\quad k_1 k_2 = \frac{y_1}{x_1} \frac{y_2}{x_2} = -1$
            - **Angle in n-D space**:
                - Angle between $\boldsymbol{OP_1}$ & $\boldsymbol{OP_2}$: $\quad \theta = \arccos(\frac{\boldsymbol{P_1} \cdot \boldsymbol{P_2}}{\left \| \boldsymbol{P_1} \right \| \left \| \boldsymbol{P_2} \right \|})$
                - Perpendicular: $\quad \boldsymbol{P_1} \cdot \boldsymbol{P_2} = x_1 x_2 + y_1 y_2 + z_1 z_2 = 0$
            - **Line & plane** (represented as linear equation):
                - 2-D line: $\quad y = m x + c \quad$ or $\quad a x + b y + c = 0 \quad$ or $\quad \frac{x - x_1}{x_2 - x_1} = \frac{y - y_1}{y_2 - y_1}$
                - n-D plane: $\quad \boldsymbol{n} \cdot (\boldsymbol{r} - \boldsymbol{P_1}) = a (x - x_1) + b (y - y_1) + c (z - z_1) = 0$
                - n-D line (intersection of n-1 planes): $\quad \frac{x - x_1}{x_2 - x_1} = \frac{y - y_1}{y_2 - y_1} = \frac{z - z_1}{z_2 - z_1}$
            - **Intersection points**: points satisfy multiple equations simultaneously
            - **Tangent**: when intersection points merge
            ''')

st.write("\n")
st.subheader("Solve Geometry Problems")

st.markdown(r''' Question 1: ''')
q1_col1, q1_col2 = st.columns(2, vertical_alignment="center")
with q1_col1:
    st.markdown(r'''
            A, C are on a circle with radius $5\sqrt{2}$. B is inside the circle and form a right angle triangle $\triangle{ABC}$, $\angle{B} = 90^{\circ}$, $AB = 6$ and $BC = 2$. What is the distance between circle's center $O$ and B?
            ''')

with q1_col2:
    st.image("assets/images/analytic_geometry/analytic_geometry_q1.png", width = 200)

st.write("\n")
st.markdown(r''' Question 2: ''')
q2_col1, q2_col2 = st.columns(2, vertical_alignment="center")
with q2_col1:
    st.markdown(r'''
            Inside a circle, cord AB and CD are perpendicular to each other and intersect at E. $AE = 2$, $BE = 6$ and $CE = 3$. What is the radius of the circle?
            ''')

with q2_col2:
    st.image("assets/images/analytic_geometry/analytic_geometry_q2.png", width = 200)

st.write("\n")
st.markdown(r''' Question 3: AMC 10 2016 A(19) ''')
q3_col1, q3_col2 = st.columns(2, vertical_alignment="center")
with q3_col1:
    st.markdown(r'''
            In rectangle $ABCD,$ $AB=6$ and $BC=3$. Point $E$ between $B$ and $C$, and point $F$ between $E$ and $C$ are such that $BE=EF=FC$. Segments $\overline{AE}$ and $\overline{AF}$ intersect $\overline{BD}$ at $P$ and $Q$, respectively. The ratio $BP:PQ:QD$ can be written as $r:s:t$ where the greatest common factor of $r,s,$ and $t$ is $1.$ What is $r+s+t$?
            ''')

with q3_col2:
    st.image("assets/images/analytic_geometry/analytic_geometry_q3.png", width = 300)

st.markdown(r'''
        $\textbf{(A) } 7 \qquad \textbf{(B) } 9 \qquad \textbf{(C) } 12 \qquad \textbf{(D) } 15 \qquad \textbf{(E) } 20$
        ''')

st.write("\n")
st.markdown(r''' Question 4: AMC 10 2015 B(19) ''')
q4_col1, q4_col2 = st.columns(2, vertical_alignment="center")
with q4_col1:
    st.markdown(r'''
                In $\triangle{ABC}$, $\angle{C} = 90^{\circ}$ and $AB = 12$. Squares $ABXY$ and $ACWZ$ are constructed outside of the triangle. The points $X, Y, Z$, and $W$ lie on a circle. What is the perimeter of the triangle?
                ''')

with q4_col2:
    st.image("assets/images/analytic_geometry/analytic_geometry_q4.png", width = 200)

st.markdown(r'''
            $\textbf{(A) }12+9\sqrt{3}\qquad\textbf{(B) }18+6\sqrt{3}\qquad\textbf{(C) }12+12\sqrt{2}\qquad\textbf{(D) }30\qquad\textbf{(E) }32$
            ''')
