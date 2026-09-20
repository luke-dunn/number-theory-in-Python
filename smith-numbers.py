#  I have this code
from sympy import factorint

def sumf(n):
    return sum(
        sum(map(int, str(p))) * exponent
        for p, exponent in factorint(n).items()
    )

for n in range(4, 1000):
    if not factorint(n) == {n: 1}:  # exclude primes
        if sum(map(int, str(n))) == sumf(n):
            print(n)
