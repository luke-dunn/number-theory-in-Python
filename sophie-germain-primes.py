from sympy import primerange, isprime

# Sophie Germain primes are primes, p,  where 2*p+1 is also prime
# You can see that 2,3,5,11 are but clearly 7, 13 are not.
# It is not proven that there are an infinite number of these.


# Generate a list of primes up to a certain number
a = list(primerange(2, 10000))

# Find Sophie Germain primes
b = [p for p in a if isprime(2 * p + 1)]

print(b[:10], len(b))

# [2, 3, 5, 11, 23, 29, 41, 53, 83, 89],  190
# this is A005384 @ OEIS
