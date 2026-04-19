from math import sqrt
import numpy as np
import primes

def EuklidsFormPeriNG(l):
    "Vygeneruje vsetky primitivne pytagorejske trojice a ich sucty take, ze ich sucet nepresahuje l"
    T = set()
    nl = int((-3 + sqrt(1+4*l))/4)
    primes.initGlobalPrimes(int(sqrt((-1 + sqrt(1+2*l)) / 2)))
    for n in range(1, nl + 1):
        nD = set(primes.primeFactDecompPreinitialized(n))
        ml = int((-n + sqrt(n*n+2*l))/2)
        for m in range(n + 1, ml + 1, 2):
            mD = set(primes.primeFactDecompPreinitialized(m))
            if len(nD.intersection(mD)) == 0:
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                p = a + b + c
                if p <= l:
                    T.add((a, b, c, p))
    
    return T

def TransformativePeriNG(l):
    "Vygeneruje vsetky primitivne pytagorejske trojice take, ze ich sucet nepresahuje l"
    T = [(3, 4, 5)]
    nT = []
    Ttg = [(3, 4, 5)]
    M = [np.matrix([[1, 2, 2], [-2, -1, -2], [2, 2, 3]]), np.matrix([[1, 2, 2], [2, 1, 2], [2, 2, 3]]), np.matrix([[-1, -2, -2], [2, 1, 2], [2, 2, 3]])]
    cont = True
    
    while cont:
        cont = False
        for t in Ttg:
            for m in M:
                nt = tuple((t*m).tolist()[0])
                if sum(nt) <= l:
                    nT += [nt]
                    cont = True
        
        T += nT
        Ttg = nT
        nT = []
    
    return T
