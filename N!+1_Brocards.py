def f(x):
    if x ==1:
        return 1
    else:
        return x*f(x-1)

for z in range(1,20):
    print((f(z)+1)**0.5)
