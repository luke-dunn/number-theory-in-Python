# using this... is z=1, z=23 the only example of a square
# that is the sum of 3 consecutive cubes.
# From the TV drama 'Prime Target'

for z in range(10,100000):
    su = z**3 + (z+1)**3 + (z+2)**3
    roo = su**0.5
    if roo == int(roo):
        print(z)
