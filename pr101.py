import numpy.linalg

def P(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
    #return n**3
    
def problem101():
    C = 10
    B = [P(x) for x in range(1, C + 1)]
    s = 0
    for i in range(1, C + 1):
        M = numpy.matrix([[r**c for c in range(i)] for r in range(1, i + 1)])
        Pln = numpy.linalg.solve(M, B[:i])
        ps = 0
        for j in range(len(Pln)):
            ps += Pln[j]*(i + 1)**j
        s += ps
    
    return int(round(s))
