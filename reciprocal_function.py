from math import log


delta = 0.001
start = 1
end = 20

tot = 0

for i in range(int((end - start) / delta)):
    x1 = start + i * delta
    x2 = start + (i + 1) * delta

    y1 = 1 / x1
    y2 = 1 / x2

    tot += ((y1 + y2) / 2) * delta

print(tot)
print(log(20))
