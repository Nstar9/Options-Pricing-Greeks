import numpy as np
import matplotlib.pyplot as plt
from greeks_calculator import delta_call, gamma, vega, theta_call, rho_call

# Parameters
K = 100         # Strike price
r = 0.05        # Risk-free rate
sigma = 0.2     # Volatility
T = 1           # Time to maturity

# Stock price range
stock_prices = np.linspace(50, 150, 100)

# Compute Greeks
delta_vals = [delta_call(S, K, r, sigma, T) for S in stock_prices]
gamma_vals = [gamma(S, K, r, sigma, T) for S in stock_prices]
vega_vals  = [vega(S, K, r, sigma, T) for S in stock_prices]
theta_vals = [theta_call(S, K, r, sigma, T) for S in stock_prices]
rho_vals   = [rho_call(S, K, r, sigma, T) for S in stock_prices]

# Save plots
def plot_and_save(x, y, greek_name):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=greek_name, linewidth=2)
    plt.xlabel('Stock Price (S)')
    plt.ylabel(f'{greek_name}')
    plt.title(f'{greek_name} vs Stock Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'plots/{greek_name.lower()}_plot.png')
    plt.close()

# Generate and save all Greek plots
plot_and_save(stock_prices, delta_vals, 'Delta')
plot_and_save(stock_prices, gamma_vals, 'Gamma')
plot_and_save(stock_prices, vega_vals, 'Vega')
plot_and_save(stock_prices, theta_vals, 'Theta')
plot_and_save(stock_prices, rho_vals, 'Rho')

print(" All Greeks plots generated and saved inside /plots folder.")