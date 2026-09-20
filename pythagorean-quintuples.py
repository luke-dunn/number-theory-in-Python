from functools import reduce
from math import gcd, isqrt

# generate primitive pythagorean quintuples

for i in range(1, 15):
    for j in range(1, i):
        for k in range(1,j):
            for l in range(1,k):
                c_squared = i**2 + j**2 + k**2 +l**2
                c = isqrt(c_squared)  # Faster and exact integer sqrt
                if c * c == c_squared:  # Perfect square check
                    if reduce(gcd, (i, j, k, l, c)) == 1:
                        print(l, k, j, i, c)
