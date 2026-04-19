from primes import primes

def mults(n):
    m = int(n / (5**3 * 13**2))
    P = primes(m)
    P4n1 = [p for p in P if p % 4 == 1]
    P4n3 = [2] + [p for p in P if p % 4 == 3]
    C = [(3, 2, 1), (7, 3), (10, 2)]
    R = []
    
    def buildR(iC, c, O, pr):
        for i in [p for p in range(len(P4n1)) if p not in O]:
            npr = pr * P4n1[i]**c[iC]
            if npr <= n:
                if iC == len(c) - 1:
                    nonlocal R
                    R += [npr]
                elif npr * P4n1[min(set([0, 1, 2]) - set(O))]**c[iC + 1] <= n:
                    buildR(iC + 1, c, O + [i], npr)
            else:
                break
    
    for c in C:
        buildR(0, c, [], 1)
        
    Rx = []
    
    def extendR(iS, pr):
            for i in range(iS, len(P4n3)):
                npr = pr * P4n3[i]
                if npr <= n:
                    nonlocal Rx
                    Rx += [npr]
                else:
                    break
                
                if npr * P4n3[i] <= n:
                    extendR(i, npr)
    
    for r in R:
        extendR(0, r)
            
    
    return sum(R + Rx)
