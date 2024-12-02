"""this is a more pythonic way to explore the taxi number and its relatives"""
from itertools import combinations
from collections import Counter

def sum_of_cubes(pair):
    """Calculate the sum of cubes of a pair of numbers."""
    return pair[0] ** 3 + pair[1] ** 3

# Generating a list of numbers
a = [x for x in range(1, 1000)]

# Creating combinations of these numbers
b = combinations(a, 2)

# Applying the sum of cubes function to each combination using map
c = map(sum_of_cubes, b)

# Counting the occurrences of each sum with Counter
res = Counter(c)

print(res.most_common(10))

# [(1729, 2), (4104, 2), (13832, 2), (39312, 2), (704977, 2)]
# Ramanujan's Taxi number and some more examples of numbers
# that can be expressed as sums of cubes in more than 1 way
