from math import sqrt
from Pell_equation import pellEqu
import gmpy2

def problem94BruteForce(l):
    gmpy2.get_context().precision = 100
    T = []
    for a in range(3, (10**l - 1) // 3, 2):
        d1 = 3*a*a-2*a-1
        d2 = d1 + 4*a
        if gmpy2.sqrt(d1) % 1 == 0:
            T += [(a, a, a + 1)]
        if gmpy2.sqrt(d2) % 1 == 0:
            T +=[(a, a, a - 1)]
    
    s = 0
    for t in T:
        s += sum(t)
    return T, s

# komentar od "danzat" na strane 2
def problem94PellEq(l):
    fs = pellEqu(3, 1)[0]
    ks = fs
    Ap = 2*(2 + sqrt(1 + 3*ks[1]**2))/3 - 1
    Am = 2*(1 + sqrt(1 + 3*ks[1]**2))/3 - 1
    rl = 10**l
    T = []
    while Ap <= (rl - 1) / 3 - 1 or Am <= (rl - 1) / 3:
        if Ap % 1 == 0:
            T += [(Ap, Ap, Ap + 1)]
        if Am % 1 == 0:
            T += [(Am, Am, Am - 1)]
        
        ks = (fs[0]*ks[0] + 3*fs[1]*ks[1], fs[0]*ks[1] + fs[1]*ks[0])
        Ap = 2*(2 + sqrt(1 + 3*ks[1]**2))/3 - 1
        Am = 2*(1 + sqrt(1 + 3*ks[1]**2))/3 - 1
    
    s = 0
    for t in T:
        s += sum(t)
    
    s -= 2          # riesenie 1, 1, 0
    return T, s
    
def compMods():
    print("\tA + 1\tA - 1")
    for r in range(16):
        print(str(r) + "\t" + str((3*r**4 + 4*r**3 - 2*r**2 - 4*r - 1) % 16) + "\t" + str((3*r**4 - 4*r**3 - 2*r**2 + 4*r - 1) % 16))
    
    # Teda trojuholniky so stranami A, A, A - 1 a A, A, A + 1 mozu mat celociselny obsah len pri neparnych A
