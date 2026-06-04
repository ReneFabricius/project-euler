from math import prod
from primes import primes, isPrimeMillerRabin
from itertools import product


def pr293(lm=10**9):
    MILL_RAB_K = 22
    pr = primes(50)
    avail_primes = []
    running_prod = 1
    for p in pr:
        running_prod *= p
        if running_prod < lm:
            avail_primes.append(p)
        else:
            break

    max_pows = []
    for n, ap in enumerate(avail_primes):
        prev_pr = prod(avail_primes[:n])
        max_pow = 0
        while True:
            prev_pr *= ap
            if prev_pr < lm:
                max_pow += 1
            else:
                break

        max_pows.append(max_pow)

    print(
        f"avail primes: {avail_primes}, max powers: {max_pows}, nums to check: {prod([pw + 1 for pw in max_pows])}"
    )

    pFs = set()
    for pows in product(*[range(mp + 1) for mp in max_pows]):
        nz = False
        invalid = False
        for pw in pows[::-1]:
            if pw > 0:
                nz = True
            if nz and pw == 0:
                invalid = True
                break

        if invalid or not nz:
            continue

        num = 1
        for n, pw in enumerate(pows):
            num *= avail_primes[n] ** pw
            if num > lm:
                break

        if num > lm:
            continue

        pF = 3
        while True:
            if isPrimeMillerRabin(num + pF, k=MILL_RAB_K):
                pFs.add(pF)
                break
            else:
                pF += 2

    return sum(pFs)
