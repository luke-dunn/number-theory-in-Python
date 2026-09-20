from math import sin, exp

#tags: #iteration #dynamics #attractor #basin #stretch-fold

def iterate(x):
    for _ in range(50):
        x = sin(exp(x))
    return x

for start in [-10, -1, 0, 1, 5, 10]:
    print(start, iterate(start))

# gives:

##-10 0.9983886029750519
##-1 0.9983886029750519
##0 0.4147677328733832
##1 0.9983886029750519
##5 0.4147677328733832
##10 0.4147677328733832

# observation the second convergent is near sqrt(2)-1 but this is coincidence, nearness in number is not kinship in meaning.

# The horizon expands faster than the traveller advances; progress is measured not by arrival, but by the widening of view.

# Folding does not only bring things together; it also decides what stays apart

# The known systems are landmarks; the space of possible systems is still mostly wilderness..
