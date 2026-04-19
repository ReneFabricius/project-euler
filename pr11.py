from functools import reduce

def importMatrix(fn, w, h):
    M = [[0 for x in range(w)] for y in range(h)]
    f = open(fn, 'r')
    y = 0
    for line in f:
        cL = line.split(" ")
        for x in range(len(cL)):
            M[y][x] = int(cL[x])
        y += 1
    f.close()
    return M

prod = lambda L: reduce(lambda x, y: x*y, L, 1)

def findLargstProd():
    w, h = 20, 20
    M = importMatrix("pr11_matrix.txt", w, h)
    m = 0
    d = 0
    mx, my = 0, 0
                
    for y in range(len(M)):
        for x in range(len(M[0])):
            if x + 3 < w:
                p = prod([y][x:x + 3])
                if (p > m):
                    m = p
                    d = "horizontalne"
                    mx, my = h, y
                
            if y + 3 < h:
                p = 1
                for i in range(4):
                    p *= M[y + i][x]
                if (p > m):
                    m = p
                    d = "vertikalne"
                    mx, my = x, h
            
            if x + 3 < w and y + 3 < h:
                p = 1
                for i in range(4):
                    p *= M[y + i][x + i]
                if (p > m):
                    m = p
                    d = "diagonalne vpravo dole"
                    mx, my = x, y
            
            if x - 3 >= 0 and y + 3 < h:
                p = 1
                for i in range(4):
                    p *= M[y + i][x - i]
                if (p > m):
                    m = p
                    d = "diagonalne vlavo dole"
                    mx, my = x, y
                
    return "Maximalny produkt: " + str(m) + " Z x: " + str(mx) + ", y: " + str(my) + " " + d
