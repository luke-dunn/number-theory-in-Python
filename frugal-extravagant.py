from sympy import factorint

# Function to test if a number is frugal, equidigital, or extravagant
def tes_frugal(n):
    a = factorint(n)  # Get prime factorization of n
    length = 0

    # Iterate over the prime factors and their exponents
    for prime, exponent in a.items():
        # Add the number of digits in the prime
        length += len(str(prime))
        # If exponent is greater than 1, add the number of digits in the exponent
        if exponent > 1:
            length += len(str(exponent))
    
    # Length of the original number in digits
    z = len(str(n))

    # Compare the total length of the factorization to the number's length
    if length < z:
        print(n, 'is frugal')
    elif length == z:
        print(n, 'is equidigital')
    else:
        print(n, 'is extravagant')

# Test the function on a range of numbers
for z in range(1,1000):
    tes_frugal(z)
