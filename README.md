
# Options Pricing, Greeks Calculator & Monte Carlo Simulation

## Project Overview

This project implements the pricing of European call and put options using the Black-Scholes Model, analyzes how different "Greeks" change with stock price, and simulates option pricing using the Monte Carlo method.

If you're new to options or financial engineering, this project walks through everything from the foundational Black-Scholes formulas to visualizing risk sensitivities.

---

## Contents

- `bs_model.py`: Black-Scholes formula implementation for European call and put options.
- `greeks_calculator.py`: Functions to compute the Greeks (Delta, Gamma, Vega, Theta, Rho).
- `plot_greek.py`: Generates plots for each Greek as stock price varies.
- `monte_carlo.py`: Monte Carlo simulation to estimate call and put option prices.
- `plots/`: Folder containing all saved Greek plots.
- `results_summary.md`: Summary of results and outputs with interpretations.
- `README.md`: You're reading it.

---

## Black-Scholes Model

The **Black-Scholes model** provides a theoretical estimate of the price of European-style options.

The formulas are:

### Call Option Price:

C = S * N(d1) - K * e^(-rT) * N(d2)

### Put Option Price:

P = K * e^(-rT) * N(-d2) - S * N(-d1)

Where:
- `S` = Current stock price  
- `K` = Strike price  
- `T` = Time to expiration (in years)  
- `r` = Risk-free interest rate  
- `σ` = Volatility of the stock  
- `N()` = Standard normal cumulative distribution  
- `d1 = [ln(S/K) + (r + σ² / 2) * T] / (σ * sqrt(T))`  
- `d2 = d1 - σ * sqrt(T)`

We have implemented these formulas in `bs_model.py`, including logic for edge cases such as expiry time being 0 or volatility being 0.

---

## Greeks Calculation

Greeks measure how sensitive the option price is to various factors:

- **Delta**: Measures how the option price changes with a change in the stock price.
- **Gamma**: Measures how Delta changes with the stock price.
- **Vega**: Measures sensitivity to volatility.
- **Theta**: Measures sensitivity to time decay.
- **Rho**: Measures sensitivity to changes in interest rate.

These are calculated analytically using the formulas derived from the Black-Scholes partial derivatives.

Each Greek is implemented in `greeks_calculator.py`.

---

## Greek Sensitivity Plots

Using `plot_greek.py`, we plotted how each Greek changes with respect to stock price while keeping strike price, volatility, time, and interest rate fixed.

The following plots are generated and saved in the `plots/` directory:
- `delta_plot.png`
- `gamma_plot.png`
- `vega_plot.png`
- `theta_plot.png`
- `rho_plot.png`

These are useful to visualize how option sensitivities behave around different stock prices.

---

## Monte Carlo Simulation

The Monte Carlo method is a probabilistic way of estimating the expected payoff of an option by simulating a large number of possible future stock prices.

The steps are:
1. Generate random paths for stock prices at expiration.
2. Compute payoff of call/put option at each path.
3. Discount the average payoff to present value.

We implemented this in `monte_carlo.py`, and compared the results to Black-Scholes. With a high number of simulations, both converge closely.

---

## How to Run

1. Install dependencies:
```bash
pip install numpy scipy matplotlib

	2.	Run Black-Scholes model:

python bs_model.py

	3.	Run Greeks calculation:

python greeks_calculator.py

	4.	Plot Greeks:

mkdir plots  # Run this once if the folder doesn't exist
python plot_greek.py

	5.	Run Monte Carlo simulation:

python monte_carlo.py



⸻

Why This Project Matters

This project isn’t just about implementing formulas. It’s about building an intuition for how options behave, how risk is measured, and how numerical techniques like Monte Carlo help when analytical models fall short.

Whether you’re preparing for a quant interview, exploring financial engineering, or building a portfolio of practical data science projects — this project gives you both the math and the code.

⸻

License

This project is open-source under the MIT license. Use it, modify it, and learn from it.

