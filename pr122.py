from functools import lru_cache

def computeBinaryMults(k):
    b = bin(k)[2::]
    m = len(b) - 1 + b.count('1') - 1
    return m

M = {}

def computeMinMults(k, l):
    if k == 1:
        return 0
    if k == 2:
        if l >= 2:
            return 1
        else:
            return -1
    
    m = 1
    A = [1, 2]
    
    @lru_cache(maxsize=1024)
    def countMults(d, a, Av, am, lim):
        if am >= lim:
            return -1
        if a * 2**(lim - am) < d:
            return -1
        bst = lim
        for av in reversed(Av):
            if av + a < d and (av + a) not in Av:
                lbst = countMults(d, av + a, tuple(Av + tuple([av + a])), am + 1, lim)
                if lbst > -1 and lbst < bst:
                    bst = lbst
            elif av + a == d:
                return am
        
        return bst
    
    return countMults(k, 2, tuple(A), 2, l)
        
        

def problem122(l, u):
    global M
    s = 0
    for k in range(l, u + 1):
        bl = computeBinaryMults(k)
        if (k - 1) > 1 and M[k - 1] + 1 < bl:
            bl = M[k - 1] + 1
        if (k - 2) > 1 and M[k - 2] + 1 < bl:
            bl = M[k - 2] + 1
        if k % 2 == 0 and (k/2) > 1 and M[k/2] + 1 < bl:
            bl = M[k/2] + 1
        mm = computeMinMults(k, bl)
        om = bl
        if mm > -1 and mm < om:
            om = mm
        
        M[k] = om
        s += om
    return s, M
        
