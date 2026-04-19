
def bruteForce150():
    CG = []
    two_to_twenty = 2**20
    two_to_nineteen = 2**19
    t = 0
    for k in range(500500):
        t = (615949*t + 797807) % two_to_twenty 
        CG.append(t - two_to_nineteen)
    
    si = 0
    T = []
    for lnght in range(1, 1001):
        T.append(CG[si:si + lnght])
        si += lnght
    
    Tprec = []
    for row in range(1000):
        Tprec.append([T[row][0]])
        for col in range(1, row + 1):
            Tprec[row].append(Tprec[row][col - 1] + T[row][col])
    
    ms = 0
    for row in range(1000):
        for col in range(row + 1):
            acts = 0
            for size in range(1, 1000 - row + 1):
                if col == 0:
                    if col == row:
                        acts += Tprec[row + size - 1][-1]
                    else:
                        acts += Tprec[row + size - 1][col - row - 1]
                else:
                    if col == row:
                        acts += Tprec[row + size - 1][-1] - Tprec[row + size - 1][col - 1]
                    else:
                        acts += Tprec[row + size - 1][col - row - 1] - Tprec[row + size - 1][col - 1]
                
                if acts < ms:
                    ms = acts
    
    return ms
                
