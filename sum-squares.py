"""looking at numbers that can be expressed as a sum of
distinct squares in the most ways"""
from itertools import combinations

# Create a list of numbers from 0 to 999 (inclusive)

numbers = list(range(1000))

# Initialize a dictionary to store sums of squares and their
# corresponding pairs of numbers.
# Calculate the sum of squares for all pairs of numbers and
# add them to the sums_dict as keys using a dictionary comprehension

sums_dict = {x**2 + y**2: [] for x, y in combinations(numbers, 2)}

# Calculate the sum of squares for all pairs of numbers again.
# This time, append the corresponding pairs of numbers to the
# sums_dict for each sum of squares key.

for x, y in combinations(numbers, 2):
    sumsq = x ** 2 + y ** 2
    # Append the current pair (x, y) to the list
    # associated with the sum of squares key.
    sums_dict[sumsq].append((x, y))

# Find the sum of squares that has the largest number of associated pairs.
# Store the number of associated pairs and the corresponding sum
# of squares in the variable most_ways.

most_ways = max([(len(sums_dict[w]), w) for w in sums_dict])

# Print the result, which is the number that can be expressed
# as a sum of distinct squares in the largest number of ways.

print(most_ways)  # Output: (16, 801125)

# Print the first 50 numbers that can be expressed as the sum of
# two distinct squares.

print(sorted(sums_dict)[0:50])
