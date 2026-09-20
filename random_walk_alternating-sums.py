# ============================================================
# RANDOM WALK / CUMULATIVE SUM VISUALISATION
# ============================================================

from random import randint
import matplotlib.pyplot as plt

# running total
tot = 0

# store cumulative sums here
vals = []

# generate random terms
for _ in range(100):

    r = randint(0,4)

    # even -> positive
    # odd  -> negative
    term = ((-1)**r) * r

    # update cumulative total
    tot += term

    # save current total
    vals.append(tot)

# ============================================================
# PLOT
# ============================================================

plt.plot(vals)

# horizontal zero line
plt.axhline(0)

plt.xlabel("step")
plt.ylabel("cumulative sum")

plt.title("Random Alternating Series")

plt.show()
