from collections import Counter

c=Counter()

a=2**11000
for z in str(a):
    c[z]+=1

for key in c:
    print (key,c[key])
