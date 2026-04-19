

def problem61():
    PG = [[] for i in range(6)]
    pg = [0 for i in range(6)]
    end = False
    n = 1
    while not end:
        end = True
        pg[0] = n * (n + 1) // 2
        pg[1] = n * n
        pg[2] = n * (3*n - 1) // 2
        pg[3] = n * (2*n - 1)
        pg[4] = n * (5*n - 3) // 2
        pg[5] = n * (3*n - 2)
        
        for i in range(6):
            if pg[i] < 10000:
                end = False
                if pg[i] > 999:
                    PG[i] += [pg[i]]
        
        n += 1
    
    S = [[] for i in range(7)]
    
    for o in PG[5]:
        om = o % 100
        for pi in range(5):
            for pgn in PG[pi]:
                if pgn // 100 == om:
                    S[2] += [((5, pi), o, pgn)]
    
    for sl in range(3, 7):
        for prs in S[sl - 1]:
            prsm = prs[sl - 1] % 100
            for pi in range(5):
                if pi in prs[0]:
                    continue
                for pgn in PG[pi]:
                    if pgn // 100 == prsm:
                        S[sl] += [tuple([prs[0] + tuple([pi])]) + prs[1::] + tuple([pgn])]
    
    CS = []
    for fsl in S[6]:
        if fsl[1] // 100 == fsl[6] % 100:
            CS += [fsl]
    
    return CS, sum(CS[0][1::])
        
