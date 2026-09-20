from collections import Counter
import matplotlib.pyplot as plt
from mpmath import mp

mp.dps = 10000

digits = str(mp.pi).replace('.', '')

c = Counter(digits)

plt.bar(c.keys(), c.values())

plt.xlabel('digit')
plt.ylabel('frequency')
plt.title('Digit frequencies in pi')

plt.show()
