# investigating record breaking prime gaps

from sympy import isprime

results={z:[] for z in range(1000)}
max_value= 1000000
start, count = 2,0

for x in range(2,max_value):
    if isprime(x):
        results[count].append(start)
        start=x
        count=0
    else:
        count+=1

print("""
Record Breaking Prime Gaps
--------------------------
  
|   gap    |    prime   |
|----------|------------|""")
for key in results:
    if results[key]:
        results[key].sort()
        print('|',str(key).rjust(5),'   |',str(results[key][0]).rjust(10),'|')
print("""
--------------------------""")
