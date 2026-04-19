from primes import find_divisors_range_simple, primeFactDecomp
from math import sqrt

def pr211(l):
    divisors = find_divisors_range_simple(l)
    res_ns = []
    for n in range(1, l):
        sds = sum([d**2 for d in divisors[n]])
        if int(sqrt(sds))**2 == sds:
            res_ns.append(n)
            print(f"Found n: {n}")
            print(f"Prime factorization: {primeFactDecomp(n)}")
            print(f"Divisors: {divisors[n]}")
            print(f"Divisors squared: {[d**2 for d in divisors[n]]}")
            print(f"Divisors squared sum: {sds}, root: {sqrt(sds)}\n\n")
    
    print(res_ns)
    return sum(res_ns)


def pr211_direct(l):
    sdsq = [1] * l
    for d in range(2, l):
        if d < 100 or (d < 1000 and d % 100 == 0) or (d < 10000 and d % 1000 == 0) or (d < 100000 and d % 10000 == 0) or d % 100000 == 0:
            print(f"Applying d: {d}")
        dsq = d ** 2
        for mult in range(d, l, d):
            sdsq[mult] += dsq
    
    res = 0
    for n in range(1, l):
        rsdsq = sqrt(sdsq[n])
        if int(rsdsq) == rsdsq:
            print(f"Found {n}")
            res += n
    
    return res