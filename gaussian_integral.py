from math import e, pi

# ------------------------------------------------------------
# Numerical approximation of the Gaussian integral
#
#                ∞
#               ⌠
#               |   -x²
#               |  e     dx  = √π
#               ⌡
#               0
#
# Therefore:
#
#                ∞
#               ⌠
#           2 * | e^(-x²) dx  = √π
#               ⌡
#               0
#
# Squaring both sides gives:
#
#     ( 2 * integral )² = π
#
# We will approximate the integral numerically and see π emerge.
# ------------------------------------------------------------


# width of each tiny strip
delta = 0.001

# how far along the x-axis to integrate
#
# we cannot integrate to infinity numerically,
# so we stop at x = 20
#
# because e^(-x²) becomes absurdly tiny very quickly,
# almost all of the area is already captured by then
rang = 20


# actual value of pi for comparison
print(pi)


# ============================================================
# RECTANGLE RULE
# ============================================================
#
# Approximate the curve using many thin rectangles.
#
# Each rectangle has:
#
#     width  = delta
#     height = f(x)
#
# area = height * width
#
# We add all these tiny areas together.
# ============================================================

tot = 0

for i in range(int(rang / delta)):

    # convert loop counter into actual x-coordinate
    x = i * delta

    # evaluate the Gaussian function:
    #
    #     f(x) = e^(-x²)
    #
    y = e**(-x**2)

    # add rectangle area
    tot += y * delta


# multiply by 2 because we only integrated from:
#
#     0 → +∞
#
# but the Gaussian is symmetric around x = 0
#
# then square the result to estimate pi
print((tot * 2)**2)



# ============================================================
# TRAPEZIUM RULE
# ============================================================
#
# Instead of flat rectangles,
# approximate the curve with tiny straight-line segments.
#
# Each strip becomes a trapezium:
#
#      y2
#      *
#     /|
#    / |
#   /  |
#  *---*
# y1
#
# area of trapezium:
#
#     ((y1 + y2) / 2) * width
#
# This usually converges much faster than rectangles
# because it captures the slope of the curve.
# ============================================================

tot = 0

for i in range(int(rang / delta)):

    # left and right x-values of the strip
    x1 = i * delta
    x2 = (i + 1) * delta

    # corresponding function heights
    y1 = e**(-x1**2)
    y2 = e**(-x2**2)

    # add trapezium area
    tot += ((y1 + y2) / 2) * delta


# again:
#
# multiply by 2 for symmetry,
# then square to estimate pi
print((tot * 2)**2)
