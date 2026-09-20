
from sympy import isprime
##for z in range(15):
##    for x in range(z):
##        w = z**3-x**3
##        print(z,x,w,isprime(w))

# when z=x+1 results look like  w is prime
# using difference of cubes
# (z-x)(z^2+zx+x^2)
# for z = x+1 this gives
# w = 3x^2 + 3x + 1
# it's not universal but for small x many of these are indeed prime
# first counterexample is 6,5 -> 91 = 7 x 13

# to clarify just check the candidates

for x in range(50):
    quad = 3*x**2 + 3*x + 1
    print(x,quad, isprime(quad))
