from itertools import combinations
    
def problem106(n):
    # Najde dvojice podmnozin ktore treba skontrolovat
    d = range(n)
    S = set(d)
    CT = []
    for cl in range(2, n//2 + 1):
        for fc in combinations(d, cl):
            fcl = sorted(list(fc))
            for sc in combinations(S - set(fc), cl):
                scl = sorted(list(sc))
                if fcl[0] > scl[0]:
                    continue
                
                for i in range(1, cl):
                    if fcl[i] > scl[i]:
                        CT += [(fcl, scl)]
                        break
    
    return CT
