from math import sqrt
from primes import primes

def problem131(n):
    P = primes(n)
    c = 0
    C = []
    for p in P:
        m = (-3 + sqrt(3*(4*p - 1)))/6
        if m.is_integer():
            c += 1
            C += [tuple([m**3, p])]
    
    return C, c
