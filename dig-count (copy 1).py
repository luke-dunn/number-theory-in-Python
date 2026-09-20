from collections import Counter

c=Counter()
a=''
for z in range(4000):
    a+=str(2**z)
for z in a:
    c[z]+=1

for key in sorted(c):
    print (key,c[key])
