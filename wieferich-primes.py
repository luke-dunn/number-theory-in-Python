from sympy import primerange

# find Wieferich Primes where z^2 divides 2^(z-1)-1

a=primerange(2,10000)
wief=[]        
for z in a:
    if (2**(z-1)-1)%(z**2)==0:
        wief.append(z)

print (wief)
        
# 1093, 3511 these are the only ones known
# A001220 @ OEIS. 

