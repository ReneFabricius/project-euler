from math import log
from primes import findDivisors

def problem29(n):
    "Vyriesi problem 29 so spodnou hranicou 2 a hornou hranicou n"
    c = 0
    S = [True]*(n+1)
    for b in range(2, n + 1):
        if S[b]:
            l = int(log(n, b))
            Ce = set(range(2, n+1))
            for m in range(2, l + 1):
                Ce = Ce.union(set(range(2*m, m*n + 1, m)))
            
            c += len(Ce)
        
            pb = b
            while (pb <= n):
                S[pb] = False
                pb *= b
    
    return c
    
def problem29Naive(n):
    "Brute force riesenie 29"
    S = set()
    for b in range(2, n + 1):
        for e in range(2, n + 1):
            S.add(b**e)
            
    return len(S)
