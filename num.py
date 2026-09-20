# most useful basic number theoretical functions
# add to this reliable way to getsizeof
# need numpy and pympler in addition to basic python install
# asizeof has been useful in making various processes use up
# as much of my workstations ram, proc etc as possible

from pympler import asizeof
from numpy import array
from itertools import combinations_with_replacement as rep
from pprint import pprint
from array import array as a1
from math import prod
from time import time
from sympy import isprime

def size(x):
    s=asizeof.asizeof(x)
    return str(s)+' bytes, '+ str((s/(1073741824*16))*100)+' % of total RAM' #I have 16GB

def factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def primorial(n):
    a=1
    for x in prime_sieve(n+1):
        if x<=n:
            a*=x
        else:
            break
    return a


def prime_sieve(max1):
    candidates = set(range(3, max1, 2))
    for factor in range(3, int(max1 ** 0.5) + 1, 2):
        for multiple in range(factor ** 2, max1, factor * 2):
            candidates.discard(multiple)
    return a1('I',[2])+a1('I',candidates)

def gcd(a,b):
    """Euclid's algorithm for gcd"""
    while b!= 0:
        t = b
        b = a % b
        a = t
    return a


def prim(x):
    """fermat primality test for 1<a<x"""
    z=[]
    for y in range(x):
        if gcd(x,y)==1:
            z.append((y**(x-1))%x)
    return z

def mean(a):
    """arithmetic mean"""
    if not a:
        return 0
    return sum(a)/len(a)

def fac_rec(x):
    """recursive factorial function"""
    if x<=1:
        return 1
    else:
        return x * fac(x-1)

def fac(x):
    """faster factorial just using loop"""
    a=1
    for z in range(2,x+1):
        a*=z
    return a

def choose(x,y):
    """combinatorial x choose y function"""
    return int(fac(x)/(fac(x-y)*fac(y)))

def permute(x,y):
    """combinatorial x permute y function"""
    return int(fac(x)/(fac(x-y)))

def partitions(n, I=1):
    """integer partitions"""
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p


