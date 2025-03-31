import numpy as np

def monte_carlo_call_price(S, K, r, sigma, T, simulations=100000):
    """
    Monte Carlo simulation to estimate the European Call Option price.

    Parameters:
    S (float): Current stock price
    K (float): Strike price
    r (float): Risk-free interest rate
    sigma (float): Volatility of the underlying asset
    T (float): Time to expiration (in years)
    simulations (int): Number of Monte Carlo paths

    Returns:
    float: Estimated Call option price
    """
    np.random.seed(42)  # For reproducibility
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(ST - K, 0)
    call_price = np.exp(-r * T) * np.mean(payoff)
    return call_price

def monte_carlo_put_price(S, K, r, sigma, T, simulations=100000):
    """
    Monte Carlo simulation to estimate the European Put Option price.
    """
    np.random.seed(42)
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(K - ST, 0)
    put_price = np.exp(-r * T) * np.mean(payoff)
    return put_price

def validate_monte_carlo():
    S = 100
    K = 100
    r = 0.05
    sigma = 0.2
    T = 1
    simulations = 100000

    call_mc = monte_carlo_call_price(S, K, r, sigma, T, simulations)
    put_mc = monte_carlo_put_price(S, K, r, sigma, T, simulations)

    print("\n--- Monte Carlo Simulation ---")
    print(f"Simulations: {simulations}")
    print(f"Monte Carlo Call Price: {call_mc:.4f}")
    print(f"Monte Carlo Put Price: {put_mc:.4f}")

if __name__ == "__main__":
    validate_monte_carlo()