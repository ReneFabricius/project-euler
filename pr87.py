from math import sqrt
from primes import primes

def findTripletsBel(n):
    a = int(sqrt(n)) + 1
    P = primes(a)
    S = set()
    for i2 in range(len(P)):
        b = False
        for i3 in range(len(P)):
            for i4 in range(len(P)):
                s = P[i2]**2 + P[i3]**3 + P[i4]**4
                if s < n:
                    S.add(s)
                else:
                    if i4 == 0:
                        b = True
                    break
                    
            if b:
                break

    return len(S)
