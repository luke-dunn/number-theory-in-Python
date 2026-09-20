from math import gcd

def phi(n):
    """Compute Euler's totient function φ(n)"""
    count = 0
    for k in range(1, n + 1):
        if gcd(k, n) == 1:
            count += 1
    return count

def primitive_roots_with_cycles(mod):
    from math import gcd

    def power_cycle(a, mod):
        seen = []
        val = 1
        for _ in range(1, mod):
            val = (val * a) % mod
            seen.append(val)
            if val == 1:
                break
        return seen

    def is_primitive_root(a, mod):
        cycle = power_cycle(a, mod)
        return len(cycle) == phi(mod)

    results = []
    for a in range(2, mod):
        if gcd(a, mod) == 1 and is_primitive_root(a, mod):
            results.append((a, power_cycle(a, mod)))
    return results

# Example usage
#mod = 10

for mod in range(2,20):
    for root, cycle in primitive_roots_with_cycles(mod):
        print(f"Primitive root {root} mod {mod}: {cycle}")
