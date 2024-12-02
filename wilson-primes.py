from sympy import primerange, factorial

def wilson_primes(ubound):
    """find wilson primes of the sort where n**2 divides (n-1)!+1"""
    primes=primerange(2,ubound)
    results=[]
    for z in primes:
        if (factorial(z-1)+1)%(z**2)==0:
            results.append(z)
    return results

print(wilson_primes(20000))

# output:

# [5, 13, 563]

# actually these are the only ones known, although it is thought there are many
# more once the numbers get big. Not much point in me searching on a machine
# of this kind of power.

# this sequence is A007540 @ OEIS
