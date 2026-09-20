from sympy import gcd

def z(y):
    return [x for x in range(1,y) if gcd(x,y)==1]
