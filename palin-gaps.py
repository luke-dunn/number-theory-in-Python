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

def find_record_gap_palindromes(prime_list, max_window=50):
    gaps = np.diff(prime_list)
    record_starts = []
    current_max_len = 0

    for window in range(3, max_window + 1):
        for i in range(len(gaps) - window + 1):
            segment = gaps[i:i + window]
            if is_palindrome(segment):
                if window > current_max_len:
                    start_prime = prime_list[i]
                    record_starts.append((start_prime, window))
                    current_max_len = window
                    break  # Only keep the *first* occurrence for this new record length
    return record_starts

def main():
    upper_bound = 100_000_000  # You can raise this value
    print(f"Generating primes up to {upper_bound}...")
    primes = generate_primes_up_to(upper_bound)

    print("Searching for record-breaking palindromic prime gap sequences...")
    records = find_record_gap_palindromes(primes)

    print("\nRecord-breaking gap-palindrome starts:")
    for start_prime, length in records:
        print(f"Length {length} → Start Prime: {start_prime}")

    print("\nOEIS-style sequence (comma-separated):")
    print(", ".join(str(start) for start, _ in records))

if __name__ == "__main__":
    main()
