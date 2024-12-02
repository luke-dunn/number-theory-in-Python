# the harmonic numbers are the partial sums to n of the
# harmonic sequence here we show them as fractions

from fractions import Fraction
def su(x):
    a=Fraction(0)
    for z in range(1,x):
        a+=Fraction(1,z)
    return a

for n in range(1,20):
    print(su(n),end=', ')
