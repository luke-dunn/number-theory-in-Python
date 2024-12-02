"""
Prime Distribution Plotter in Fixed Intervals

This script calculates the number of prime numbers within fixed-length intervals and plots the results.
The goal is to explore how the distribution of prime numbers changes as we move through different ranges 
of integers.

Prime numbers are fundamental objects in number theory, but their distribution among natural numbers 
is somewhat irregular. This script aims to provide a visual representation of prime counts over evenly spaced 
intervals of length 'k'. By plotting the number of primes in each interval, you can observe trends or patterns 
in the density of primes over a given range of integers.

The interval size 'k' and the upper limit of the range can be adjusted to explore different ranges or intervals.

For k=100, the script plots the number of primes in intervals like [1, 100], [101, 200], ..., up to [2901, 3000].
"""
import matplotlib.pyplot as plt
from sympy import primerange

# Set a constant interval length
k = 100

# Initialize dictionary to hold prime counts
prime_counts = {}

# Calculate the number of primes in each interval [n, n+k]
for n in range(1, 3000, k):  # Adjust range as needed
    count = len(list(primerange(n, n + k)))  # More efficient prime counting
    prime_counts[n] = count

# Prepare data for plotting
n_values = list(prime_counts.keys())
prime_counts_values = list(prime_counts.values())

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(n_values, prime_counts_values, marker='o', linestyle='-', color='b')
plt.xlabel('Starting value of n')
plt.ylabel(f'Number of primes in [n, n+{k}]')
plt.title(f'Prime Count Distribution in Intervals of {k}')
plt.grid(True)
plt.show()
