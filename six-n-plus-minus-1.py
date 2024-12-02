from sympy import isprime

# For p != 2, 3 the formula 6n +- 1 generates all primes and some composites
# This script investigates the ratio of composites to primes as slimit increases

slimit = 100
candidates = [6*n-1 for n in range(1, slimit) if 6*n-1 > 1]  # Exclude 1
candidates.extend([6*n+1 for n in range(1, slimit)])
candidates.sort()

misses = []
for z in candidates:
    if not isprime(z):
        misses.append(z)

# Calculate the ratio of composites to primes
ratio = len(misses) / len(candidates)

# Output the ratio and the first 50 composite misses
print(f"Ratio of composites to total candidates: {ratio}")
print(f"First 50 composites: {misses[:50]}")
