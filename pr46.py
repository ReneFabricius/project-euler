from math import sqrt
from primes import primes, primesRang

def problem46():
    l = 10000
    P = primes(l)
    P = P[1::]
    PS = set(P)
    i = 9
    while True:
        if i > l:
            Pn = primesRang(l + 1, 2*l)
            P += Pn
            PS = set(P)
            l *= 2
        
        if i not in PS:
            g = False
            for p in P:
                if p >= i:
                    break
                if sqrt((i - p) // 2) % 1 == 0:
                    g = True
                    break
            
            if not g:
                return i
        
        i += 2
            
