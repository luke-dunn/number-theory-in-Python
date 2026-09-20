from sympy import nextprime
import numpy as np

def is_palindrome(seq):
    return np.array_equal(seq, seq[::-1])

def generate_primes_up_to(limit):
    primes = []
    p = 2
    while p <= limit:
        primes.append(p)
        p = nextprime(p)
    return primes

def find_record_palindromes(prime_list, min_len=3, max_len=50):
    gaps = np.diff(prime_list)
    record_lengths = []
    seen_lengths = set()

    for length in range(min_len, max_len + 1):
        for i in range(len(gaps) - length + 1):
            segment = gaps[i:i + length]
            if is_palindrome(segment):
                if length not in seen_lengths:
                    start_prime = prime_list[i]
                    record_lengths.append((length, start_prime))
                    seen_lengths.add(length)
                    break  # Only want the first occurrence of each length
    # Sort by increasing length
    record_lengths.sort()
    return record_lengths

def main():
    upper_bound = 1_000_000  # You can raise this if your system allows
    print(f"Generating primes up to {upper_bound}...")
    primes = generate_primes_up_to(upper_bound)

    print("Searching for record-breaking palindromic prime gap sequences...")
    records = find_record_palindromes(primes)

    print("\nRecord-breaking palindromic gap sequence starts (by increasing length):")
    for length, start_prime in records:
        print(f"Length {length} → Start Prime: {start_prime}")

    print("\nOEIS-style sequence (comma-separated):")
    print(", ".join(str(start) for _, start in records))

if __name__ == "__main__":
    main()
