# Vieme, ze produkt 9, (1,2,3,4,5) concatovany je 918273645, aby bol cc produkt vacsi, plati:
# jednocifernym vacsi produkt nedostaneme
# dvojciferne by muselo byt vacsie ako 91, co nam dava 2 a 3- nasobok 3 ciferny, teda 8 cifier - nepandigitalne
# trojciferne by muselo byt vacsie ako 918, co nam dava 2 a 3- nasobok 4 ciferny, teda dokopy 11 cifier - nepandigitalne
# hladame 4 - ciferne cislo vacsie ako 9182

from itertools import permutations

def concatenatedPandigitality(L):
    s = ''
    for l in L:
        s += str(l)
    ss = set(s)
    return len(ss) == 9 and '0' not in ss

def problem38():
    P = list(permutations([str(x) for x in range(1, 10)], 4))
    LP = 0
    
    for i in range(8*8*7*6 + 6*6, len(P)):              # zacinam na permutacii 9182
        ip = int(''.join(P[i]))
        if concatenatedPandigitality([ip, 2*ip]):
            LP = ip
    
    return LP*10**5 + 2*LP
