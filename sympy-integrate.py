from sympy import symbols, integrate, pprint, Integral

x = symbols('x')
expr = 2 * x * (x**2 + 1)**3
result = integrate(expr, x)
print(result)

pprint(Integral(expr, x).doit(), use_unicode=True)
