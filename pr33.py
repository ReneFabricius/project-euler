from fractions import Fraction

def problem33():
    L = []
    N = 1
    D = 1
    for n in range(10, 100):
        for d in range(n+1, 100):
            i = set(str(n)).intersection(set(str(d)))
            if len(i) == 1 and i.copy().pop() != '0':
                nns = set(str(n)) - i
                nds = set(str(d)) - i
                if len(nns) == 1:
                    nn = int(nns.pop())
                else:
                    nn = int(i.pop())
                if len(nds) == 1:
                    nd = int(nds.pop())
                else:
                    nd = int(i.pop())
                if nd != 0 and n/d == nn/nd:
                    N *= nn
                    D *= nd
                    L += [(n, d)]
    
    return L, Fraction(N, D)
