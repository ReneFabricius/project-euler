from functools import reduce
import primes

def problem124():
    primes.initGlobalPrimes(10**5)
    P = [(1,1)]
    for n in range(2, 100001):
         decomp = primes.primeFactDecompPreinitialized(n)
         rad = reduce(lambda a,b:a*b, decomp.keys())
         P += [(n, rad)]
    
    P.sort(key = lambda p:p[0])
    P.sort(key = lambda p:p[1])
    return P[10000-1]
