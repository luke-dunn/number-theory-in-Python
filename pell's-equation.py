from math import sqrt

# Check if a given x, y, d satisfies Pell's equation
def is_solution(x, y, d):
    return x**2 - d*y**2 == 1

# Find solutions for Pell's equation for a range of D and x values
def find_pell_solutions(min_d, max_d, max_x):
    solutions = []
    D = [d for d in range(min_d, max_d + 1) if int(d**0.5) != d**0.5]  # d nonsquare
    for d in D:
        for x in range(2, max_x + 1):
            # Pre-calculate max_y for efficiency
            max_y = int(sqrt((x**2 - 1) / d)) 
            for y in range(1, max_y + 1):
                if is_solution(x, y, d):
                    solutions.append((x, y, d))
                    break  # Move to the next x after finding a solution
    return solutions

# Parameters for the search
min_d = 2
max_d = 20  # Adjust as needed for more D values
max_x = 1000  # Larger values of x for more solutions

# Find Pell's equation solutions
solutions = find_pell_solutions(min_d, max_d, max_x)

# Output the solutions
for solution in solutions:
    print(solution)

# x/y will tend to be a good rational approximation for sqrt(D)
# note this iterative method is not as efficient as the
# continued fraction method but is included here anyway!
