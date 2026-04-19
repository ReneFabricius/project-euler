from primes import primes

def problem37(l):
    T = []
    P = primes(l)
    PS = set(P)
    for p in P:
        if p > 7:
            i = 0
            t = True
            pp = p
            
            while pp > 9:
                pp //= 10
                i += 1
                if pp not in PS:
                    t = False
                    break
                
                
            
            pp = p
            while i > 0 and t:
                pp = pp % 10**i
                i -= 1
                if pp not in PS:
                    t = False
                    break
            
            if t:
                T += [p]
    
    return T
                
                
