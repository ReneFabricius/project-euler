from math import log
from primes import primes
from collections import Counter
from math import sqrt

def findM(n, e):
    "Najde minimalne cislo ktoreho faktorial je delitelny n**e"
    m = 0
    while e / n >= 1:           # Teda iste musim dosiahnut dalsi nasobok n**2
        e -= n + 1
        m += n * n
        c = m - n*n             # Pripadne vyssie mocniny n
        if c > n:
            e -= int(log(c, n))
    
    if e > 0:
        m += e * n
    
    return m, e

def s(n):
    F = primeFactDecomp(n)
    P = list(F.keys())
    m = 0
    l = 0
    e = 0
    for p in range(len(P) - 1, -1, -1):
        if P[p]*F[P[p]] > m:
            if F[P[p]] == 1:
                m = P[p]
                l = P[p]
            else:
                mp, pe = findM(P[p], F[P[p]])
                if mp > m:
                    m = mp
                    l = P[p]
                    e = pe
    ml = 0
    if e > 0:
        ml = e * l
    else:
        ml = l
    
    for p in P:
        i = 1
        while i * p < ml:
            mm, ee = findM(p, F[p] + i)
            if mm > m:
                ml = i * p
                break
            i += 1
    
    return m, ml


def S(n):
    B = [True] * (n + 1)
    S = 0
    for i in range(2, n + 1):
        if B[i]:
            p, l = s(i)
            if n // i < l - 1:
                S += p * B[i:(n // i + 1)*i:i].count(True)
                B[i:(n // i + 1)*i:i] = [False] * (n // i)
            else:
                S += p * B[i:l*i:i].count(True)
                B[i:l*i:i] = [False] * (l - 1)
    return S
    
def testT(n):
    for i in range(2, n + 1):
        p, l, e = s(i)
        for j in range(1, l):
            pj, lj, ej = s(j*i)
            if p != pj:
                print ("Pri zaklade " + str(i) + " kde p: " + str(p) + ", limitovanom " + str(l) + ", s e: " + str(e) + ", sa " + str(j) + "-ty nasobok nesprava podla predpokladu, s p:" + str(pj) + ", l: " + str(lj) + " a e: " + str(ej))
    
    
def countOccurences(n):
    C = Counter()
    L = Counter()
    
    for i in range(2, n + 1):
        m, l, e = s(i)
        C[m] += 1
        L[l] += 1
    
    return C, L
    
    
    
    
    
    
P = primes(10**4)
    
def sim_primeFactDecomp(n):
    "Najde prvociselny rozklad cisla"
    F = Counter()
    a = int(sqrt(n))
    F = Counter()
    for p in P:
        while (n % p == 0):
            n = n / p
            F[p] += 1
        if (n == 1):
            return F
        if p > a:
            break
        
            
    F[int(n)] += 1
    
    return F
    
def sim_findM(n, e):
    "Najde minimalne cislo ktoreho faktorial je delitelny n**e"
    m = 0
    while e / n >= 1:           # Teda iste musim dosiahnut dalsi nasobok n**2
        e -= n + 1
        m += n * n
        c = m / (n*n)             # Pripadne vyssie mocniny n
        if c >= n:
            while c % n == 0 and c > 0:
                e -= 1
                c //= n
    
    if e > 0:
        m += e * n
    
    return m
    
def sim_s(n):
    F = sim_primeFactDecomp(n)
    P = list(F.keys())
    m = 0
    for p in range(len(P) - 1, -1, -1):
        if P[p]*F[P[p]] > m:
            if F[P[p]] == 1:
                m = P[p]
            else:
                mp = sim_findM(P[p], F[P[p]])
                if mp > m:
                    m = mp
    return m
    
def sim_S(n):
    S = 0
    for i in range(2, n + 1):
        S += sim_s(i)
    
    return S
