# A004080 @oeis
# Least k such that H(k) >= n, where H(k) is the harmonic
# number Sum_{i=1..k} 1/i.

def harmon(n,k):
    zet=0
    x=1
    for z in range(1,n):
        zet+=1.0/z
        if zet>=k:
            return (z)

for k in range(2,10):
    print(harmon(10000,k), end=', ')


# output
# 4, 11, 31, 83, 227, 616, 1674, 4550, 
