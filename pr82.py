def importMatrix(fn, w, h):
    M = [[0 for x in range(w)] for y in range(h)]
    f = open(fn, 'r')
    y = 0
    for line in f:
        cL = line.split(",")
        for x in range(len(cL)):
            M[y][x] = [int(cL[x]), -1, False, 0]                # hodnota policka, najkratsia cesta do neho, zafixovany, smer prichodu: 0 - zaciatok, 1 - zlava, 2 - zhora, 3 - zdola
        y += 1
    f.close()
    return M
    

    
def problem82():
    fn = 'p082_matrix.txt'
    w, h = 80, 80
    M = importMatrix(fn, w, h)
    
    mD = 10**10
    fst = True
    
    for r in range(h):
        
        if not fst:
            for y in range(h):
                for x in range(w):
                    M[y][x][1::] = [-1, False, 0]
        else:
            fst = False
        
        
        D = [(r, 1)]                        # Dosiahnutelne body, moze obsahovat jeden bod viac krat
        M[r][1][1] = M[r][0][0] + M[r][1][0]
        M[r][1][3] = 1
        if r > 0:
            D += [(r - 1, 0)]
            M[r - 1][0][1] = M[r][0][0] + M[r - 1][0][0]
            M[r - 1][0][3] = 3
        if r < h - 1:
            D += [(r + 1, 0)]
            M[r + 1][0][1] = M[r][0][0] + M[r + 1][0][0]
            M[r + 1][0][3] = 2
        fp = 0
        while True:
            mdp = M[D[0][0]][D[0][1]]           # dosiahnutelny bod s minimalnou vzdialenostou
            mdpyx = D[0]
            for d in D:
                if M[d[0]][d[1]][1] < mdp[1]:
                    mdp = M[d[0]][d[1]]
                    mdpyx = d
                    
            mdp[2] = True
            D.remove(mdpyx)
                
            
            if mdpyx[1] == w - 1:
                fp = list(mdpyx) + mdp
                break
            
            if not M[mdpyx[0]][mdpyx[1] + 1][2]:
                if M[mdpyx[0]][mdpyx[1] + 1][1] < 0 or M[mdpyx[0]][mdpyx[1] + 1][1] > M[mdpyx[0]][mdpyx[1] + 1][0] + mdp[1]:
                    if M[mdpyx[0]][mdpyx[1] + 1][1] < 0:
                        D.append((mdpyx[0], mdpyx[1] + 1))
                    M[mdpyx[0]][mdpyx[1] + 1][1] = M[mdpyx[0]][mdpyx[1] + 1][0] + mdp[1]
                    M[mdpyx[0]][mdpyx[1] + 1][3] = 1
            
            if mdpyx[0] < h - 1 and not M[mdpyx[0] + 1][mdpyx[1]][2]:
                if M[mdpyx[0] + 1][mdpyx[1]][1] < 0 or M[mdpyx[0] + 1][mdpyx[1]][1] > M[mdpyx[0] + 1][mdpyx[1]][0] + mdp[1]:
                    if M[mdpyx[0] + 1][mdpyx[1]][1] < 0:
                        D.append((mdpyx[0] + 1, mdpyx[1]))
                    M[mdpyx[0] + 1][mdpyx[1]][1] = M[mdpyx[0] + 1][mdpyx[1]][0] + mdp[1]
                    M[mdpyx[0] + 1][mdpyx[1]][3] = 2
                    
            if mdpyx[0] > 0 and not M[mdpyx[0] - 1][mdpyx[1]][2]:
                if M[mdpyx[0] - 1][mdpyx[1]][1] < 0 or M[mdpyx[0] - 1][mdpyx[1]][1] > M[mdpyx[0] - 1][mdpyx[1]][0] + mdp[1]:
                    if M[mdpyx[0] - 1][mdpyx[1]][1] < 0:
                        D.append((mdpyx[0] - 1, mdpyx[1]))
                    M[mdpyx[0] - 1][mdpyx[1]][1] = M[mdpyx[0] - 1][mdpyx[1]][0] + mdp[1]
                    M[mdpyx[0] - 1][mdpyx[1]][3] = 3
                
        if fp[3] < mD:
            mD = fp[3]
        
                
    
    return mD
        
    
    
    
    

