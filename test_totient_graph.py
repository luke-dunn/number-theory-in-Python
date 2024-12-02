import matplotlib.pyplot as plt
from sympy import totient

# Define the range of n values you want to explore
n_values = list(range(1, 401))  # For example, n from 1 to 100

# Calculate phi(n) for each n in the range
phi_values = [totient(n) for n in n_values]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, phi_values, marker='o', linestyle='-', color='blue')

# Adding titles and labels
plt.title("Distribution of Euler's Totient Function phi(n)", fontsize=16)
plt.xlabel("n", fontsize=14)
plt.ylabel("phi(n)", fontsize=14)
plt.grid(True)

# Show the plot
plt.show()
