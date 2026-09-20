def is_primitive_root(r, k):
    residues = []
    seen = set()
    for i in range(1, k):
        val = pow(r, i, k)
        if val in seen:
            return (residues, False)  # duplicate found before full cycle
        residues.append(val)
        seen.add(val)
    return (residues, len(residues) == k - 1)

for z in range(23,24):
    print("testing", z)
    for j in range(1, z):
        result = is_primitive_root(j, z)
        print(f"{j}: {result}")
    print()
