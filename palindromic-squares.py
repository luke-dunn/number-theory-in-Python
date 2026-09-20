from math import isqrt

def ispalin(x):
    return str(x) == str(x)[::-1]

def issq(x):
    z=isqrt(x)
    return z*z==x

pls = [(x, isqrt(x)) for x in range(1000000) if ispalin(x) and issq(x)]

print(pls)
