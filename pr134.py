from math import log, ceil
from euclidean_alg import extEuclid
from primes import primes

def problem134(l):
    L = []
    P = primes(int(1.1*l))
    p_1_i = 2
    sum_s = 0
    while P[p_1_i] <= l:
        p_1 = P[p_1_i]
        p_2 = P[p_1_i + 1]
        m = 10**ceil(log(p_1, 10))
        gcd_, x, y = extEuclid(p_2, m)
        x_0 = (x*p_1) % m
        n = p_2*x_0
        sum_s += n
        L += [tuple([p_1, p_2, n])]
        
        p_1_i += 1
    
    return L, sum_s
