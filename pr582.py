from math import ceil, floor
import gmpy2
from gmpy2 import mpz, mpfr, sqrt

def testFind(l):
    S = set()
    Sdm = set()
    Sdn = set()
    ln = 21
    lm = 56
    for m in range(57, l + 1):
        bt = ceil((-m+sqrt(3*m*m-200))/2)
        tp = floor((-m+sqrt(3*m*m+200))/2)
        if bt == tp:
            S.add((m, bt))
            Sdm.add(m-lm)
            Sdn.add(bt-ln)
            ln = bt
            lm = m
    
    return S, Sdm, Sdn
    
def countTriangles(l):
    T = set()
    
    for m in range(2, min(int(sqrt(l)) + 1, 57)):
        for n in range(1, m):
            tc = m*m + n*n + m*n
            if tc <= l:
                ta = m*m - n*n
                tb = 2*m*n + n*n
                if ta > tb:
                    ta, tb = tb, ta
                df = tb - ta
                if df <= 100:
                    for i in range(1, min(int(100/df) + 1, int(l/tc) + 1)):
                        T.add((i*ta, i*tb, i*tc))
    
    if l < 57*57+21*21+57*21:
        return T
    
    
    gmpy2.get_context().precision = 400
    a = 1
    b = 2
    c = 3
    d = 2
    m = 56
    
    def testWithAdd(add):
        nonlocal T
        nonlocal m
        
        bt = ceil((-(m + add) + sqrt(3*(m + add)*(m + add) - 200))/2)
        tp = floor((-(m + add) + sqrt(3*(m + add)*(m + add) + 200))/2)
        if bt == tp:
            m += add
            tc = m*m + bt*bt + bt*m
            if tc <= l:
                ta = m*m - bt*bt
                tb = 2*m*bt + bt*bt
                if ta > tb:
                    ta, tb = tb, ta
                df = tb - ta
                if df <= 100:
                    for i in range(1, min(int(100/df) + 1, int(l/tc) + 1)):
                        T.add((i*ta, i*tb, i*tc))
                        
                    return 1
            else:
                return 2
        
        else:
            return 0
            
        
    while m <= sqrt(l) + 1:
        twa = testWithAdd(a)
        if twa == 2:
            return T
        if twa == 0:
            twa = testWithAdd(b)
            if twa == 2:
                return T
            if twa == 0:
                twa = testWithAdd(c)
                if twa == 2:
                    return T
                if twa == 0:
                    if d > 0:
                        a, b, c = b, c, b + c
                        d -= 1
                        print("a: " + str(a) + ", b: " + str(b) + ", c: " + str(c))
                    else:
                        b, c = c, a + c
                        d = 2
                        print("a: " + str(a) + ", b: " + str(b) + ", c: " + str(c))
    
    return T
