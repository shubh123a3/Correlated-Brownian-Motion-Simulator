import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_correlated_bm(num_paths, num_steps, T, rho):
    Z1 = np.random.normal(0.0, 1.0, [num_paths, num_steps])
    Z2 = np.random.normal(0.0, 1.0, [num_paths, num_steps])
    W1 = np.zeros([num_paths, num_steps + 1])
    W2 = np.zeros([num_paths, num_steps + 1])
    dt = T / float(num_steps)
    time = np.zeros([num_steps + 1])
    
    for i in range(num_steps):
        if num_paths > 1:
            Z1[:, i] = (Z1[:, i] - np.mean(Z1[:, i])) / np.std(Z1[:, i])
            Z2[:, i] = (Z2[:, i] - np.mean(Z2[:, i])) / np.std(Z2[:, i])
        
        Z2[:, i] = rho * Z1[:, i] + np.sqrt(1.0 - rho**2) * Z2[:, i]
        W1[:, i+1] = W1[:, i] + np.power(dt, 0.5) * Z1[:, i]
        W2[:, i+1] = W2[:, i] + np.power(dt, 0.5) * Z2[:, i]
        time[i+1] = time[i] + dt
    
    return {"time": time, "W1": W1, "W2": W2}

st.title("Correlated Brownian Motion Simulation")

st.markdown("""
This app simulates correlated Brownian motion paths and visualizes them. 
Adjust the correlation coefficient to see how it affects the relationship between two Brownian motion paths.

- Negative correlation: Paths tend to move in opposite directions
- Positive correlation: Paths tend to move together
- Zero correlation: Paths move independently
""")

# Sidebar for user input
st.sidebar.header("Simulation Parameters")
num_paths = st.sidebar.number_input("Number of Paths", min_value=1, max_value=10, value=1)
num_steps = st.sidebar.number_input("Number of Steps", min_value=100, max_value=1000, value=500)
T = st.sidebar.number_input("Total Time", min_value=0.1, max_value=5.0, value=1.0)
rho = st.sidebar.slider("Correlation Coefficient", min_value=-1.0, max_value=1.0, value=0.0, step=0.1)

# Generate paths
paths = generate_correlated_bm(num_paths, num_steps, T, rho)
time_grid = paths["time"]
W1 = paths["W1"]
W2 = paths["W2"]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(time_grid, W1.T, label="W1", alpha=0.7)
ax.plot(time_grid, W2.T, label="W2", alpha=0.7)
ax.set_title(f'Correlated Brownian Motion (ρ = {rho:.2f})')
ax.set_xlabel("Time")
ax.set_ylabel("W(t)")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# Additional information
st.subheader("Interpretation")
if rho < -0.5:
    st.write("The paths show a strong tendency to move in opposite directions.")
elif rho > 0.5:
    st.write("The paths show a strong tendency to move together.")
elif -0.2 <= rho <= 0.2:
    st.write("The paths show little to no correlation, moving mostly independently.")
else:
    st.write("The paths show a weak correlation. Observe their general trends.")

st.subheader("Key Concepts")
st.markdown("""
- **Brownian Motion**: A continuous-time stochastic process, fundamental in modeling random behavior over time.
- **Correlation**: Measures the strength and direction of the linear relationship between two variables.
- **Correlation Coefficient (ρ)**: Ranges from -1 to 1, where:
    - ρ = 1: Perfect positive correlation
    - ρ = 0: No correlation
    - ρ = -1: Perfect negative correlation
""")

st.subheader("Formula")
st.latex(r"""
\begin{align}
W_1 &= Z_1 \\
W_2 &= \rho Z_1 + \sqrt{1 - \rho^2} Z_2
\end{align}
""")
st.write("Where Z₁ and Z₂ are independent standard Brownian motions, and ρ is the correlation coefficient.")