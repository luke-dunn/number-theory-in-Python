from math import log


delta = 0.0001
start = 0
end = 1

tot = 0

for i in range(1,int((end - start) / delta)):
    x1 = start + i * delta
    x2 = start + (i + 1) * delta

    y1 = log(x1)
    y2 = log(x2)

    tot += ((y1 + y2) / 2) * delta

print(tot)

# converge to -1
