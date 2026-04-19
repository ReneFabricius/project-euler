from functools import lru_cache

def loadTriangle(fn):
    f = open(fn, 'r')
    T = []
    for l in f:
        sL = [int(n) for n in l.split()]
        T.append(sL)
    f.close()
    return T

def findPathRec():
    T = loadTriangle("p067_triangle.txt")
    l, P = findNext(T, 0, 0)
    P.reverse()
    return l, P
    
    
def findNext(T, y, x):
    if y == len(T) - 1:
        print("Returning from: " + str(x) + ", " + str(y))
        return T[y][x], [(y, x)]
        
    nL = findNext(T, y + 1, x)
    nR = findNext(T, y + 1, x + 1)
    if nL[0] > nR[0]:
        print("Returning from: " + str(x) + ", " + str(y))
        return nL[0] + T[y][x], nL[1] + [(y, x)]
    
    print("Returning from: " + str(x) + ", " + str(y))
    return nR[0] + T[y][x], nR[1] + [(y, x)]
    
