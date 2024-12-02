# some figurate numbers as list comprehensions
# see if you can follow the nesting


print('''
triangular numbers

''',[sum(range(1,x)) for x in range(2,15)])

print('''
tetrahedral numbers

''',[sum([sum(range(1,x)) for x in range(2,y)]) for y in range(3,15)])

print('''
3-simplex numbers

''',[sum([sum([sum(range(1,x)) for x in range(2,y)]) for y in range(3,z)]) for z in range(4,16)])


# output:


# triangular numbers
#
#  [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91]
#
# tetrahedral numbers
#
#  [1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286, 364]
#
# 3-simplex numbers
#
#  [1, 5, 15, 35, 70, 126, 210, 330, 495, 715, 1001, 1365]
#

# is this pythonic or just confusing lol?
