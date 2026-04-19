from primes import primes, isPrime

def quadPrimProd():
    P = primes(500000)
    B = primes(1000)
    m = 0
    mb = 2
    ma = -999
    for b in B:
        for a in range(-b + 1, 1000):
            n = 0
            c = True
            while c:
                p = n*n + a*n + b
                if (p < 2) or (p not in P):
                    c = False
                n += 1
            if (n - 1 > m):
                m = n - 1
                mb = b
                ma = a
   
    return m, ma, mb, ma*mb         

def quadPrimProdCheck():
    B = primes(1000)
    m = 0
    mb = 2
    ma = -999
    for b in B:
        for a in range(-b + 1, 1000):
            n = 0
            c = True
            while c:
                p = n*n + a*n + b
                if (not isPrime(p)):
                    c = False
                n += 1
                
            if (n - 1 > m):
                m = n - 1
                mb = b
                ma = a
   
    return m, ma, mb, ma*mb        
