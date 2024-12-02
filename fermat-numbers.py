from sympy import isprime, primefactors

for z in range(20):
    fermat = 2**(2**z) + 1
    if isprime(fermat):
        print(f"2**(2**{z}) + 1 is prime")
    else:
        print(f"2**(2**{z}) + 1 has factors:", primefactors(fermat))

# Fermat numbers take the form 2^2^n+1, some are prime, some not
