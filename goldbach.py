def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

from itertools import product

def prime_pairs(primes):
    return list(product(primes, repeat=2))

def goldbach_pairs(prime_list, target):
    return [(a, b) for (a, b) in product(prime_list, repeat=2) if a + b == target]

def goldbach_counts(n):
    primes = primes_up_to(n)
    even_counts = {}
    for even in range(4, n + 1, 2):
        count = 0
        for p in primes:
            if p > even // 2:
                break
            if (even - p) in primes:
                count += 1
        even_counts[even] = count
    return even_counts

max_n = 100
counts = goldbach_counts(max_n)
for even, count in counts.items():
    print(f"{even}: {count} representations")
