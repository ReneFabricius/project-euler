from primes import primes
from math import log

def sstEvenlyDible(n):
    "Najde najmensie cislo ktore je delitelne vsetkymi cislami od 1 po n vratane"
    v = 1
    P = primes(n)
    for p in P:
        v = v * p ** int(log(n, p))
        
    return v

def chcecksstEvenlyDible(n):
    for i in range(1, n + 1):
        x = sstEvenlyDible(i)
        for d in range(1, i + 1):
            if (x % d != 0):
                return False
                
    return True
