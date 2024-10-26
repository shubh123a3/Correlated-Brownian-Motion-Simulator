# Correlated Brownian Motion Simulator

## Overview
try it by urself -https://correlated-brownian-motion-simulator.streamlit.app/

https://github.com/user-attachments/assets/00a3231f-aa67-46ab-bcc0-bf952676f87c


This project provides an interactive Streamlit application for simulating and visualizing correlated Brownian motion. It serves as an educational tool for understanding the concept of correlation in random processes, which is crucial in various fields such as finance, physics, and mathematics.

## Features

- Interactive adjustment of simulation parameters
- Real-time visualization of correlated Brownian motion paths
- Explanation of key concepts and formulas
- Interpretation of results based on correlation coefficient

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/correlated-brownian-motion-simulator.git
   ```
2. Navigate to the project directory:
   ```
   cd correlated-brownian-motion-simulator
   ```
3. Install the required dependencies:
   ```
   
Then, open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

## Theory

### Brownian Motion

Brownian motion, also known as the Wiener process, is a continuous-time stochastic process named after botanist Robert Brown. It describes the random motion of particles suspended in a fluid, resulting from their collision with fast-moving molecules in the fluid.

Key properties of Brownian motion:
1. W(0) = 0
2. For 0 ≤ s < t, the increment W(t) - W(s) is normally distributed with mean 0 and variance t - s
3. For non-overlapping time intervals, the increments are independent

### Correlated Brownian Motion

Correlated Brownian motion extends the concept to multiple dimensions, where the movements of two or more Brownian paths are related by a correlation coefficient.

The key formula for generating correlated Brownian motions is:

Given two independent standard Brownian motions Z₁ and Z₂, we can create correlated Brownian motions W₁ and W₂ with correlation ρ as follows:

W₁ = Z₁
W₂ = ρZ₁ + √(1 - ρ²)Z₂

The discretized version for simulation is:

ΔW₁ = √Δt Z₁
ΔW₂ = ρ√Δt Z₁ + √(1 - ρ²)√Δt Z₂

Where Z₁ and Z₂ are independent standard normal random variables, and Δt is the time step.

### Correlation Coefficient

The correlation coefficient ρ ranges from -1 to 1:
- ρ = 1: Perfect positive correlation
- ρ = 0: No correlation
- ρ = -1: Perfect negative correlation

In the context of Brownian motion:
- Positive correlation: Paths tend to move together
- Negative correlation: Paths tend to move in opposite directions
- Zero correlation: Paths move independently

## Implementation Details

The simulation is implemented in Python using NumPy for numerical computations and Matplotlib for plotting. The Streamlit framework is used to create an interactive web application.

Key functions:
1. `generate_correlated_bm`: Generates correlated Brownian motion paths
2. Streamlit interface: Allows users to adjust parameters and visualize results in real-time

## Applications

Understanding correlated Brownian motion is crucial in various fields:
1. Finance: Modeling correlated asset prices, risk management
2. Physics: Studying particle behavior in fluids
3. Biology: Analyzing molecular dynamics
4. Environmental science: Modeling pollutant dispersion

## Contributing

Contributions to improve the simulator or extend its capabilities are welcome. Please feel free to submit pull requests or open issues for discussion.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the work on stochastic processes by Kiyoshi Itō and other mathematicians
- Built with Streamlit, NumPy, and Matplotlib

   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:
