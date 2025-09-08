import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.markdown('''<style> .katex-html { text-align: left; } </style>''', unsafe_allow_html=True)

st.title("Markov Chain and PageRank")

st.write(r'''
        Markov Chain is a mathematical model for a system, where the future state depends only on
        the current state and not on the sequence of events that preceded it. It is widely used 
         in various fields, including economics, game theory, and computer science. For an 
         interesting overview, please refer to YouTube video: [The Strange Math That Predicts 
         (Almost) Anything](https://www.youtube.com/watch?v=KZeIEiBrT_w).
         ''')

st.subheader("Modeling the Web with Random Walks")

st.write(r'''
         The whole web pages can be modeled as a graph, where each page is a node, 
         and each hyperlink to other page is a directed edge, allowing viewers 
         to walk to the linked pages. 
         ''')

st.write(r''' 
         Assuming a 4-page system, page 1 links to page 2, 3 and 4, given 1/3 chance to visit 
         them. Page 2 has links to page 3 and 4, given 1/2 chance to each of them. Page 3 links to 
         page 1 only, given 100% chance to it. Page 4 links to page 1 and 3, given 1/2 chance to 
         them. This gives the following transition matrix: 
         ''')

st.write(r'''
        $$
        \qquad A = \begin{pmatrix}
        0   & 0   & 1 & 1/2 \\
        1/3 & 0   & 0 & 0   \\
        1/3 & 1/2 & 0 & 1/2 \\
        1/3 & 1/2 & 0 & 0 
        \end{pmatrix}
        $$
         ''')

st.write(r'''
        Assuming a random walker starts from page 1, the initial state vector is: $ P_0 = [1, 0, 0, 0]^T $.
        After one step, the state vector becomes: $ P_1 = A P_0. $ Repeating this process, the state vector 
        converges to:
        ''')

st.write(r"$\qquad P = AP$")

st.write(r'''
        We can see that the solution is the eigenvector of matrix A corresponding to the eigenvalue 1. 
        For above example, the steady state vector is: $P = [0.39, 0.13, 0.29, 0.19]^T$ and can be used 
        to rank the importance of the pages.
        ''')

st.subheader("Avoiding Disconnected Graphs")

st.write(r'''
         In real world, there are many dead ends (pages without any outgoing links) and disconnected
         graphs (groups of pages without any links to other groups). To avoid these issues, Page and 
         Brin introduced a damping factor, which allows viewers to jump to a random page with some 
         small probability. The modified transition matrix becomes:
        ''')
 
st.write(r'''
        $$ \qquad M = (1-p) A + pE $$
        ''')

st.write(r''' 
        Where $E$ is a matrix with all entries equal to $1/n$, and $n$ is the number of pages, and $p$
        is the damping factor, usually set to 0.15.
        ''')

st.subheader("Think Recursively")

st.write(r'''
         Similar to Markov Chain model, there are many interesting problems can be solved by thinking 
         recursively. Here are some more examples:
         ''')

st.write(r"Problem 1: what is $x$, given the following equations:")
st.write(r'''
         $$ \qquad x = \sqrt{1 + \sqrt{1 + \sqrt{1 + ... }}}$$
         ''')

st.write(r"Problem 2: what is $x$, given the following equations:")
st.write(r'''
         $$ \qquad x = 1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{1 + ...}}}$$
         ''')