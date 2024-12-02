from fractions import Fraction
from sympy import primerange

# Initializing the list to store the sum of fractions
fractions_list = []

# Looping through a range to sum fractions with prime denominators
for z in range(1, 25):
    # Generating prime numbers up to 1000
    pr = iter(primerange(1,1000))

    # Starting with a Fraction of 0
    a = Fraction(0)

    # Summing fractions with prime denominators
    for y in range(z):
        # Each fraction has 1 as the numerator and a prime number as the denominator
        a += Fraction(1, next(pr))

    # Appending the resulting fraction to the list
    fractions_list.append(a)

# Displaying the list of fractions
for idx, frac in enumerate(fractions_list, 1):
    print(f"Sum of the first {idx} fractions: {frac}")

# Note:
# This code illustrates the sum of fractions with prime number denominators.
# The series is known to diverge, as the sum of the reciprocals of primes diverges.
# Each fraction is of the form 1/prime, and as more terms are added, the numerators
# represent the count of these reciprocals, which grows without bound.
