from math import sqrt
from primes import primes


PG = set()
L = 0

def isPrime(n):
    if n <= L:
        return n in PG
    for p in PG:
        if n % p == 0:
            return False
    
    return True

def isConcatPrime(a, b):
    if a == b:
        return False
    sa = str(a)
    sb = str(b)
    return isPrime(int(sa + sb)) and isPrime(int(sb + sa))
    
def minTuple(T):
    m = 10**10
    mt = tuple()
    for t in T:
        if sum(t) < m:
            m = sum(t)
            mt = t
    
    return mt, m
        
    
def problem60(l, n):
    P = primes(l)
    global L
    L = int(sqrt(int(str(P[-1]) + str(P[-2]))))
    if L < l:
        L = l
        
    P = primes(L)
    global PG
    PG = set(P)
    PC  = [set() for i in range(l + 1)]         # na i-tej pozicii - mnozina prvocisiel konkatovatelnych s i
    PN = [[] for j in range(n + 1)]             # na indexoch 2-n vsetky mozne tuple s pozadovanymi vlastnostami dlzky index
    for pfi in range(len(P)):
        if P[pfi] > l:
            break
        for psi in range(pfi + 1, len(P)):
            if P[psi] > l:
                break
            
            if isConcatPrime(P[pfi], P[psi]):
                PC[P[pfi]].add(P[psi])
                PN[2] += [(P[pfi], P[psi])]
    
    for m in range(3, n + 1):
        for n_p in PN[m - 1]:
            Is = PC[n_p[0]].intersection(PC[n_p[1]])
            for ei in range(2, len(n_p)):
                Is = Is.intersection(PC[n_p[ei]])
            
            for ip in Is:
                PN[m] += [n_p + tuple([ip])]
    
    mN = [0, 2]
    mNT = [tuple(), tuple([2])]
    
    for m in range(2, n + 1):
        if len(PN[m]) == 0:
            print(str(m) + " - prvkove tuple nenajdene")
            break
        cmt, cm = minTuple(PN[m])
        mN += [cm]
        mNT += [cmt]
        print("Minimalne najdene " + str(m) + " - prvkove tuple: " + str(mNT[m]) + ", sucet: " + str(sum(mNT[m])))
        if mN[m - 1] + l + 1 < mN[m]:
            print("Mozna existencia " + str(m) + " - prvkoveho tuple prvocisel s mensim suctom ako minimalny najdeny, potrebne spustit problem40 pre l aspon " + str(mN[m] - mN[m-1] - 1))
    
    
    
    
    return PN[n]
