# estimate phi with minimum storage required

from math import sqrt

a, b = 0, 1

for _ in range(40):
    a, b = b, a + b
    
print('phi estimate:   ',b/a)
print('phi actual:     ',(sqrt(5)+1)/2)
