from math import sqrt, log
from collections import Counter
from itertools import combinations, product
from primes import primes

def isPandigital(n):
    d = int(log(n, 10)) + 1
    D = set()
    while n:
        D.add(n % 10)
        n //= 10
    
    if len(D) == d and 0 not in D:
        return True
        
    return False
    
def isPandigList(L):
    S = set(range(1,10))
    D = set()
    for n in L:
        if hasattr(n, '__iter__'):
            for nn in n:
                while nn:
                    D.add(nn % 10)
                    nn //= 10
        else:
            while n:
                D.add(n % 10)
                n //= 10
    
    return S == D

def pandigPrimesBel():
    P = primes(98765432)
    Pp = []
    for p in P:
        if isPandigital(p):
            Pp += [p]
    
    Pn = [[] for k in range(8)]
    
    i = 0
    for pp in Pp:
        if pp >= 10**(i + 1):
            i += 1
        Pn[i] += [pp]
    
    c = 0
    for p8 in Pn[7]:
        for p1 in Pn[0]:
            if isPandigList([p1, p8]):                                                  # 8, 1
                c += 1
                
    for p7 in Pn[6]:
        for p2 in Pn[1]:
            if isPandigList([p7, p2]):                                                  # 7, 2
                c += 1
                
        for p1i in range(len(Pn[0])):
            for p1j in range(p1i + 1, len(Pn[0])):
                if isPandigList([p7, Pn[0][p1i], Pn[0][p1j]]):                          # 7, 1, 1
                    c += 1
                    
    for p6 in Pn[5]:
        for p3 in Pn[2]:
            if isPandigList([p6, p3]):                                                  # 6, 3
                c += 1
        
        for p2 in Pn[1]:
            for p1 in Pn[0]:
                if isPandigList([p6, p2, p1]):                                          # 6, 2, 1
                    c += 1
        
        for p1i in range(len(Pn[0])):
            for p1j in range(p1i + 1, len(Pn[0])):
                for p1k in range(p1j + 1, len(Pn[0])):
                    if isPandigList([p6, Pn[0][p1i], Pn[0][p1j], Pn[0][p1k]]):          # 6, 1, 1, 1
                        c += 1
    
    for p5 in Pn[4]:
        for p4 in Pn[3]:
            if isPandigList([p5, p4]):                                                  # 5, 4
                c += 1
        
        for p3 in Pn[2]:
            for p1 in Pn[0]:
                if isPandigList([p5, p3, p1]):                                          # 5, 3, 1
                    c += 1
        
        for p2i in range(len(Pn[1])):
            for p2j in range(p2i + 1, len(Pn[1])):
                if isPandigList([p5, Pn[1][p2i], Pn[1][p2j]]):                          # 5, 2, 2
                    c += 1
            
            for p1i in range(len(Pn[0])):
                for p1j in range(p1i + 1, len(Pn[0])):
                    if isPandigList([p5, Pn[1][p2i], Pn[0][p1i], Pn[0][p1j]]):          # 5, 2, 1, 1
                        c += 1
        
        if isPandigList(Pn[0] + [p5]):                                                  # 5, 1, 1, 1, 1
            c += 1
    
    for p4i in range(len(Pn[3])):
        for p4j in range(p4i + 1, len(Pn[3])):
            for p1 in Pn[0]:
                if isPandigList([Pn[3][p4i], Pn[3][p4j], p1]):                          # 4, 4, 1
                    c += 1
        
        for p3 in Pn[2]:
            for p2 in Pn[1]:
                if isPandigList([Pn[3][p4i], p3, p2]):                                  # 4, 3, 2
                    c += 1
                    
            for p1i in range(len(Pn[0])):
                for p1j in range(p1i + 1, len(Pn[0])):
                    if isPandigList([Pn[3][p4i], p3, Pn[0][p1i], Pn[0][p1j]]):          # 4, 3, 1, 1
                        c += 1
        
        for p2i in range(len(Pn[1])):
            for p2j in range(p2i + 1, len(Pn[1])):
                for p1 in Pn[0]:
                    if isPandigList([Pn[3][p4i], Pn[1][p2i], Pn[1][p2j], p1]):          # 4, 2, 2, 1
                        c += 1
            
            for p1i in range(len(Pn[0])):
                for p1j in range(p1i + 1, len(Pn[0])):
                    for p1k in range(p1j + 1, len(Pn[0])):
                        if isPandigList([Pn[3][p4i], Pn[1][p2i], Pn[0][p1i], Pn[0][p1j], Pn[0][p1k]]):  # 4, 2, 1, 1, 1
                            c += 1
        
    for p3i in range(len(Pn[2])):
        for p3j in range(p3i + 1, len(Pn[2])):
            for p3k in range(p3j + 1, len(Pn[2])):
                if isPandigList([Pn[2][p3i], Pn[2][p3j], Pn[2][p3k]]):                  # 3, 3, 3
                    c += 1
            
            for p2 in Pn[1]:
                for p1 in Pn[0]:
                    if isPandigList([Pn[2][p3i], Pn[2][p3j], p2, p1]):                  # 3, 3, 2, 1
                        c += 1
                        
            for p1i in range(len(Pn[0])):
                for p1j in range(p1i + 1, len(Pn[0])):
                    for p1k in range(p1j + 1, len(Pn[0])):
                        if isPandigList([Pn[2][p3i], Pn[2][p3j], Pn[0][p1i], Pn[0][p1j], Pn[0][p1k]]):  # 3, 3, 1, 1, 1
                            c += 1
                    
        for p2i in range(len(Pn[1])):
            for p2j in range(p2i + 1, len(Pn[1])):
                for p2k in range(p2j + 1, len(Pn[1])):
                    if isPandigList([Pn[2][p3i], Pn[1][p2i], Pn[1][p2j], Pn[1][p2k]]):  # 3, 2, 2, 2
                        c += 1
                        
                for p1i in range(len(Pn[0])):
                    for p1j in range(p1i + 1, len(Pn[0])):
                        if isPandigList([Pn[2][p3i], Pn[1][p2i], Pn[1][p2j], Pn[0][p1i], Pn[0][p1j]]):  # 3, 2, 2, 1, 1
                            c += 1
                            
            if isPandigList(Pn[0] + [Pn[2][p3i]] + [Pn[1][p2i]]):                       # 3, 2, 1, 1, 1, 1
                c += 1
                        
    for p2i in range(len(Pn[1])):
        for p2j in range(p2i + 1, len(Pn[1])):
            for p2k in range(p2j + 1, len(Pn[1])):
                for p2l in range(p2k + 1, len(Pn[1])):
                    for p1 in Pn[0]:
                        if isPandigList([Pn[1][p2i], Pn[1][p2j], Pn[1][p2k], Pn[1][p2l], p1]):      # 2, 2, 2, 2, 1
                            c += 1
                            
                for p1i in range(len(Pn[0])):
                    for p1j in range(p1i + 1, len(Pn[0])):
                        for p1k in range(p1j + 1, len(Pn[0])):
                            if isPandigList([Pn[1][p2i], Pn[1][p2j], Pn[1][p2k], Pn[0][p1i], Pn[0][p1j], Pn[0][p1k]]):     # 2, 2, 2, 1, 1, 1
                                c += 1

    return c
    

def pandigPrimesBel1():
    P = primes(98765432)
    Pp = []
    for p in P:
        if isPandigital(p):
            Pp += [p]
    
    Pn = [[] for k in range(8)]
    
    i = 0
    for pp in Pp:
        if pp >= 10**(i + 1):
            i += 1
        Pn[i] += [pp]
    
    global S
    S = []
    def findCombs(i, r, C):
        global S
        if C[1] > 4:
            return
        if r == 0:
            S += [C]
            return
        for l in range(i, 0, -1):
            if r >= l:
                findCombs(l, r - l, C + Counter([l]))
     
    findCombs(8, 9, Counter())

    
    c = 0
    for C in S:
        L = []
        for e in C:
            if C[e] > 1:
                L.append(list(combinations(Pn[e - 1], C[e])))
            else:
                L.append(Pn[e - 1])
        P = list(product(*L))
        for p in P:
            if isPandigList(p):
                c += 1
    return c
