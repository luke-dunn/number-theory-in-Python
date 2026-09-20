from sympy.utilities.iterables import partitions

def restricted_partition_count(n):
    result = {}
    for k in range(1, n + 1):
        count = 0
        for p in partitions(n):
            total_parts = sum(p.values())  # Sum of multiplicities
            if total_parts == k:
                count += 1
        result[k] = count
    return result

n = 10
counts = restricted_partition_count(n)

for k, count in counts.items():
    print(f"Partitions of {n} into exactly {k} parts: {count}")
