"""
The Ramanujan-Nagell Equation:

The Ramanujan-Nagell equation is a specific type of Diophantine equation given by:

    x^2 + 7 = 2^n

Where x and n are integers. This equation asks which integer values of x and n satisfy the equation.

### Background:

The Ramanujan-Nagell equation was named after mathematicians Srinivasa
Ramanujan and Trygve Nagell.
It was originally studied by Ramanujan, and Nagell
later proved that the equation has only a finite number of integer solutions.

The equation relates a quadratic term (x^2) to an exponential term (2^n), and it is one of many similar equations that ask how powers of 2 (or other integers) can relate to squares or other powers of integers.

### Known Solutions:

The Ramanujan-Nagell equation has only five solutions, which are:

    (x, n) = (1, 3), (3, 4), (5, 5), (11, 7), (181, 15)

### Generalization:

The equation can be generalized to:

    x^2 + y = 2^n

This general form investigates how changing the constant term
(7 in the original equation) to other integers (y) influences
the existence of solutions.
The original Ramanujan-Nagell equation is a special case where y = 7.
The goal of the generalized equation is to find values of x, n, and y
such that the equation holds, which may or may not have finite solutions,
depending on the chosen value of y.
"""

from math import log2

def is_solution(x, n, y):
    """Check if x and n are a solution for the equation x^2 + y = 2^n."""
    return x**2 + y == 2**n

for z in range(16, 25):
    y = 7 * 4**z  # Generalization of y
    print(f'Testing for y = {y}, z = {z}')
    
    # Lower and upper bounds for x based on your logic
    lower_bound_x = (2**z) - 1
    upper_bound_x = 181 * (2**z) + 1
    
    for x in range(lower_bound_x, upper_bound_x):
        # Calculate a reasonable range for n based on the equation
        bound = int(log2(x**2 + y))  # log base 2 gives an approximation for n
        n_lower = bound - 2  # Small range around the approximate bound
        n_upper = bound + 2

        for n in range(n_lower, n_upper):
            if is_solution(x, n, y):
                print(f"Solution found: x = {x}, n = {n}, y = {y}")
                break

