from euclidean_alg import extEuclid
from primes import initGlobalPrimes, divisorsNumberPreinitialized
from math import ceil

def pr157(l):
    initGlobalPrimes(10**(ceil(l/2)))
    sum = 0
    for i in range(1, l + 1):
        sum += problem_157_n(i)

    return sum

def problem_157_n(n):
    sum = 0
    for k in range(2*n + 1):
        for i in range(2*n + 1):
            d_j = 2**k*5**i
            dd_j = 2**(2*n-k)*5**(2*n-i)
            if (d_j > dd_j):
                break

            gcd = extEuclid(d_j + 10**n, dd_j + 10**n)[0]
            d = divisorsNumberPreinitialized(gcd)
            sum += d

    return sum