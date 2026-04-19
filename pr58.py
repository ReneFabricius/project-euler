from math import sqrt
import primes

def problem58(pb):
    up = 10**12
    primes.initGlobalPrimes(10**6)
    c = 1
    cp = 0
    l = 3
    x = 1
    while True:
        for i in range(4):
            x += l - 1
            if x > up:
                primes.initGlobalPrimes(sqrt(up*100))
                up *= 100
            c += 1
            if primes.isPrimePreinitialised(x):
                cp += 1
        if cp / c * 100 < pb:
            return l, c, cp
        l += 2
