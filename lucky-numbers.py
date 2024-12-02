# we have looked at the Sieve of Eratosthenes before
# one can take the idea of a sieve process as starting with
# the natural numbers and weeding out certain numbers
# in a systematic way (according to a rule)
# Generalising this idea of a sieve process, one variant we
# find generates a sequence known as the 'Lucky Numbers'

# start with 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, (...)

# first remove every second number
# 1,3,5,7,9,11,13,15,17,19, (...)

# then acting on the list that remains, remove every third
# 1,3,7,9,13,15,19, (...)

# then remove every 4th
# 1,3,7,13,15,19

a = list(range(1, 50))

i = 1  # Start at the second element (which corresponds to the first 'rule')

while i < len(a):
    step = a[i]  # The "rule" is to remove every step-th number
    a = [a[j] for j in range(len(a)) if (j + 1) % step != 0]  # Remove every step-th element
    i += 1

print(a)
