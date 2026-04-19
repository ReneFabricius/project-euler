from itertools import combinations, permutations, product
from collections import Counter
from primes import isPrimeMillerRabin, primesRang

def problem111(n, k):
    ss = 0
    S = [0]*10
    M = [0]*10
    N = [0]*10
    Nmbrs = [[] for i in range(10)]
        
    def generateAndTest(Psts, Numd, Dig, BS):
        nonlocal N
        nonlocal S
        nonlocal M
        nonlocal Nmbrs
        for p in product([str(x) for x in range(10) if str(x) != Dig], repeat=len(Psts)):
            Curr = BS[:]
            nv = False
            for posI in range(len(Psts)):
                if Psts[posI] == 0 and p[posI] == '0':
                    nv = True
                    break
                Curr[Psts[posI]] = p[posI]
                
            if nv:
                continue
            
            CurrN = int(''.join(Curr))
            if isPrimeMillerRabin(CurrN, k):
                N[int(Dig)] += 1
                S[int(Dig)] += CurrN
                M[int(Dig)] = Nd
                Nmbrs[int(Dig)] += [CurrN]

    for d in range(10):
        Base = [str(d)]*n
        oP = []
        if d % 2 == 0 or d % 5 == 0:
            if d == 0:
                oP += [0]
            oP += [n - 1]
        
        for Nd in range(n - 1, 0, -1):
            if S[d] > 0:
                break
            
            PosN = n - Nd - len(oP)
            if PosN < 0:
                continue
            
            if PosN == 0:
                Pos = oP
                generateAndTest(Pos, Nd, d, Base)
            
            else:
                for c in combinations([x for x in range(n) if x not in oP], PosN):
                    Pos = oP + list(c)
                    generateAndTest(Pos, Nd, d, Base)

    ss = sum(S)
    return Nmbrs, M, N, S, ss

def test111(n):
    P = primesRang(10**(n-1), 10**n - 1)
    M = [0]*10
    for p in P:
        C = Counter(str(p))
        maxC = 0
        maxD = -1
        for d in C:
            if C[d] > maxC:
                maxC = C[d]
                maxD = d
        if M[int(maxD)] < maxC:
            M[int(maxD)] = maxC
    
    Nmbrs = [[] for _ in range(10)]
    for p in P:
        C = Counter(str(p))
        for d in range(10):
            if C[str(d)] == M[d]:
                Nmbrs[d] += [p]
    
    N = [len(nmbs) for nmbs in Nmbrs]
    S = [sum(nmbs) for nmbs in Nmbrs]
    return Nmbrs, M, N, S, sum(S)      
    
