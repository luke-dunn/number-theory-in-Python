from sympy import isprime
c=0
for z in range(2000):
    y=3**z-2
    if isprime(y):
        print(y, 'is 3^'+str(z)+'-2, and is prime')
        c+=1
    y=3**z+2
    if isprime(y):
        print(y, 'is 3^'+str(z)+'+2, and is prime')
        c+=1
print(c,'occurrences')
##c=0
##for z in range(1000):
##    y=2**z-1
##    if isprime(y):
##        c+=1
##        print(y, 'is 2^'+str(z)+'-1, and is prime')
##    y=2**z+1
##    if isprime(y):
##        c+=1
##        print(y, 'is 2^'+str(z)+'+1, and is prime')
##
##print(c,'occurrences')    
##
##c=0
##for z in range(1000):
##    y=5**z-2
##    if isprime(y):
##        c+=1
##        print(y, 'is 5^'+str(z)+'-2, and is prime')
##    y=5**z+2
##    if isprime(y):
##        c+=1
##        print(y, 'is 5^'+str(z)+'+2, and is prime')
##
##print(c,'occurrences')    
