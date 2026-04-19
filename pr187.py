import primes

def greatest_i_lower_than(L, lim):
    s = 0
    e = len(L)
    while s != e - 1:
        m = (s + e) // 2
        if L[m] > lim:
            e = m
        else:
            s = m

    return s

def pr187(L):
    prms = primes.primes(L//2)
    res = 0
    for i in range(len(prms)):
        cp = prms[i]
        if cp*cp >= L:
            break
        ei = greatest_i_lower_than(prms, L/cp)
        if prms[ei]*cp < L:
            res += ei - i + 1
        else:
            res += ei - i

    return res
