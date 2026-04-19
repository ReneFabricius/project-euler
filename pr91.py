from itertools import product

def problem91(l):
    c = 0
    P = list(product(range(l + 1), repeat = 2))
    for p1i in range(len(P)):
        for p2i in range(p1i + 1, len(P)):
            if (P[p1i][0] == 0 and P[p1i][1] == 0) or (P[p2i][0] == 0 and P[p2i][1] == 0):
                continue
            if P[p1i][0]*P[p2i][0] + P[p1i][1]*P[p2i][1] == 0:
                c += 1
                continue
            if P[p1i][0]*P[p1i][0] + P[p1i][1]*P[p1i][1] - P[p1i][0]*P[p2i][0] - P[p1i][1]*P[p2i][1] == 0:
                c += 1
                continue
            if P[p2i][0]*P[p2i][0] + P[p2i][1]*P[p2i][1] - P[p1i][0]*P[p2i][0] - P[p1i][1]*P[p2i][1] == 0:
                c += 1
    
    return c
