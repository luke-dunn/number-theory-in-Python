from functools import reduce
from math import gcd, isqrt

# generate primitive pythagorean triples
a=[]
for i in range(1, 5000):
    for j in range(1, i):
        c_squared = i**2 + j**2
        c = isqrt(c_squared)  # Faster and exact integer sqrt
        if c * c == c_squared:  # Perfect square check
            if reduce(gcd, (i, j, c)) == 1:
                a.append((j,i,c))


for x in sorted(a):
    print(x)
