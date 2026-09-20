from cmath import sin, exp
import matplotlib.pyplot as plt

z =2.5 + 2j   # try different starts
xs = []
ys = []

for n in range(100):
    xs.append(z.real)
    ys.append(z.imag)
    
    if n % 2:
        z = sin(z)
    else:
        z = exp(z)

plt.plot(xs, ys, marker='o')
plt.xlabel("Re")
plt.ylabel("Im")
plt.title("Complex iteration")
plt.show()
