from itertools import permutations
from primes import isPrime

def lPandigPrim():
    "Najde najvacsie pandigitalne prvocislo"
    m = 0
    for n in [4, 7]:            # Ostatne dlzky maju ciferne sucty delitelne 3
        R = range(1, n + 1)
        Ps = permutations(R)
        for P in Ps:
            if (P[n - 1] % 2 == 0):
                continue
            
            c = 0
            for i in range(n):
                c += P[i] * 10**(n - 1 - i)
                
            if isPrime(c) and c > m:
                m = c
                
    return m
    
