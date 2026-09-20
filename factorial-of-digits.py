from sympy import factorial as f

def facsum(x):
    return sum(f(int(i)) for i in str(x))

cycle_169 = {169, 363601, 1454}

for a in range(100000):
    seen = []
    x=a
    while x not in seen:
        seen.append(x)
        x = facsum(x)


    if x not in cycle_169:
        print(a, seen, "cycle entry:", x)
