from math import sqrt
from fractions import Fraction

def continuedFracSQroot(n, maxPer = 0):
    F = []
    sqr = sqrt(n)
    F += [int(sqr)]
    if F[0] * F[0] == n:
        return F
    fd = 1
    d = fd
    fa = F[0]
    a = fa
    i = 1
    while True:
        F += [int(d/(sqr - a))]
        nd = n - a*a
        d = nd // d
        a = -(a - F[i] * d)
        if a == fa and d == fd:
            return F
        
        if maxPer and i >= maxPer:
            return 0
        
        i += 1

def periodicContinuedFraction(a, b, c):
    "Vrati periodicky retazovy zlomok (a + sqrt(b))/c, pre b nie stvorec, index zaciatku periodickej casti a True/False pre zaporny/kladny vyraz"
    # Rosen - Elementary number theory and its applications (p 379)
    P0, d, Q0 = 0, 0, 0
    if (b - a*a) % c == 0:
        P0, d, Q0 = a, b, c
    else:
        P0, d, Q0 = a*abs(c), b*c*c, c*abs(c)
    neg = (a + sqrt(b))/c < 0
    if neg:
        Q0 = -Q0
    F = []
    Pk, Qk = P0, Q0
    L = []
    ak = 0
    fst = True
    while (Pk, Qk) not in L or fst:
        L += [(Pk, Qk)]
        ak = int((Pk + sqrt(d))/Qk)
        if fst:
            F += [ak]
        else:
            F += [abs(ak)]
        Pk = ak*Qk - Pk
        Qk = (d - Pk*Pk)/Qk
        if fst:
            fst = False
    
    return F, L.index((Pk, Qk)), neg
        
def periodLengthContinuedFSQroot(n):
    return len(continuedFracSQroot(n)) - 1


def nthConvergentSQroot(a, n):
    "N-ty konvergent(od 0) square-free cisla"
    F = continuedFracSQroot(a)
    a0 = F[0]
    F = F[1::]
    r = len(F)
    if r == 0:
        print("Zadane cislo je stvorec")
        return a0
        
    P = [0, a0, a0*F[0] + 1]
    Q = [0, 1, F[0]]
    if n < 2:
        return Fraction(P[n + 1], Q[n + 1])
    
    for i in range(2, n + 1):
        P = P[1::] + [0]
        Q = Q[1::] + [0]
        P[2] = F[(i - 1) % r] * P[1] + P[0]
        Q[2] = F[(i - 1) % r] * Q[1] + Q[0]
    
    return Fraction(P[2], Q[2])

def nthConvergentSQrootPrecomputed(F, n):
    "N-ty konvergent(od 0) periodickeho retazoveho zlomku"
    a0 = F[0]
    F = F[1::]
    r = len(F)
    if r == 0:
        print("Zadane cislo je stvorec")
        return a0
        
    P = [0, a0, a0*F[0] + 1]
    Q = [0, 1, F[0]]
    if n < 2:
        return Fraction(P[n + 1], Q[n + 1])
    
    for i in range(2, n + 1):
        P = P[1::] + [0]
        Q = Q[1::] + [0]
        P[2] = F[(i - 1) % r] * P[1] + P[0]
        Q[2] = F[(i - 1) % r] * Q[1] + Q[0]
    
    return Fraction(P[2], Q[2])
    
def nConvergentsQuadraticSurdPrecomputed(F, pi, n, neg):
    "Vrati list prvych n konvergentov periodickeho retazoveho zlomku F, kde sa periodicka cast zacina na pi-tom mieste, neg znamena minus pred retazovym zlomkom"
    q = 1
    if neg:
        q = -1
    pl = len(F) - pi
    A = [1, F[0]]
    B = [0, 1]
    C = [Fraction(q*A[1], B[1])]
    for k in range(1, n):
        if k < pi:
            A = [A[1], F[k]*A[1] + A[0]]
            B = [B[1], F[k]*B[1] + B[0]]
        else:
            A = [A[1], F[(k - pi) % pl + pi]*A[1] + A[0]]
            B = [B[1], F[(k - pi) % pl + pi]*B[1] + B[0]]
        C += [Fraction(q*A[1], B[1])]
    
    return C
    
