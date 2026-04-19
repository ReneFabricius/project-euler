from math import sqrt, gcd
from functools import lru_cache

def problem153(l):
    sqr_l = int(sqrt(l))
    j = 4
    sm = 0
    
    for a in range(1, sqr_l + 1):
        b = 1
        a2 = a*a
        b2 = b*b
        sq = a2 + b2
        while b <= a and sq <= l:
            if b == a and a != 1:
                break
            
            if gcd(a, b) != 1:
                b += 1
                b2 = b*b
                sq = a2 + b2
                continue
            
            c = (l//sq)
            '''r_lim = int((-j + sqrt(j*j + 4*c*j))/(2*j))
            
            for r in range(1, r_lim + 1):
                cs = (c//(r + 1) + 1 + c//r)*(c//r - c//(r + 1))*r
                sm += cs*a
                if a != b:
                    sm += cs*b
            
            for m in range(1, c//(r_lim + 1) + 1):
                cs = (c//m)*m*2
                sm += cs*a
                if a != b:
                    sm += cs*b'''
            
            cs = 2*countDivsAdv(c, j)
            sm += cs*a
            if a != b:
                sm += cs*b
                
                
            b += 1
            b2 = b*b
            sq = a2 + b2
    
    su = 0
    
    p_lim = int((-j + sqrt(j*j + 4*j*l))/2/j)
    
    for p in range(1, p_lim + 1):
        su += (l//(p + 1) + 1 + l//p)*(l//p - l//(p + 1))*p//2
    
    for d in range(1, l//(p_lim + 1) + 1):
        su += (l//d)*d
    
    
    return sm , su
    
def BF(l):
    CD = {}
    RD = {}
    cs = 0
    rs = 0
    
    for n in range(1, l + 1):
        CD[n] = set()
        RD[n] = set()
        for a in range(1, n + 1):
            for b in range(1, a + 1):
                g = gcd(a, b)
                if (n*g) % (a*a + b*b) == 0:
                    cs += 2*a
                    CD[n].add(tuple([a, b]))
                    CD[n].add(tuple([a, -b]))
                    if a != b:
                        cs += 2*b
                        CD[n].add(tuple([b, a]))
                        CD[n].add(tuple([b, -a]))
        
        for d in range(1, n + 1):
            if n % d == 0:
                rs += d
                RD[n].add(d)
    
    return cs, rs, CD, RD
    
def test():
    l = 1
    while True:
        cs_a, rs_a = problem153(l)
        cs_b, rs_b, CD, RD = BF(l)
        if cs_a != cs_b or rs_a != rs_b:
            return cs_a, rs_a, cs_b, rs_b, CD, RD
        
        l += 1

def countDivsNorm(l):
    su = 0
    for d in range(1, l + 1):
        su += d*(l//d)
    
    return su

@lru_cache(maxsize = 32768)
def countDivsAdv(l, j):
    su = 0
    p_lim = int((-j + sqrt(j*j + 4*j*l))/2/j)
    
    for p in range(1, p_lim + 1):
        su += (l//(p + 1) + 1 + l//p)*(l//p - l//(p + 1))*p//2
    
    for d in range(1, l//(p_lim + 1) + 1):
        su += (l//d)*d
    
    return su
