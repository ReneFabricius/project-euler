from copy import deepcopy

def solveSudoku(S):
    def guess(Z):
        def minCH():
            mch = 10
            mz = []
            for z in Z:
                if len(z[2]) < mch:
                    mch = len(z[2])
                    mz = z
                    
            return mz
    
        if not Z:
            return True
        
        cz = minCH()
        if len(cz[2]) == 0:
            return False
        
        for ch in list(cz[2]):
            nZ = deepcopy(Z)
            nZ.remove(cz)
            rr = range((cz[0] // 3) * 3, (cz[0] // 3) * 3 + 3)
            cr = range((cz[1] // 3) * 3, (cz[1] // 3) * 3 + 3)
            for nz in nZ:
                if nz[0] == cz[0] or nz[1] == cz[1] or (nz[0] in rr and nz[1] in cr):
                    nz[2].discard(ch)
            
            if guess(nZ):
                nonlocal S
                S[cz[0]][cz[1]] = ch
                return True
            
    Z = []
    n = set(range(1, 10))
    for r in range(9):
        for c in range(9):
            if S[r][c] == 0:
                cn = set()
                for i in range(9):
                    cn.add(S[r][i])
                    cn.add(S[i][c])
                for ri in range((r // 3) * 3, (r // 3) * 3 + 3):
                    for ci in range((c // 3) * 3, (c // 3) * 3 + 3):
                        cn.add(S[ri][ci])
                Z += [[r, c, n - cn]]
    
    if guess(Z):
        return S


    
    
def problem96():
    n = "p096_sudoku.txt"
    f = open(n, "r")
    s = 0
    while True:
        nl = f.readline()
        if nl == "":
            f.close()
            return s
        
        S = []
        for r in range(9):
            R = f.readline()
            R = R.rstrip()
            R = [int(ch) for ch in list(R)]
            S += [R]
        
        SS = solveSudoku(S)
        # print(SS)
        s += SS[0][0] * 100 + SS[0][1] * 10 + SS[0][2]
    
