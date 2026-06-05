from mpmath import mp
from math import sqrt

mp.dps = 300


def pr_heegner():
    dist = mp.mpf(1.0)
    clos_n = None
    for n in range(2, 10**3 + 1):
        if int(sqrt(n)) ** 2 == n:
            continue

        sqr = mp.sqrt(n)

        pos = mp.cos(mp.pi * sqr)
        neg = mp.cosh(mp.pi * sqr)

        pos_dist = mp.fabs(mp.nint(pos) - pos)
        if pos_dist < dist:
            dist = pos_dist
            clos_n = n

        neg_dist = mp.fabs(mp.nint(neg) - neg)
        if neg_dist < dist:
            dist = neg_dist
            clos_n = -n

        print(f"pos dist: {pos_dist}, neg dist: {neg_dist}")

    return clos_n, dist
