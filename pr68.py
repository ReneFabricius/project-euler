from itertools import combinations, permutations

def problem68(T):
    R = []
    N = set(range(1, 2*T + 1))
    sols = set()
    for c in combinations(N, T):
        if sum(c) % T == 0:
            O = N - set(c)
            s = (sum(N) + sum(c)) // T
            for p in permutations(O, T):
                if p[0] > p[-1]:
                    continue
                    
                R = [[p[i], 0, 0] for i in range(T)]
                for ip in permutations(c, 2):
                    if sum(ip) + R[0][0] == s:
                        
                        for rli in range(T):
                            R[rli][1] = 0
                            R[rli][2] = 0
                        
                        cI = set(c) - set(ip)
                        R[0][1] = ip[0]
                        R[0][2] = ip[1]
                        R[1][1] = ip[1]
                        R[T-1][2] = ip[0]
                        acp = True
                        for rli in range(1, T - 1):
                            r = s - sum(R[rli])
                            if r in cI:
                                cI.remove(r)
                                R[rli][2] = r
                                R[rli + 1][1] = r
                            else:
                                acp = False
                                break
                        
                        if acp and sum(R[T - 1]) == s:
                            m = 2*T + 1
                            mi = 0
                            for li in range(T):
                                if R[li][0] < m:
                                    m = R[li][0]
                                    mi = li
                            
                            sol = []
                            for pi in range(mi, mi + T):
                                sol += R[pi % T]
                            
                            sols.add(''.join([str(x) for x in sol]))
    
    print(sols)
    
    Lsols = [int(xs) for xs in list(sols) if len(xs) == 16]
    return max(Lsols)
                        
                        
    
