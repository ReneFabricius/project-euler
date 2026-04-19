import primes
import math
from time import time
from collections import Counter


def test_decomposition(l):
    start_oao = time()
    primes.initGlobalPrimes(int(math.sqrt(l)) + 1)
    D = [None]
    for i in range(1, l):
        D.append(primes.primeFactDecompPreinitialized(i))

    end_oao = time()
    print("Time one after one: " + str(end_oao - start_oao))

    start_sieve = time()
    prim_lim = int(math.sqrt(l) + 1)
    SD = [Counter() for i in range(1, l)]
    SD = [None] + SD
    SD[1][1] = 1
    PRODS = [1 for i in range(l)]
    PS = [True for i in range(prim_lim + 1)]
    for pc in range(2, prim_lim + 1):
        if PS[pc]:
            pcp = pc
            while pcp < l:
                pcm = pcp
                while pcm < l:
                    PRODS[pcm] *= pc
                    SD[pcm][pc] += 1
                    pcm += pcp
                pcp *= pc

            for np in range(pc*pc, prim_lim + 1, pc):
                PS[np] = False

    for rem in range(prim_lim + 1, l):
        if PRODS[rem] != rem:
            SD[rem][rem/PRODS[rem]] += 1

    end_sieve = time()
    print("Time sieve: " + str(end_sieve - start_sieve))

    return D, SD


def compute_digit_sum(n):
    while n > 9:
        r = 0
        while n:
            r += n % 10
            n = n // 10
        n = r

    return n


def combinations_increment(CT):
    L = {2: CT[2], 3: CT[3], 4: CT[4]}
    res = 0
    res += L[3]//2*3
    L[3] = L[3] % 2
    min24 = min(L[2], L[4])
    res += min24*2
    L[2] = L[2] - min24
    L[4] = L[4] - min24
    res += L[2]//3*2
    L[2] = L[2] % 3
    min23 = min(L[2], L[3])
    res += min23
    L[2] = L[2] - min23
    L[3] = L[3] - min23
    return res


def pr159(n):
    'Zalozene na: ciferny sucet sucinu sa rovna sucinu cifernych suctov'
    P = primes.primes(n)
    D = primes.rangePrimeFactDecomposition(n)
    PSUM = {}
    for p in P:
        PSUM[p] = compute_digit_sum(p)

    res = 0
    for i in range(2, n):
        DSC = Counter()
        for pf in D[i]:
            DSC[compute_digit_sum(pf)] += D[i][pf]

        for dsc in DSC:
            res += dsc*DSC[dsc]

        res += combinations_increment(DSC)

    return res

