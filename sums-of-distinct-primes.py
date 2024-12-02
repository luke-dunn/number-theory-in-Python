from itertools import combinations
from sympy import primerange

# Generate a list of prime numbers up to 1000 using the primerange function
primes = list(primerange(2, 1000))

# Create a list of all unique pairs of primes using itertools.combinations
pairs_of_primes = list(combinations(primes, 2))

# Initialize a dictionary to store sums of prime pairs as keys and the corresponding pairs as values
sums_dict = {}

# Populate the sums_dict with the pairs that have the same sum
for pair in pairs_of_primes:
    sum_of_pair = sum(pair)
    if sum_of_pair not in sums_dict:
        sums_dict[sum_of_pair] = []
    sums_dict[sum_of_pair].append(pair)

# Print the first 20 even numbers that can be represented as the sum of two distinct primes
print(sorted(sums_dict.keys())[:20])

# Find sums that can be formed in many ways (i.e., sums with more than 50 pairs)
for z in sums_dict:
    if len(sums_dict[z]) > 50:
        print(z, sums_dict[z])

# Create a set of sums of two distinct primes
sum_of_primes = set(sums_dict.keys())

# Create a list to store numbers that cannot be represented as the sum of two distinct primes
cants = []

# Check numbers from 2 to 100
for x in range(2, 100):
    if x not in sum_of_primes:
        cants.append(x)

# Print the first 100 numbers that cannot be represented as the sum of two distinct primes
print(cants)

# These numbers match the sequence A166081 on the OEIS
