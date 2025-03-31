# Results Summary - Options Pricing, Greeks, and Monte Carlo Simulation

## **Black-Scholes Model Results**
### Parameters:
- Stock Price (S): 100
- Strike Price (K): 100
- Risk-Free Rate (r): 5%
- Volatility (σ): 20%
- Time to Expiry (T): 1 year

| Metric         | Value    |
|--------------- |--------:|
| Call Price     | 10.4506 |
| Put Price      | 5.5735  |
| Put-Call Parity Check |  Holds True |

---

## **Greeks Calculations (at S = 100)**
| Greek      | Value   | Interpretation |
|----------- |--------:|---------------|
| Delta (Call) | 0.6368 | For $1 move in S, Call changes $0.6368 |
| Delta (Put)  | -0.3632 | For $1 move in S, Put changes -$0.3632 |
| Gamma        | 0.0188 | Sensitivity of Delta to S |
| Vega         | 37.5240 | Sensitivity to 1% change in Volatility |
| Theta (Call) | -6.4140 | Time decay per year |
| Theta (Put)  | -1.6579 | Time decay per year |
| Rho (Call)   | 53.2325 | Sensitivity to 1% change in r |
| Rho (Put)    | -41.8985 | Sensitivity to 1% change in r |

---

##  **Greeks Sensitivity Plots**
All plots saved in **/plots/** folder:
- `delta_plot.png`
- `gamma_plot.png`
- `vega_plot.png`
- `theta_plot.png`
- `rho_plot.png`

Observations:
- Delta increases with S
- Gamma peaks at ATM (S ≈ K)
- Vega highest at ATM
- Theta shows steep negative decay near expiry
- Rho is positive for Calls, negative for Puts

---

##  **Monte Carlo Simulation (100,000 Simulations)**
| Metric         | Value    |
|--------------- |--------:|
| Monte Carlo Call Price | 10.4365 |
| Monte Carlo Put Price  | 5.5712 |

 Monte Carlo results closely match Black-Scholes — confirming correctness.

---

##  **Key Takeaways:**
- Black-Scholes and Monte Carlo are aligned.
- Greeks help visualize risk sensitivities.
- Project demonstrates complete Options Pricing & Risk Analysis pipeline.

---

## **Next Step:** Portfolio Optimization / Efficient Frontier