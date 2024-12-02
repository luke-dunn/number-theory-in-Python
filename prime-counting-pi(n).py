from sympy import primerange

def prime_count_tabulate(limit):
    """
    Function to calculate the prime-counting function values
    up to a given limit and print them in a neatly tabulated format.

    Parameters:
        limit (int): The upper limit for calculating
        the prime-counting function.

    Returns:
        None (prints the tabulated output directly)
    """
    
    primes = list(primerange(2, limit))  # Convert to list so primes can be accessed multiple times

    n = 10
    print()
    print(f"{'n':<10}{'pi(n)':<12}")
    print("-------------------")

    while n <= limit:
        pi_n = len([x for x in primes if x < n])
        print(f"{n:<10}{pi_n:<12}")
        n *= 10

# Prompt the user to enter the upper limit for calculating
# the prime-counting function

upper_bound = int(input('Enter the maximum value for n > '))
prime_count_tabulate(upper_bound)
