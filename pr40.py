def d(n):
    b = 9
    i = 1
    s = 1
    sn = 10
    while sn <= n:
        s = sn
        sn += (i + 1) * 10**i * b
        i += 1
    
    n -= s
    m = n % i
    n = n % (i*10**(i-m))
    n //= i*10**(i-1 - m)
    if m == 0:
        return n + 1
    else:
        return n
    
def dNaive(n):
    s = ''
    i = 1
    while len(s) < n:
        s += str(i)
        i += 1
    
    return int(s[n-1])
    
def problem40(L):
    s = 1
    for l in L:
        s *= d(l)
    
    return s
