def in_base(n, b):
    digits = []
    while True:
        digits.append(str(n % b))
        n //= b
        if n == 0:
            break
    return ''.join(digits[::-1])

def ispal(s):
    return s == s[::-1]

for n in range(1, 200):
    count = 0
    for b in range(2, 11):
        if ispal(in_base(n, b)):
            count += 1
    if count >= 4:
        print(n, count)
