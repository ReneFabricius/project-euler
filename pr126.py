from itertools import combinations_with_replacement as c_w_r
from collections import Counter
from math import ceil

def cuboidCoverSize(n, a, b, c):
    "Vypocita pocet kociek potrebnych na uplne pokrytie v n-tej vrstve kvadra"
    return 2 * (a*b + a*c + c*b) + 4 * (n - 1) * (a + b + c + n - 2)


def C(n):
    "Vypocita pocet kvadrov ktore obsahuju v jednej zo svojich vrstiev n kociek"
    m = int((n / 2 - 1) / 2)
    C = list(c_w_r(range(1, m + 1), 3))
    p = 0
    Co = Counter()
    for c in C:
        l = 1
        while True:
            cs = cuboidCoverSize(l, *c)
            if cs > n:
                break
            Co[cs] += 1
            if cs == n:
                p += 1
                break
            l += 1
    
    return p, Co

def C1(n):
    if n % 2 != 0:
        return 0
    
    M = []
    for i in range(2, int((n + 1000) / 1000) + 1):
        M += [int(n / (2*i))]
    
    if len(M) == 0:
        M += [int(n/4)]
        
    C = list(c_w_r(range(1, M[-1] + 1), 3))
    
    P = []
    for i in range(2, int((n + 1000) / 1000)):
        L = []
        a = ceil(i/2) - 1
        b = int(i/2) + 1
        while b != 1:
            a += 1
            b -= 1
            L += [(a, b)]
        P += [L]
    
    for j in range(len(M) - 1):
        for c in range(M[j], M[j + 1], -1):
            for l in range(j, -1, -1):
                for k in P[l]:
                    C += [(c, k[0], k[1])]
    
    Co = Counter()
    for c in C:
        l = 1
        while True:
            cs = cuboidCoverSize(l, *c)
            if cs > n:
                break
            Co[cs] += 1
            l += 1
    
    return min([r for r in Co if Co[r] == 1000])
    #return Co
    
    
    
    
