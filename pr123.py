from primes import primes, primesRang

def problem123():
    P = primes(5*10**5)
    n = len(P)
    ln = -1
    for p in reversed(P):
        if n % 2 == 1:
            if (2*n*p) % (p*p) > 10**10:
                ln = n
            else:
                return ln
        n -= 1
