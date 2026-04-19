from itertools import combinations

def isValidSet(S):
    l = len(S)
    for cl in range(2, l//2 + 1):
        for fc in combinations(S, cl):
            for sc in combinations(S - set(fc), cl):
                if sum(fc) == sum (sc):
                    return False
    
    return True

def problem105():
    n = "p105_sets.txt"
    f = open(n, 'r')
    s = 0
    for l in f:
        L = sorted([int(x) for x in l.split(',')])
        S = set(L)
        
        br = False
        for k in range(2, (len(L) + 2)//2 + 1):
            if sum(L[:k]) <= sum(L[-1:-k:-1]):
                br = True
                break
        
        if br:
            continue
        
        if isValidSet(S):
            s += sum(S)
    
    f.close()
    return s
        
