from diophantine_equation import quadraticDiophantineEq, ReccurentSolution

def problem100(m):
    # Diofanticka rovnica x*x + x -2*y*y - 2*y = 0, x + 1 je celkovy pocet, y + 1 je pocet modrych
    f, S = quadraticDiophantineEq(1, 0, -2, 1, -2, 0)
    R = []
    for rc in S[1]:
        R += [ReccurentSolution(*S[0], *rc)]
    
    pS = []
    for r in R:
        x, y = r.nextSol()
        while abs(x + 1) < m:
            x, y = r.nextSol()
        pS += [(x, y)]
    
    mD = m
    ms = (0, 0)
    for ps in pS:
        if ps[0] > 0:
            if ps[0] - m < mD:
                mD =  ps[0] - m
                ms = ps
    
    return ms[0] + 1, ms[1] + 1
