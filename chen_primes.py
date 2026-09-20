from sympy import primerange, isprime, factorint

a = []
for p in primerange(1000):
    q = p + 2
    if isprime(q):
        a.append(p)
    else:
        factors = factorint(q)
        total_exponents = sum(factors.values())  # count prime factors with multiplicity
        if len(factors) >= 1 and total_exponents == 2:
            a.append(p)
print(a)
