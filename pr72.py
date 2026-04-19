# Podla http://www.cut-the-knot.org/blue/Farey.shtml

from math import sqrt
import primes

def problem72(de):
    "Spocita pocet prvkov vo Farey-ho postupnosti pre de"
    primes.initGlobalPrimes(int(sqrt(de)))
    
    s = 0
    for n in range(2, de + 1):
        s += primes.totientPreinitialized(n)
    
    return s
