# The Thwaites conjecture (also known as the 3n + 1 conjecture, 
# the Collatz conjecture, and other names) proposes that no matter 
# what starting value is chosen, the sequence will always reach 1.

# This code generates the sequence and finds the seed with the 
# longest path to reach 1, searching up to a specified max value.

max_value = 100000  # Define the maximum seed value to search
seed, best_path_length, best_seed = 1, 0, 0

while seed <= max_value:
    path_length, term = 0, seed
    while term != 1:
        if term % 2 == 0:
            term //= 2  # Use integer division
        else:
            term = term * 3 + 1
        path_length += 1

    if path_length > best_path_length:
        best_path_length = path_length
        best_seed = seed
        print(f"New record: seed {best_seed} takes {best_path_length} steps to reach 1.")
    
    seed += 1
print()
print(f"Longest path: seed {best_seed} takes {best_path_length} steps.")
