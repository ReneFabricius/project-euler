from math import sqrt
import primes

def problem47(c):
    l = 1000000
    primes.initGlobalPrimes(1000)
    
    n = 4
    while True:
        if n > l:
            l *= 10
            primes.initGlobalPrimes(sqrt(l))
            
        if len(primes.primeFactDecompPreinitialized(n)) == c:
            p = True
            for d in range(1, c):
                if len(primes.primeFactDecompPreinitialized(n + d)) != c:
                    n += d
                    p = False
                    break
            if p:
                return n
        
        n += 1
