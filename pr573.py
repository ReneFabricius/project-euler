from random import random
from collections import Counter
import gmpy2
from gmpy2 import mpq, mpfr, log10

def MonteCarloRace(n):
    C = Counter()
    l = 100000*n
    for i in range(l):
        S = []
        for j in range(n):
            S += [random()]
            
        S.sort()
        for c in range(1, n + 1):
            w = True
            for r in [k for k in range(1, n + 1) if k != c]:
                if S[c - 1] / c > S[r - 1] / r:
                    w = False
                    break
            
            if w:
                C[c] += 1
                break;
    print(C)
    return [C[p] / l for p in range(1, n + 1)]

def UnfairRace(n):
    "Len parne n"
    b = n**(n-1)
    r = (int(n / 2))**(n - 1)/ b / (int(n/2) - 1) / 2
    
    for k in range(int(n/2) + 1, n - 1):
        r += k**(k-1)*(n-k)**(n-k-1) / b
        r *= k/(n-k-1)
    
    r += (n-1)**(n-2) / b
    r *= 2*(n-1)
    
    r += 1
    
    return r
    
    
def UnfairRaceGmp(n):
    "Len parne n"
    S = mpfr(0)
    s = pow(10, log10(mpq(n - 1, n)) * (n - 1))
    
    S += 2 * s
    
    for j in range(2, int(n/2)):
        s *= pow(10, log10(mpq(n - j, n - j + 1)) * (n - j))*pow(10, log10(mpq(j, j - 1)) * (j - 1))
        S += 2 * s
    
    s *= pow(10, log10(mpq(int(n/2), int(n/2) - 1)) * (int(n/2) - 1)) * pow(10, log10(mpq(int(n/2), int(n/2) + 1)) * int(n/2))
    S += s
    S += 1
    
    return S
