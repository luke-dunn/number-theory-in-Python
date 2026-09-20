from math import gcd
def totient_naive(n):
    return sum(1 for k in range(1, n) if gcd(k, n) == 1)
print(totient_naive(1024))
