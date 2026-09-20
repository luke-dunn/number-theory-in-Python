def decimal_to_binary(decimal_number):
    """Convert a decimal number to binary."""
    if decimal_number == 0:
        return "0"
    binary = ""
    while decimal_number > 0:
        binary = str(decimal_number % 2) + binary
        decimal_number //= 2
    return binary

# Example usage:
decimal_number = 42
binary_result = decimal_to_binary(decimal_number)
print(f"Binary representation of {decimal_number} is {binary_result}")
