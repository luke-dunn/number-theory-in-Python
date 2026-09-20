from sympy import symbols
from sympy.solvers.diophantine import diophantine

w, x, y, z = symbols('w x y z', integer=True)

a = diophantine(w**3 + x**3 + y**3 - z**3)
print(a)
