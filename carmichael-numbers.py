from sympy import isprime, primerange
from math import gcd

def fermat(candidate, base):
    """Perform Fermat's test for base on candidate."""
    return pow(base, candidate - 1, candidate) == 1


def is_carmichael_candidate(number):
    """Check if a number is a Carmichael candidate by testing Fermat's theorem for all coprime bases."""
    if isprime(number):  # Carmichael numbers are composite
        return False
    # Test Fermat's Little Theorem for all coprime bases < number
    for base in range(2, number):
        if gcd(base, number) == 1:  # Only test if the base is coprime to the number
            if not fermat(number, base):
                return False
    return True

max_value =100000
primes = set(primerange(2, max_value))  # Generate primes up to 1000 and convert to a set

carms = []
for z in range(2, max_value):
    if is_carmichael_candidate(z):
        carms.append(z)  # Compile list of Fermat pseudoprimes

# Using set methods to get the difference between pseudoprimes and true primes
carmichael_numbers = set(carms).difference(primes)
print(sorted(list(carmichael_numbers)))
