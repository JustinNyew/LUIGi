import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

st.title("🧮 Smart Calculator with Graphs")

# --- Calculator ---
st.header("Basic Calculator")
expression = st.text_input("Enter a math expression (e.g. 2 + 3 * 4):", "")

if expression:
    try:
        result = eval(expression)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error in expression: {e}")

# --- Graphing ---
st.header("Function Plotter")
func_input = st.text_input("Enter a function of x (e.g. x**2 + 2*x):", "")

if func_input:
    try:
        x = sp.symbols('x')
        func = sp.sympify(func_input)
        func_lambdified = sp.lambdify(x, func, modules=["numpy"])
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func_lambdified(x_vals)

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_title(f"Graph of {func_input}")
        ax.grid(True)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error plotting function: {e}")
