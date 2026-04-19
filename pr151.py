from functools import lru_cache
import gmpy2
from gmpy2 import mpfr

gmpy2.get_context().precision = 100

def getEmptyDict():
    d = {}
    for b in range(2, 16):
        d[b] = [0, 0]
    
    return d

def sumDicts(D0, D1):
    nD = getEmptyDict()
    for b in range(2, 16):
        nD[b][0] = D0[b][0] + D1[b][0]
        nD[b][1] = D0[b][1] + D1[b][1]
    
    return nD

def multiplyDict(D, m):
    nD = getEmptyDict()
    for b in range(2, 16):
        nD[b][0] = D[b][0]*m
        nD[b][1] = D[b][1]*m
    
    return nD

def problem151(FE):
    
    @lru_cache(maxsize = 512)
    def countWays(E):
        if len(E) == 1 and E[0] == 1:
            return getEmptyDict()
        
        batch = sum(E)
        
        D = getEmptyDict()
        
        if len(E) == 1:
            D[batch][0] += 1
        else:
            D[batch][1] += 1
        
        
        for e in E:
            if e == 1:
                L = list(E)
                L.remove(e)
                cD = countWays(tuple(L))
                D = sumDicts(D, multiplyDict(cD, mpfr(1/len(E))))
            
            else:
                L = list(E)
                L.remove(e)
                
                while e > 1:
                    e //= 2
                    L.append(e)
                
                cD = countWays(tuple(L))
                D = sumDicts(D, multiplyDict(cD, mpfr(1/len(E))))
        
        return D
    
    FD = countWays(FE)
    res = 0
    for b in range(2, 16):
        if FD[b][0] + FD[b][1] > 0:
            res += FD[b][0]/(FD[b][0] + FD[b][1])
    
    return FD, res
