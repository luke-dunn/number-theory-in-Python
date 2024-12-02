# Find Poulet numbers, which are composites that the 'Fermat test'
# lies about and says are prime for base-2
# sequence A001567 in the OEIS
# note Poulet was a French, self-taught mathematician
# he also discovered sociable numbers

from sympy import isprime

def isfermat(x, base):
    """This function simply uses Fermat's little theorem
    to provide a prime candidate. One says 'candidate'
    because it can sometimes be wrong about primality."""
    return pow(base, x-1, x) == 1


for x in range(2,100000):
     if isfermat(x,2) and not isprime(x):
        print(x)

# first few are 341, 561, 645, 1105, 1387, 1729, 1905, 2047, 2465, 2701...
