from functools import reduce
from primes import primes

def sumPrimesBel(n):
    P = primes(n - 1)
    s = reduce(lambda a, b: a + b, P)
    return s
