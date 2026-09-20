# product of non-zero digits
def prod(x):
    a=1
    for z in x:
        if z:
            a*=z
    return a

for a in range(100):
    seen = []
    x=a
    while x not in seen:
        seen.append(x)
        digits = [int(d) for d in str(x)]
        x=sum(digits) * prod(digits)
    print(a, seen, "cycle entry:", x)

