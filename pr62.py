

def problem62(n):
    ci = 3
    cl = 2
    C = [[] for i in range(2)]
    while True:
        C += [[]]
        while True:
            cv = ci * ci * ci
            if len(str(cv)) > cl:
                break
            C[cl] += [cv]
            ci += 1
        
        for cncli in range(len(C[cl])):
            pc = 1
            scncl = sorted(str(C[cl][cncli]))
            for cni in range(cncli + 1, len(C[cl])):
                if sorted(str(C[cl][cni])) == scncl:
                    pc += 1
            
            if pc == n:
                return C[cl][cncli]
                
        
        cl += 1


def problem62better(n):
    ci = 3
    cl = 2
    
    while True:
        T = {}
        PA = []
        while True:
            cv = ci * ci * ci
            sscv = ''.join(sorted(str(cv)))
            if len(sscv) > cl:
                break
            l = T.setdefault(sscv, [])
            l.append(ci)
            if len(l) == n:
                PA.append(l)
            
            ci += 1
        
        PA = [pa for pa in PA if len(pa) == n]
        if PA:
            m = min(map(min, PA))
            return m, m**3
        
        cl += 1
        
