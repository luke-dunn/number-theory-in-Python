def t(n):
    return sum(range(1,n+1))


for x in range(1000000):
    digits = [int(i) for i in str(x)]
    trisum = sum(t(n) for n in digits)
    if x == trisum:
        print(x)
            
# i thought of this and I'm not getting any non-trivial results yet
# none exist! sum(T(digit)) is not large enough to cover any number with more than2 digits
