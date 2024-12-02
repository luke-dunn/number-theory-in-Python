from sympy import isprime

# Explore prime generating polynomials for longest sequence with consecutive x
# Type of polynomial is a quadratic, x**2 + x + a, with 1 < a < 99

longest_sequences = {}

for a in range(2, 100):
    count = 0
    longest_count = 0
    start_i = 0
    for i in range(1, 100):  # Increase the range for more tests
        pr = i**2 + i + a
        if isprime(pr):
            count += 1
        else:
            if count > longest_count:
                longest_count = count
                start_i = i - count
            count = 0

    longest_sequences[longest_count] = [a, start_i]

# Print the two longest sequences
for z in sorted(longest_sequences, reverse=True)[:2]:
    print("Longest sequence:", longest_sequences[z], "Length:", z)

# Calculate total coverage for different upper bounds
# We are checking x**2 + x + 41 for prime-generating sequences

def coverage_calculation(ubound):
    quadratic_nums = [x**2 + x + 41 for x in range(ubound)]
    prime_nums = [z for z in range(2, max(quadratic_nums) + 1) if isprime(z)]

    # Convert to sets for efficient intersection
    primes_set = set(prime_nums)
    quadratic_set = set(quadratic_nums)

    coverage = len(quadratic_set.intersection(primes_set)) / len(quadratic_set)
    return coverage

# Check coverage for different upper bounds
for ubound in range(100, 1001, 100):
    coverage = coverage_calculation(ubound)
    print(f"Coverage: {coverage:.2%}, Upper Bound: {ubound}")

# Longest sequence: [41, 1] Length: 39
