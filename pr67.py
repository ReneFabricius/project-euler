def loadTriangle(fn):
    f = open(fn, 'r')
    T = []
    for l in f:
        sL = [int(n) for n in l.split()]
        T.append(sL)
    f.close()
    return T

def findPath():
    T = loadTriangle("p067_triangle.txt")
    aT = [[] for i in range(len(T))]
    for y in range(len(T) - 1, -1, -1):
        for x in range(y + 1):
            if (y == len(T) - 1):
                aT[y] += [(T[y][x], [(y, x)])]
            else:
                if (aT[y + 1][x][0] > aT[y + 1][x + 1][0]):
                    aT[y] += [(T[y][x] + aT[y + 1][x][0], aT[y + 1][x][1] + [(y, x)])]
                else:
                    aT[y] += [(T[y][x] + aT[y + 1][x + 1][0], aT[y + 1][x + 1][1] + [(y, x)])]
    
    P = aT[0][0][1]
    P.reverse()
    l = aT[0][0][0]
    return l, P
