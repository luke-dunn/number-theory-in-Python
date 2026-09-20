from math import sin, exp
import matplotlib.pyplot as plt

##x = 3
##values = []
##
##for _ in range(50):
##    values.append(x)
##    x = sin(exp(x))
##
##plt.plot(values)
##plt.xlabel("iteration")
##plt.ylabel("x")
##plt.show()

x = 3
xs = []
ys = []

for _ in range(50):
    x_next = sin(exp(x))
    xs.append(x)
    ys.append(x_next)
    x = x_next

plt.scatter(xs, ys)
plt.xlabel("x_n")
plt.ylabel("x_{n+1}")
plt.show()
