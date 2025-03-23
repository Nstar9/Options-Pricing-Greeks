import numpy as np
from scipy.stats import norm
from bs_model import d1, d2

__all__ = [
    'delta_call', 'delta_put', 'gamma', 'vega',
    'theta_call', 'theta_put', 'rho_call', 'rho_put',
    'validate_greeks'
]

# Delta measures sensitivity to underlying price changes
def delta_call(S, K, r, sigma, T):
    return norm.cdf(d1(S, K, r, sigma, T))

def delta_put(S, K, r, sigma, T):
    return norm.cdf(d1(S, K, r, sigma, T)) - 1

# Gamma measures rate of change of delta
def gamma(S, K, r, sigma, T):
    d1_val = d1(S, K, r, sigma, T)
    return norm.pdf(d1_val) / (S * sigma * np.sqrt(T))

# Vega measures sensitivity to volatility
def vega(S, K, r, sigma, T):
    d1_val = d1(S, K, r, sigma, T)
    return S * norm.pdf(d1_val) * np.sqrt(T)

# Theta measures time decay of option price
def theta_call(S, K, r, sigma, T):
    d1_val, d2_val = d1(S, K, r, sigma, T), d2(S, K, r, sigma, T)
    term1 = - (S * norm.pdf(d1_val) * sigma) / (2 * np.sqrt(T))
    term2 = - r * K * np.exp(-r * T) * norm.cdf(d2_val)
    return term1 + term2

def theta_put(S, K, r, sigma, T):
    d1_val, d2_val = d1(S, K, r, sigma, T), d2(S, K, r, sigma, T)
    term1 = - (S * norm.pdf(d1_val) * sigma) / (2 * np.sqrt(T))
    term2 = r * K * np.exp(-r * T) * norm.cdf(-d2_val)
    return term1 + term2

# Rho measures sensitivity to interest rate changes
def rho_call(S, K, r, sigma, T):
    d2_val = d2(S, K, r, sigma, T)
    return K * T * np.exp(-r * T) * norm.cdf(d2_val)

def rho_put(S, K, r, sigma, T):
    d2_val = d2(S, K, r, sigma, T)
    return -K * T * np.exp(-r * T) * norm.cdf(-d2_val)

# Test function to validate Greeks calculation
def validate_greeks(S=100, K=100, r=0.05, sigma=0.2, T=1):
    print("\n--- Greeks Validation ---")
    print(f"Delta (Call): {delta_call(S, K, r, sigma, T):.4f}")
    print(f"Delta (Put): {delta_put(S, K, r, sigma, T):.4f}")
    print(f"Gamma: {gamma(S, K, r, sigma, T):.4f}")
    print(f"Vega: {vega(S, K, r, sigma, T):.4f}")
    print(f"Theta (Call): {theta_call(S, K, r, sigma, T):.4f}")
    print(f"Theta (Put): {theta_put(S, K, r, sigma, T):.4f}")
    print(f"Rho (Call): {rho_call(S, K, r, sigma, T):.4f}")
    print(f"Rho (Put): {rho_put(S, K, r, sigma, T):.4f}")

if __name__ == "__main__":
    validate_greeks()
