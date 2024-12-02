# 1729 is known as the Ramanujan-Hardy number
# being 1^3 + 12^3 and also 9^3 + 10^3
# to quote Ramanujan: "it is a very interesting number;
# it is the smallest number expressible as the sum of
# two cubes in two different ways."
# This script finds more numbers like 1729.

cube_sums = {}
max_value = 50
# Check sums of cubes for combinations of x and y
for x in range(max_value):
    for y in range(x+1):
        sum_of_cubes = x**3 + y**3
        if sum_of_cubes not in cube_sums:
            cube_sums[sum_of_cubes] = [(x, y)]
        else:
            cube_sums[sum_of_cubes].append((x, y))

# Filter and print the numbers that can be written as the sum of cubes in two different ways
for sum_value, pairs in cube_sums.items():
    if len(pairs) > 1:  # Only print sums that have more than one pair
        for pair in pairs:
            print(f"{sum_value}: {pair}")
