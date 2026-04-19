from math import ceil, log
from primes import primes

def problem108(o):
    # Problem vedie na jednoduchy hyperbolicky pripad diofantickej rovnice: n*x - x*y + n*y = 0, kde riesenia hladame prostrednictvom delitelov n*n, rienia pozadovanych vlastnosti ziskame z delitelov <= n,
    # takze potrebujeme n take, ze pre pocet delitelov p(n*n) plati: (p(n*n) + 1)/2 <= o
    ul = 2*o - 1
    P = primes(200)
    ub = 1
    for pi in range(ceil(log(ul, 3))):
        ub *= P[pi]
    
    pnn = [0, 0] + [1] * (ub - 1)       # pocet delitelov cisla index**2
    for k in range(len(pnn)):
        if pnn[k] == 1:
            pw = 1
            while k**pw <= ub:
                m = 1
                nm = k**pw
                while m*nm <= ub:
                    if pw > 1:
                        pnn[m*nm] //= (2*(pw - 1) + 1)
                    pnn[m*nm] *= (2*pw + 1)
                    m += 1
                pw += 1
        
        if pnn[k] >= ul:
            return k
