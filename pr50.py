from primes import primes, isPrime

def lConsecPrimSumBel():
    "Najde najdlhsiu neprerusenu postupnost prvocisel ktorych suma je prvocislo mensie ako l"
    l = 1000000
    P = primes(50200)       # Pre sucet do 1000 existuje 21 clenna postupnost prvocisiel, sucet poslednych 21 prvocisiel do 50200 > 1000000
    m = 0
    mb = 0
    me = 1
    for d in range(len(P), 1, -1):
        s = sum(P[:d])
        nf = False
        for b in range(len(P) - d + 1):
            if nf:
                s -= P[b - 1]
                s += P[b + d - 1]
            else:
                nf = True
                
            if s > l:
                break
                
            if isPrime(s):
                m = d
                mb = b
                me = b + d
                return m, P[mb:me], sum(P[mb:me])           # dlzka postupnosti, postupnost, sucet postupnosti
