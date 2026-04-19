# Pell equation, Størmer's theorem, http://11011110.livejournal.com/97325.html#comments - maxPeriod
from itertools import combinations
from Pell_equation import pellEqu
import primes

def findConsecutivePairsOfNsmoothNumbers(N, maxPer = 0):
    P = primes.primes(N)
    D = []
    for l in range(1, len(P) + 1):
        for c in combinations(P, l):
            d = 1
            for i in range(len(c)):
                d *= c[i]
            D += [d]
    
    D[0] = 1
    print(len(D))
    print(max(D))
    
    ns = max(3, (P[-1] + 1)//2)
    primes.initGlobalPrimes(N)
    
    CPSI = []
    for d in D:
        PS = pellEqu(2*d, ns, maxPer)
        if PS == 0:
            continue
        for psi in range(len(PS)):
            pp = ((PS[psi][0] - 1) // 2, (PS[psi][0] + 1) // 2)
            if primes.isN_smoothPreinitialized(pp[0], N) and primes.isN_smoothPreinitialized(pp[1], N):
                CPSI += [pp]
            elif psi == 0:                              # AK prvy par nie je smooth, ostatne nebudu
                break
                
    return CPSI

def problem581(n, maxPer = 0):
    CP = findConsecutivePairsOfNsmoothNumbers(n, maxPer)
    s = 0
    for cp in CP:
        s += cp[0]
    
    return s
