from math import sqrt
import primes

def sumOfPropDvisors(n):
    "Najde sucet delitelov cisla n mensich ako n"
    D = primes.primeFactDecompPreinitialized(n)
    s = 1
    for p in D:
        s *= (p**(D[p] + 1) - 1) // (p - 1)
    
    return s - n
    
def problem95(l):
    primes.initGlobalPrimes(int(sqrt(l)))
    N = [0 for _ in range(l + 1)]
    N[0:1:] = [-1, -1]
    mCHl = 0
    mCH = []
    
    cCH = []
    for n in range(2, l + 1):
        if N[n] == 0:
            cCH = [n]
            niCH = sumOfPropDvisors(n)
            ab = False
            while niCH not in cCH:
                if niCH > l:
                    ab = True
                    break
                if N[niCH] != 0:
                    ab = True
                    break
                    
                cCH += [niCH]
                niCH = sumOfPropDvisors(niCH)
            
            for chn in cCH:
                N[chn] = -1
                    
            if ab:
                continue
            
            iniCH = cCH.index(niCH)
            cCHl = len(cCH) - iniCH
            if cCHl > mCHl:
                mCHl = cCHl
                mCH = cCH[iniCH::]
    
    return mCH, min(mCH)
            
            
