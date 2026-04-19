from math import log
from functools import lru_cache

# priblizne 40 min, v pythone pod minutu asi nepojde
def problem154(l, pw):
    full_c_5 = findPowsInFact(l, 5)
    full_c_2 = findPowsInFact(l, 2)
    dc = 0
    a = l
    while True:
        b = l - a
        if a < b:
            b = a
        if b < l - a - b:
            break
            
        pw_c_a_5 = findPowsInFact(a, 5)
        
        if full_c_5 - pw_c_a_5 < pw:
            a -= 1
            continue
        
        pw_c_a_2 = findPowsInFact(a, 2)
        if full_c_2 - pw_c_a_2 < pw:
            a -= 1
            continue
        
        mp_5 = 5**findMaxPowLog(l - a, 5)
        min_pw_bc_5 = findPowsInFact(mp_5 - 1, 5) + findPowsInFact(l - a - mp_5 + 1, 5)
        if full_c_5 - pw_c_a_5 - min_pw_bc_5 < pw:
            a -= 1
            continue
            
        mp_2 = 2**findMaxPowLog(l - a, 2)
        min_pw_bc_2 = findPowsInFact(mp_2 - 1, 2) + findPowsInFact(l - a - mp_2 + 1, 2)
        if full_c_2 - pw_c_a_2 - min_pw_bc_2 < pw:
            a -= 1
            continue
        
        while b >= l - a - b:
            pw_c_b_5 = findPowsInFact(b, 5)
            pw_c_c_5 = findPowsInFact(l - a - b, 5)
            if full_c_5 - (pw_c_a_5 + pw_c_b_5 + pw_c_c_5) >= pw:
                pw_c_b_2 = findPowsInFact(b, 2)
                pw_c_c_2 = findPowsInFact(l - a - b, 2)
                if full_c_2 - (pw_c_a_2 + pw_c_b_2 + pw_c_c_2) >= pw:
                    st = set([a, b, l - a - b])
                    if len(st) == 3:
                        dc += 6
                    elif len(st) == 2:
                        dc += 3
                    else:
                        dc += 1
            
            b -= 1
        
        a -= 1
    
    return dc
    
def BF(l, pw):
    full_c_5 = findPowsInFact(l, 5)
    full_c_2 = findPowsInFact(l, 2)
    dc = 0
    
    for a in range(l + 1):
        pw_c_a_5 = findPowsInFact(a, 5)
        pw_c_a_2 = findPowsInFact(a, 2)
        for b in range(l - a + 1):
            c = l - a - b
            pw_c_b_5 = findPowsInFact(b, 5)
            pw_c_c_5 = findPowsInFact(c, 5)
            if full_c_5 - (pw_c_a_5 + pw_c_b_5 + pw_c_c_5) >= pw:
                pw_c_b_2 = findPowsInFact(b, 2)
                pw_c_c_2 = findPowsInFact(c, 2)
                if full_c_2 - (pw_c_a_2 + pw_c_b_2 + pw_c_c_2) >= pw:
                    dc += 1
    
    return dc
             
        
    
@lru_cache(maxsize = 262144)
def findPowsInFact(n, p):
    c_c = n // p
    c = 0
    while c_c:
        c += c_c
        c_c //= p
    
    return c

def powsInSum(l, p):
    a = l
    while a >= l - a:
        print(a, l - a, findPowsInFact(a, p) + findPowsInFact(l - a, p))
        a -= 1

def findMaxPow(n, p):
    k = p
    c = 0
    while k <= n:
        c += 1
        k *= p
    
    return c

@lru_cache(maxsize = 262144)
def findMaxPowLog(n, p):
    if n == 0:
        return 0
    return int(log(n, p))

def testFindMaxPow(l, p):
    for n in range(l + 1):
        findMaxPow(n, p)

def testFindMaxPowLog(l, p):
    for n in range(1, l + 1):
        findMaxPowLog(n, p)


