from math import factorial

F = [factorial(i) for i in range(10)]

def nextInChain(n):
    r = 0
    while n:
        d = n % 10
        n //= 10
        r += F[d]
    
    return r
    

def problem74(l, lch):
    L = [-1 for i in range(l)]
    c = 0
    D = {}
    for i in range(1, l):
        if L[i] < 0:
            CH = [i]
            rl = -1
            nich = nextInChain(CH[-1])
            while nich not in CH:
                if nich >= l:
                    if nich in D:
                        rl = D[nich]
                        break
                elif L[nich] >= 0:
                    rl = L[nich]
                    break
                CH.append(nich)
                nich = nextInChain(CH[-1])
                
            if rl == -1:
                ni = CH.index(nich)
                for chi in range(len(CH)):
                    if CH[chi] < l:
                        pl = 0
                        if chi < ni:
                            pl = len(CH) - chi
                            L[CH[chi]] = pl
                        else:
                            pl = len(CH) - ni
                            L[CH[chi]] = pl
                        
                        if pl == lch:
                            c += 1
            else:
                for chi in range(len(CH)):
                    pl = len(CH) - chi + rl
                    if CH[chi] < l:
                        L[CH[chi]] = pl
                        if pl == lch:
                            c += 1
                    else:
                        D[CH[chi]] = pl
    
    return c
