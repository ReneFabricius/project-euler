from math import log
from primes import primes

def rotate(n):
    "Presunie prve cislo na posledne miesto, ak sa v cisle nachadza 0, vrati 0"
    if n < 10:
        return n
    sn = str(n)
    if '0' in sn:
        return 0
    return int(sn[1::]) * 10 + int(sn[0])

def problem35(l):
    rl = log(l, 10)
    P = primes(l)
    PS = set(P)
    C = []
    for p in P:
        r = rotate(p)
        c = True
        i = 1
        while r != p and i <= rl:
            i += 1
            if r in PS:
                r = rotate(r)
            else:
                c = False
                break
        
        if c:
            C += [p]
    
    return C
    
