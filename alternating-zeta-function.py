"""the alternating zeta function converges to pi^2/12"""
from math import pow, pi
from matplotlib import pyplot as plt

# Define the zeta function for s = 2
def zeta_2(x):
    return sum([(-1)**(n-1)*(1/pow(n,2)) for n in range(1,x+1)])

# Generate the range of x values
x = range(1, 40)

# Compute the zeta function for each value of x
y = [zeta_2(z) for z in x]

# Print the last value to check the result
print(f"Sum with {x[-1]} terms: {y[-1]}")

# Plot the results
plt.plot(x, y, label="Zeta Function Series")

# Add the asymptote line for pi^2/12
asymptote_value = pi**2 / 12
plt.axhline(y=asymptote_value, color='r', linestyle='--', label=f"Asymptote: $\\frac{{\\pi^2}}{{12}} \\approx {asymptote_value:.4f}$")

# Add labels and grid
plt.xlabel("Number of Terms")
plt.ylabel("Sum of Series")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
