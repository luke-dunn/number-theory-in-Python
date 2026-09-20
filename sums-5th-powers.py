from collections import defaultdict

a = defaultdict(list)

for x in range(300):
    for y in range(x):
        for z in range(y):
            tot=x**5+y**5+z**5
            a[tot].append((x,y,z))

for x in a:
    if len(a[x])>1:
        print (x,a[x])
        break

# 1375298099 [(62, 54, 3), (67, 28, 24)]

