a=[1,2]
for x in range(2,30):
    a.append(a[x-1]*a[x-2])

tot=0

for z in a:
    tot+=(1/z)
print(tot)

# output
# 2.410278797207866
