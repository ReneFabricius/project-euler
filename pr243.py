from functools import reduce
from primes import primes, primeFactDecomp

prod = lambda L: reduce(lambda x, y: x*y, L, 1)

def leastRessilDenoms():
    Ph = primes(100)
    for pi in range(len(Ph)):
        d = prod(Ph[:pi + 1])
        dn = d - 1                                          # Pocet zlomkov
        nn = d * prod([(1-1/p) for p in Ph[:pi + 1]])
                    
        r = nn/dn
        print("Multipliing to prime: " + str(Ph[pi]) + " Denominator: " + str(d) + ", Ressilience: " + str(r))
        
def leastRessilDenomsBel(l):
    d = 223092870
    while True:
        F = set(primeFactDecomp(d))
        dn = d - 1
        nn = d * prod([(1 - 1/f) for f in F])
        if nn / dn < l:
            return d, nn / dn
        print(str(d) + " , R(d): " + str(nn / dn))
        d *= 2
