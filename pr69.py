from math import sqrt
from primes import primes


def maximiseTotdivNBel(n):
    a = int(sqrt(n)) + 1
    P = primes(a)
    pp = 1
    for i in range(len(P)):
        pp *= P[i]
        if pp > n:
            pp /= P[i]
            break

    return pp
