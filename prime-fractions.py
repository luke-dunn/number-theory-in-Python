"""
generate a list of prime numbers up to a limit and calculate
the ratios between consecutive primes. plot the ratios to visualize how they
approach 1 as the primes increase.

The ratios of consecutive primes converge very quickly toward 1, which can be observed
in the plot, indicating that the relative difference between consecutive primes becomes
smaller as the primes grow larger.
"""

from sympy import primerange
import matplotlib.pyplot as plt

# Generate list of primes
primes = [x for x in primerange(1, 10000)]

# Calculate the ratios of consecutive primes
fracs = [primes[i] / primes[i + 1] for i in range(len(primes) - 1)]

# Plot the ratios
plt.figure(figsize=(10, 6))
plt.plot(fracs, label='Consecutive Prime Ratios')
plt.axhline(y=1, color='r', linestyle='--', label='y=1 (Asymptote)')
plt.xlabel("Index of consecutive prime pairs")
plt.ylabel("Prime Ratio (p_i / p_{i+1})")
plt.title("Ratios of Consecutive Primes")
plt.legend()
plt.grid(True)
plt.show()
