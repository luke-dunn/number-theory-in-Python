from math import sqrt

# Archimedes-style approximation of pi
# using inscribed regular polygons in a unit circle.
#
# Unit circle:
#   radius = 1
#   circumference = 2*pi
#
# If an inscribed n-gon has side length s,
# then:
#   perimeter = n * s
#   pi ≈ perimeter / 2


# Start with an inscribed square.
# Its diagonal is the circle's diameter = 2.
# So its side length is sqrt(2).
n = 4
s = sqrt(2)

for step in range(10):
    perimeter = n * s
    pi_estimate = perimeter / 2

    print(f"{n:5d}-gon  pi ≈ {pi_estimate:.12f}")

    # Now double the number of sides:
    # square -> octagon -> 16-gon -> 32-gon ...
    #
    # If s is the old side length, the new side length is:
    #
    #   s_new = sqrt(2 - sqrt(4 - s^2))
    #
    # This is the chord-halving formula.
    # It comes from pure geometry:
    # repeatedly bisecting the central angle.
    s = sqrt(2 - sqrt(4 - s*s))

    n *= 2
