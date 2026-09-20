from collections import defaultdict
ans = defaultdict(list)
def tri(x):
    return x*(x-1)//2
t = [tri(x) for x in range(2,100)]

for i, x in enumerate(t):
    for y in t[:i]:
        z = x + y
        ans[z].append((x, y))
q = 1

for s in sorted(ans):
    if len(ans[s]) > q:
        print(s, ans[s])
        q = len(ans[s])
