from math import log, ceil
from collections import Counter
from primes import primes


def problem110(o):
    ul = 2*o - 1    # minimalny pocet delitelov cisla**2
    n = ceil(log(ul, 3))
    n5 = ceil(log(ul, 5))
    m = 0
    if n < 6:
        m = 11
    else:
        m = ceil(n * (log(n) + log(log(n)))) # horny odhad pre n-te prvocislo
    P = primes(m)
    
    mn = 1
    for pi in range(n):
        mn *= P[pi]
    
    def findPowers(notThreesrem, threes, notThreePows, remProd, maxAlloved):
        nonlocal mn
        if notThreesrem == 1 or remProd < 9:
            if remProd != 1:
                notThreePows += [ceil((remProd - 1)/2)*2 + 1]
            notThreePows += [3]*threes
            nmb = 1
            for pi in range(len(notThreePows)):
                nmb *= P[pi]**((notThreePows[pi] - 1)//2)
            if nmb < mn:
                mn = nmb
            return
        
        currPows = notThreePows[:] + [1] + [3]*threes
        currNmb = 1
        for pi in range(len(currPows)):
                currNmb *= P[pi]**((currPows[pi] - 1)//2)
        
        maxAA = int(log(mn/currNmb, P[len(notThreePows)]))
        
        currProd = 1
        for pw in notThreePows:
            currProd *= pw
        
        
        for aa in range(2*min(maxAA, maxAlloved) + 1, ceil(remProd**(1/notThreesrem)) - 1, -2):
            findPowers(notThreesrem - 1, threes, notThreePows[:] + [aa],  ceil(rqp/(currProd*aa)), (aa - 1)//2)
        
    
    for dp in range(1, n5 + 1):
        dtl = n - 1 - dp
        rqp = ceil(ul/(3**(dtl)))
        findPowers(dp, dtl, [], rqp, ceil((rqp - 1)/2)*2 + 1)
    
    return mn
    
