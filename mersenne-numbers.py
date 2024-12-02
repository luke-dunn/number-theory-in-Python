"""
Mersenne speculated that numbers of the form 2^n - 1 are often prime.
Although Mersenne did not have computer assistance, his work laid the foundation
for the study of these primes. M31 = 2147483647 was later discovered to be prime
by Leonhard Euler in 1772.
"""

"""

from sympy import isprime

for x in range(1, 50):
    mersenne = 2**x - 1
    if isprime(mersenne):
        print(f"M{x} = {mersenne} is prime")
    else:
        print(f"M{x} = {mersenne} is composite")
