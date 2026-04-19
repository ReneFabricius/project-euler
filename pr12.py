from primes import divisorsNumber

def triangleNDivAb(l):
    n = 1
    a = 2
    while True:
        dn = divisorsNumber(n)
        if dn > l:
            return n
        
        n += a
        a += 1
        
