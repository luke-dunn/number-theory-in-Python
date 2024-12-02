from sympy import primerange
from itertools import combinations_with_replacement

# Find numbers that can be expressed as sums of two primes in the maximum number of different ways.
# Connected to the Goldbach Conjecture.

# Get the upper bound for the prime sieve
upper_bound = input('Enter the upper bound for the prime sieve: ')
print()

# Convert the input to an integer
bound = int(upper_bound)

# Generate a list of prime numbers using the prime sieve
primes = list(primerange(2, bound))  # Generate primes from 2 to the upper bound

# Generate a list of all possible pairs of primes, repetition allowed
sums = list(combinations_with_replacement(primes, 2))

# Create a dictionary to store the sums as keys and an empty list as values
sum_dict = {}
for pair in sums:
    total = sum(pair)
    if total not in sum_dict:
        sum_dict[total] = []
    sum_dict[total].append(pair)

# Create a dictionary to store the number of ways as keys and an empty list as values
ways_dict = {}
for total in sum_dict:
    num_ways = len(sum_dict[total])
    if num_ways not in ways_dict:
        ways_dict[num_ways] = []
    ways_dict[num_ways].append([total, sum_dict[total]])

# Find the largest number of ways
largest_num_ways = max(ways_dict.keys())

# Get the list of sums with the largest number of ways
answer = ways_dict[largest_num_ways]

# Print the result
print("The number", answer[0][0], "can be expressed as a sum of two primes in", largest_num_ways, "ways.")
print()

# Ask the user if they want to see all the ways
show_ways = input('Would you like to see all the ways? (y/n) ')
print()
if show_ways.lower() == 'y':
    for val in answer[0][1]:
        print(val)
