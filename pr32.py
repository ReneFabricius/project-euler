from itertools import permutations

def problem32():
    S = set()
    d = set([str(x) for x in range(1, 10)])
    
    for i in range(1, 3):
        for p1 in permutations(d, i):
            p1i = int(''.join(p1))
            for p2 in permutations(d - set(p1), (9 - 2*i + 1) // 2):
                m = p1i * int(''.join(p2))
                if set(str(m)) == d - set(p1) - set(p2) and len(str(m)) == len(d) - len(p1) - len(p2):
                    S.add(m)
    
    return sum(S)
    
    
