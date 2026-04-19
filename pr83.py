def importMatrix(fn, w, h):
    M = [[0 for x in range(w)] for y in range(h)]
    f = open(fn, 'r')
    y = 0
    for line in f:
        cL = line.split(",")
        for x in range(len(cL)):
            M[y][x] = [int(cL[x]), -1, False, 0]                # hodnota policka, najkratsia cesta do neho, zafixovany, smer prichodu: 0 - zaciatok, 1 - zlava, 2 - zhora, 3 - zdola, 4 - sprava
        y += 1
    f.close()
    return M
    

    
def problem83():
    fn = 'p083_matrix.txt'
    w, h = 80, 80
    M = importMatrix(fn, w, h)
    
    D = [(1, 0), (0, 1)]            # Dosiahnutelne body, moze obsahovat jeden bod viac krat
    
    M[0][0][1:-1:] = [M[0][0][0], True]
    M[1][0][1] = M[0][0][0] + M[1][0][0]
    M[1][0][3] = 2
    M[0][1][1] = M[0][0][0] + M[0][1][0]
    M[0][1][3] = 1
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
        
            
        
        if (mdpyx[0] == h - 1 and mdpyx[1] == w - 1):
            fp = list(mdpyx) + mdp
            break
            
        if mdpyx[0] < h - 1 and not M[mdpyx[0] + 1][mdpyx[1]][2]:                                                               # dole
            if M[mdpyx[0] + 1][mdpyx[1]][1] < 0 or M[mdpyx[0] + 1][mdpyx[1]][1] > M[mdpyx[0] + 1][mdpyx[1]][0] + mdp[1]:
                if M[mdpyx[0] + 1][mdpyx[1]][1] < 0:
                    D.append((mdpyx[0] + 1, mdpyx[1]))
                M[mdpyx[0] + 1][mdpyx[1]][1] = M[mdpyx[0] + 1][mdpyx[1]][0] + mdp[1]
                M[mdpyx[0] + 1][mdpyx[1]][3] = 2
                
                
        if mdpyx[1] < w - 1 and not M[mdpyx[0]][mdpyx[1] + 1][2]:                                                               # doprava
            if M[mdpyx[0]][mdpyx[1] + 1][1] < 0 or M[mdpyx[0]][mdpyx[1] + 1][1] > M[mdpyx[0]][mdpyx[1] + 1][0] + mdp[1]:
                if M[mdpyx[0]][mdpyx[1] + 1][1] < 0:
                    D.append((mdpyx[0], mdpyx[1] + 1))
                M[mdpyx[0]][mdpyx[1] + 1][1] = M[mdpyx[0]][mdpyx[1] + 1][0] + mdp[1]
                M[mdpyx[0]][mdpyx[1] + 1][3] = 1
        
        
        if mdpyx[1] > 0 and not M[mdpyx[0]][mdpyx[1] - 1][2]:                                                               # dolava
            if M[mdpyx[0]][mdpyx[1] - 1][1] < 0 or M[mdpyx[0]][mdpyx[1] - 1][1] > M[mdpyx[0]][mdpyx[1] - 1][0] + mdp[1]:
                if M[mdpyx[0]][mdpyx[1] - 1][1] < 0:
                    D.append((mdpyx[0], mdpyx[1] - 1))
                M[mdpyx[0]][mdpyx[1] - 1][1] = M[mdpyx[0]][mdpyx[1] - 1][0] + mdp[1]
                M[mdpyx[0]][mdpyx[1] - 1][3] = 4
                
        
        if mdpyx[0] > 0 and not M[mdpyx[0] - 1][mdpyx[1]][2]:                                                               # hore
            if M[mdpyx[0] - 1][mdpyx[1]][1] < 0 or M[mdpyx[0] - 1][mdpyx[1]][1] > M[mdpyx[0] - 1][mdpyx[1]][0] + mdp[1]:
                if M[mdpyx[0] - 1][mdpyx[1]][1] < 0:
                    D.append((mdpyx[0] - 1, mdpyx[1]))
                M[mdpyx[0] - 1][mdpyx[1]][1] = M[mdpyx[0] - 1][mdpyx[1]][0] + mdp[1]
                M[mdpyx[0] - 1][mdpyx[1]][3] = 2
    
    
    d = fp[3]
    
    
    return d
        
    
    
    
    

