def zeta3(n):
    """
    Approximates the value of the Riemann zeta function at s = 3 (Apéry's constant)
    by summing the series sum(1/n^3) from n = 1 to the given upper limit.

    Args:
    n (int): The upper limit of the series to approximate ζ(3).

    Returns:
    float: The approximate value of ζ(3) for the given limit.

    Example:
    >>> zeta3(1000000)
    1.2020569031595942
    """
    return sum(1.0 / z**3 for z in range(1, n+1))

print(zeta3(1000000))

# ζ(3) ≈ 1.202056903159594285399.. known as Apéry's constant
