"""Cunningham chains are sequences of primes where each successive number is 2*n+1 whe
with n as the previous number. This means that all items except the last in any chain
are Sophie-Germain primes
"""
from sympy import primerange, isprime
import numpy as np
from time import time
from pprint import pprint

def generate_primes_array(limit):
    primes = primerange(2, limit)
    prime_count_estimate = int((limit * 1.5)/ np.log(limit))  
    primes_array = np.zeros(prime_count_estimate, dtype=np.int64)
    
    index = 0
    for prime in primes:
        primes_array[index] = prime
        index += 1
    
    return primes_array[:index]

def find_cunningham_chains(prims):
    chains = {x: [] for x in range(2, 21)}
    used_primes = set()

    for p in prims:
        if p % 10 == 7 or p in used_primes:
            continue
        chain = [p]
        while True:
            q = 2 * chain[-1] + 1
            if isprime(q):
                chain.append(q)
                if q % 10 == 7:
                    break
            else:
                break
        
        chain_length = len(chain)
        if 2 <= chain_length <= 20 and not chains[chain_length]:
            chains[chain_length] = chain
            used_primes.update(chain)

    return {k: [int(x) for x in v] for k, v in chains.items() if v}

ti=time()

limit = 750000
primes_array = generate_primes_array(limit)

print(f"Search Range: {limit}")
print(f"NumPy array memory usage: {primes_array.nbytes} bytes")
print(f"Number of primes tested: {len(primes_array)}")
print()
print('here are the chains found')
print()

pprint(find_cunningham_chains(primes_array))

print()
print(f"time taken: {(time()-ti)/60} minutes")

# output

## Search Range: 5000000000
## NumPy array memory usage: 1879633784 bytes
## Memory usage  (19.8%)
## Number of primes tested: 234954223
## 
## here are the chains found
## 
## {2: [3, 7],
##  3: [41, 83, 167],
##  4: [509, 1019, 2039, 4079],
##  5: [2, 5, 11, 23, 47],
##  6: [89, 179, 359, 719, 1439, 2879],
##  7: [1122659, 2245319, 4490639, 8981279, 17962559, 35925119, 71850239],
##  8: [19099919,
##      38199839,
##      76399679,
##      152799359,
##      305598719,
##      611197439,
##      1222394879,
##      2444789759],
##  9: [85864769,
##      171729539,
##      343459079,
##      686918159,
##      1373836319,
##      2747672639,
##      5495345279,
##      10990690559,
##      21981381119]}
## 
## time taken: 99.03946168820063 minutes
