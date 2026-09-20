from sympy import factorint
i='1'*25
for _ in range(25,50):
    i+='1'
    print (i,factorint(int(i)))

# 1111111111111111111 and 11111111111111111111111 are prime!
