from math import log, sqrt


def problem88(nL):
    PS = [[] for _ in range(nL + 1)]
    for n in range(2, nL + 1):
        PS[n] += [[], []]
        for r in range(2, int(log(n, 2)) + 2):
            Sr = set()
            PS[n] += [[]]
            if r == 2:
                for d in range(1, int(sqrt(n)) + 1):
                    if (n - 1) % d == 0:
                        t = (d + 1, (n - 1) // d + 1, n - 2)
                        st = sum(t)
                        if st not in Sr:
                            PS[n][r] += [t]
                            Sr.add(st)
            else:
                for j in range(2**(r - 2) - r, int((n - 3*r + 2)/2) + 1):
                    for sl in PS[r + j][r - 1]:
                        if (n -r -j) % (sum(sl[:-1:]) + j) == 0:
                            t = tuple(list(sl[:-1:]) + [(n -r -j) // (sum(sl[:-1:]) + j) + 1, n - r])
                            st = sum(t)
                            if st not in Sr:
                                PS[n][r] += [t]
                                Sr.add(st)
            
            
    
    MS = [(0), (0)]
    for n in range(2, nL + 1):
        m = 2*n + 1
        mT = 0
        for rl in PS[n]:
            for t in rl:
                if sum(t) < m:
                    m = sum(t)
                    mT = t
        
        MS += [mT]
        
    MSs = []
    for msi in range(2, len(MS)):
        MSs += [sum(MS[msi])]
    
    MSss = set(MSs)
    return PS, MS, sum(MSss)
