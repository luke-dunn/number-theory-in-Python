"""The harmonic series is known to diverge as it tends to infinity,
here we examine the sum that is created by alternately adding and subtracting
the terms of the harmonic sequence"""

from math import log
from matplotlib import pyplot as plt


def s(x):
    return sum([(-1)**(n-1)*(1/n) for n in range(1,x)])
x=range(1,100)
y=[s(z) for z in x]
print(y[-1])

ln2=log(2)

plt.plot(x, y)

plt.axhline(y=ln2, color='r', linestyle='--', label='Asymptote at ln(2) ~0.693')

plt.title("Convergence of the Alternating Harmonic Series")
plt.xlabel("Number of Terms")
plt.ylabel("Sum of Series")
plt.grid(True)
plt.legend(loc='lower right')
plt.show()
