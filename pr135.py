from math import ceil

def problem135(l, d):
    D = {}
    for x in range(1, l):
        y_l = ceil(l/x)
        if 3*x < y_l:
            y_l = 3*x
        y_s = 4 - (x%4)
        for y in range(y_s, y_l, 4):
            if not x*y in D:
                D[x*y] = 1
            else:
                D[x*y] += 1
    T = []
    for n in D:
        if D[n] == d:
            T += [n]
    return T
            
