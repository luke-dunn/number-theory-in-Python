from functools import reduce
from math import gcd, isqrt

# generate primitive pythagorean quadruples

for i in range(1, 10):
    for j in range(1, i):
        for k in range(1,j):
            c_squared = i**2 + j**2 + k**2
            c = isqrt(c_squared)  # Faster and exact integer sqrt
            if c * c == c_squared:  # Perfect square check
                if reduce(gcd, (i, j, k, c)) == 1:
                    print(k, j, i, c)
