import primes

def pr668_brute_force(n):
    primes.initGlobalPrimes(int(n**(1/2)) + 1)
    count = 1
    for i in range(2, n + 1):
        if (i >> 20) << 20 == i:
            print(i)

        F = primes.primeFactDecompPreinitialized(i)
        FKL = list(F.keys())
        if (FKL[-1]*FKL[-1] < i):
            count += 1

    return count