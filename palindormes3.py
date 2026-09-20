
for x in range(1_000_000_000,3_000_000_000):
    z=x**5
    if str(z)==str(z)[::-1]:
        print (x,z)
    
