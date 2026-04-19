from primes import primes

def Pp(n):
    P = primes(n)
    W = [0 for _ in range(n + 1)]
    for p in P:
        for s in range(p + 2, n + 1):
            W[s] += W[s - p]
            if s - p <= p:
                W[s] += 1
    
    return W[n]
    
def problem77(m):
    v = 0
    while Pp(v) <= m:
        v += 1
    
    return v
# PDF k problemu 31
