import numpy as np
from scipy.stats import norm

__all__ = ['d1', 'd2', 'bs_call_price', 'bs_put_price', 'validate_bs_model']

def d1(S, K, r, sigma, T):
    """
    Calculate d1 from the Black-Scholes formula.
    """
    return (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

def d2(S, K, r, sigma, T):
    """
    Calculate d2 from the Black-Scholes formula.
    """
    return d1(S, K, r, sigma, T) - sigma * np.sqrt(T)

def bs_call_price(S, K, r, sigma, T):
    """
    Calculate Black-Scholes price for a European call option.
    """
    if T <= 0:
        return max(0, S - K)  # Option expired
    if sigma <= 0:
        raise ValueError("Volatility must be positive.")
    
    d1_val, d2_val = d1(S, K, r, sigma, T), d2(S, K, r, sigma, T)
    return S * norm.cdf(d1_val) - K * np.exp(-r * T) * norm.cdf(d2_val)

def bs_put_price(S, K, r, sigma, T):
    """
    Calculate Black-Scholes price for a European put option.
    """
    if T <= 0:
        return max(0, K - S)  # Option expired
    if sigma <= 0:
        raise ValueError("Volatility must be positive.")
    
    d1_val, d2_val = d1(S, K, r, sigma, T), d2(S, K, r, sigma, T)
    return K * np.exp(-r * T) * norm.cdf(-d2_val) - S * norm.cdf(-d1_val)

def validate_bs_model(S=100, K=100, r=0.05, sigma=0.2, T=1):
    """
    Validate the Black-Scholes model with sample input.
    Returns computed call price, put price, and put-call parity check.
    """
    call_price = bs_call_price(S, K, r, sigma, T)
    put_price = bs_put_price(S, K, r, sigma, T)
    parity_diff = call_price - put_price
    parity_check = S - K * np.exp(-r * T)

    print(f"Black-Scholes Model Validation:")
    print(f"Parameters: S={S}, K={K}, r={r}, sigma={sigma}, T={T}")
    print(f"Call Price: {call_price:.4f}")
    print(f"Put Price: {put_price:.4f}")
    print(f"Put-Call Parity Check: {parity_diff:.4f} ≈ {parity_check:.4f}")

    return call_price, put_price, parity_diff, parity_check

if __name__ == "__main__":
    validate_bs_model()
