from numpy import base_repr
from itertools import permutations

def changeBaseNP(bi, bo, n):
    de = int(n, bi)
    return base_repr(de, bo)
    
def isPandigital(b, n):
    s = set(n)
    return len(s) == b
    
def isNSuperPand(N, c):         # predpoklada, ze je N-pandigitalne
    for b in range(N - 1, 1, -1):
        if not isPandigital(b, changeBaseNP(N, b, c)):
            return False
    
    return True
    
    
def sumSuperPand(n):                # bezi dlho, pre n = 12 cca 20 min
    D = []
    for i in range(n):
        if i < 10:
            D.append(chr(i + 48))
        else:
            D.append(chr(i + 55))
    
    SP = []
    c = 10
    def genNPand(Di, cn, n):
        if len(Di) == 1:
            cn += Di[0]
            if isNSuperPand(n, cn):
                nonlocal c
                c -= 1
                nonlocal SP
                SP.append(int(cn, n))
        else:
            for i in range(len(Di)):
                if len(Di) == n and Di[i] == '0':
                    continue
                genNPand(Di[:i] + Di[i + 1:], cn + Di[i], n)
                if c < 1:
                    return
    
    genNPand(D, '', n)
    return sum([int(a) for a in SP])
    
def sumSuperPandPerms(n):           # bezi o nieco malo kratsie
    D = []
    for i in range(n):
        if i < 10:
            D.append(chr(i + 48))
        else:
            D.append(chr(i + 55))
    
    c = 10
    SP = []
    for p in permutations(D):
        m = ''.join(p)
        if m[0] != '0':
            if isNSuperPand(n, m):
                c -= 1
                SP.append(int(m, n))
                if c == 0:
                    return sum([int(a) for a in SP])
                    
                    
def isNSuperPand12(c):
    if int(c, 12) % 11 != 0:
        return False
    
    for b in range(11, 3, -1):
        if not isPandigital(b, changeBaseNP(12, b, c)):
            return False
    
    return True
                    

def sumSuperPandPerms12():           # bezi o nieco malo kratsie
    D = []
    for i in range(12):
        if i < 10:
            D.append(chr(i + 48))
        else:
            D.append(chr(i + 55))
    
    c = 10
    SP = []
    for p in permutations(D):
        m = ''.join(p)
        if m[0] != '0':
            if isNSuperPand12(m):
                c -= 1
                SP.append(int(m, 12))
                if c == 0:
                    return sum([a for a in SP])
