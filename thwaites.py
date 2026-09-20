def thwa_visited(limit):
    seen = set()
    for x in range(2, limit):
        if x in seen:
            continue
        path = []
        n = x
        while n != 1 and n not in seen:
            path.append(n)
            n = n // 2 if n % 2 == 0 else 3 * n + 1
        seen.update(path)
    return seen
print(sorted(thwa_visited(100)))
