# test taylor series for f(x) = sin(x)

from math import pi, factorial

def sin1(x,lim):
    return sum([((-1)**n)*(x**(2*n+1)/factorial(2*n+1)) for n in range(lim)])
limit = 20
print(1/sin1(pi/4,limit)**2)

# output should be very near 2 because sin(pi/4) = 1/root2
