from itertools import combinations
from primes import primesRang

def exchangeDigits(n, d, d_p):
    "V cisle n zameni cifry na poziciach d_p za cifru d"
    n_s_l = list(str(n))
    for p in d_p:
        n_s_l[-1 - p] = str(d)
    return int(''.join(n_s_l))
    
    

def problem51(l):
    "Najde najmensie prvocislo z ktoreho sa zamenou jednej, alebo niekolkych cifier za lubovolne cifry (vsetky zamenene rovnake) da ziskat l prvocisiel"
    p_l = 2
    while True:
        P = primesRang(10**(p_l - 1), 10**p_l - 1)          # p_l - ciferne prvocisla
        PS = set(P)
        
        for p in P:
            d_l = 10 - l                                    # najvyssia cifra ktoru mozem zamienat, aby som mohol ziskat pozadovany pocet prvocisiel
            D = [[] for i in range(1, d_l + 2)]             # na i-tej pozicii: zoznam pozicii v cisle zprava od nuly na ktorych sa nachadza cifra i
            d_i = 1                                         # na nultu poziciu v prvocislach nemozem dosadit viac ako 4 cisla
            p_d = p//10
            while p_d:
                d = p_d % 10
                p_d //= 10
                if d <= d_l:
                    D[d] += [d_i]
                d_i += 1
            
            for d in range(0, len(D)):                      # cez potecionalne cifry na vymenu
                for c_l in range(1, len(D[d]) + 1):         # cez mozne dlzky ich kombinacii
                    for c in combinations(D[d], c_l):       # cez kombinacie danej dlzky
                        count = 1                           # pocet prvocisel zyskanych vymenami danej kombinacie pozicii
                        for d_e in range(d + 1, 10):        # cez moznych kandidatov na vymenu
                            pX = exchangeDigits(p, d_e, c)  # cislo s vymenenymi pozadovanymi ciframi
                            if pX in PS:
                                count += 1
                                if count == l:
                                    print("Prve cislo: " + str(p) + ", pozicie vymienanych cifier: " + str(c))
                                    return p
                            if 9 - d_e < l - count:
                                break                       # neostava dostatok kandidatov na vymenu, aby mohla byt uspokojena poziadavka na pocet prvocisel
                    
    
        p_l += 1
