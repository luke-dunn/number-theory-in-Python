from math import factorial as fa
def taylorsin(x,n):
    tot=0
    for z in range(n):
        tot+=(-1)**z * x**(2*z + 1) / fa(2*z+1)
    return tot
pi=3.14159265
print(10*taylorsin(pi/10,10))
