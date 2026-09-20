import gmpy2

def is_prime(n):
    """Fast primality test using gmpy2."""
    return gmpy2.is_prime(n)

def search_primes(limit):
    """Search primes of the form 3^n + 2."""
    for n in range(1, limit + 1):
        candidate = pow(3, n) + 2
        if is_prime(candidate):
            print(f"3^{n} + 2 is prime: {candidate}")

# Example: Searching up to n = 500
search_primes(10000)
