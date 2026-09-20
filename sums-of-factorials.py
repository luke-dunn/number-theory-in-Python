from collections import defaultdict
from sympy import factorial as f

a = defaultdict(list)
facts = [f(n) for n in range(400)]
for x in range(400):
    for y in range(1,x):
        tot = facts[x] + facts[y] 
        a[tot].append((x,y))

for x in a:
    if len(a[x])>1:
        print (x,a[x])
        break

# trying this now

# output
# 9 [(3, 2, 0), (3, 2, 1)]

