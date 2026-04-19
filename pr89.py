def readRomanNumber(R):
    V = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
    n = 0
    i = 0
    while i < len(R):
        if i + 1 < len(R) and V[R[i]] < V[R[i + 1]]:
            n += V[R[i + 1]] - V[R[i]]
            i += 2
        else:
            n += V[R[i]]
            i += 1
    return n
        
    
def writeRomanNumber(n):
    L = [(1000, 'M', True), (900, 'CM', False), (500, 'D', False), (400, 'CD', False), (100, 'C', True), (90, 'XC', False),
     (50, 'L', False), (40, 'XL', False), (10, 'X', True), (9, 'IX', False), (5, 'V', False), (4 , 'IV', False), (1, 'I', True)]
    R = ''
    for l in L:
        while n >= l[0]:
            n -= l[0]
            R += l[1]
            if not l[2]:
                break
    return R

def findImprovement():
    f = open('p089_roman.txt', 'r')
    ls = f.read().splitlines()
    f.close()
    c = 0
    for l in ls:
        ol = len(l)
        n = readRomanNumber(l)
        R = writeRomanNumber(n)
        nl = len(R)
        c += ol - nl
        
    return c
        
