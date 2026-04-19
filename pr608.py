from math import sqrt
from collections import Counter
import numpy as np
import primes

def factDivs(m):
    primes.initGlobalPrimes(int(sqrt(m)) + 1)
    C = Counter()
    for k in range(1, m + 1):
        C += primes.primeFactDecompPreinitialized(k)
    
    divs = 1
    for p in C:
        divs *= (C[p] + 1)
    
    return C, divs


def countDivs10n(n):
    primes.initGlobalPrimes(int(sqrt(10**n)) + 1)
    s = 1
    for i in range(2, 10**n + 1):
        f = primes.primeFactDecompPreinitialized(i)
        cd = 1
        for p in f:
            cd *= (f[p] + 1)
        s += cd
    
    return s
    
def countDivsN(n):
    d = 0
    sqrn2 = (int(sqrt(n)))**2
    for x in range(1, int(sqrt(n)) + 1):
        d += n//x
    
    return 2*d - sqrn2

def countDivsInCount(C):
    res = 1
    for k in C:
        res *= (C[k] + 1)
    
    return res
    
def BF(m, n):
    primes.initGlobalPrimes(int(sqrt(n)) + 1)
    D_N = {1 : Counter()}
    for i in range(2, n + 1):
        D_N[i] = primes.primeFactDecompPreinitialized(i)
    
    F_D = Counter()
    for f in range(2, m + 1):
        F_D += primes.primeFactDecompPreinitialized(f)
    
    res = 0
    DIV_C = []
    def buildDivCounters(i, p_C):
        nonlocal DIV_C
        k = list(F_D.keys())[i]
        fin = len(F_D.keys()) == i + 1
        for c in range(F_D[k] + 1):
            Cou = Counter(p_C)
            Cou[k] = c
            if fin:
                DIV_C.append(Cou)
            else:
                buildDivCounters(i + 1, Cou)
    
    buildDivCounters(0, Counter())
    
    for Cnt in DIV_C:
        for j in D_N:
            res += countDivsInCount(Cnt + D_N[j])
    
    return res

def onlyMult(m, n):
    d_n = countDivsN(n)
    
    primes.initGlobalPrimes(int(sqrt(m)) + 1)
    F_D = Counter()
    for f in range(2, m + 1):
        F_D += primes.primeFactDecompPreinitialized(f)
    
    DIV_C = []
    def buildDivCounters(i, p_C):
        nonlocal DIV_C
        k = list(F_D.keys())[i]
        fin = len(F_D.keys()) == i + 1
        for c in range(F_D[k] + 1):
            Cou = Counter(p_C)
            Cou[k] = c
            if fin:
                DIV_C.append(Cou)
            else:
                buildDivCounters(i + 1, Cou)
    
    buildDivCounters(0, Counter())
    
    d_f = 0
    for Cnt in DIV_C:
        d_f += countDivsInCount(Cnt)
    
    return d_n*d_f
    
def problem608(m, n):
    # Hummel
    P = primes.primes(m)
    H = []
    H.append(1)
    IS = [0 for p in P]
    XS = [p for p in P]
    
    min_ind = np.argmin(XS)
    t_a = XS[min_ind]
    while t_a <= n:
        H.append(t_a)
        for i_i in range(len(P)):
            if H[-1] == XS[i_i]:
                IS[i_i] += 1
                XS[i_i] = P[i_i]*H[IS[i_i]]
        min_ind = np.argmin(XS)
        t_a = XS[min_ind]
    
    return H
