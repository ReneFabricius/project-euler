def p(n):
    W = [0 for _ in range(n + 1)]
    W[0] = 1
    for mN in range(1, n + 1):
        for s in range(mN, n + 1):
            W[s] += W[s - mN]
    
    return W[n]

CP = {0 : 1}
def pEulerMod(n, m):
    if n < 0:
        return 0
        
    global CP
    if n in CP:
        return CP[n]
    
    s = 0
    for k in range(1, n + 1):
        n1 = n - k*(3*k - 1)//2
        n2 = n - k*(3*k + 1)//2
        if n1 < 0 and n2 < 0:
            break
            
        if k % 2 == 1:
            s += pEulerMod(n1, m) + pEulerMod(n2, m)
        else:
            s -= pEulerMod(n1, m) + pEulerMod(n2, m)
        s = s % m
    
    s = s
    CP[n] = s
    return s
    
def problem78(m):
    v = 0
    while pEulerMod(v, m) % m != 0:
        v += 1
    
    global CP
    CP = {0 : 1}
    return v
    
# http://mathworld.wolfram.com/PartitionFunctionP.html (11)
