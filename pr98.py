from itertools import combinations
from collections import Counter
from math import sqrt, ceil

# Najdem vsetky dvojice permutacii zadanych slov, ulozim ich do dict podla permutacii kde cislujem velkymi pismenami, povodna permutacia je ABC..., v pripade, ze sa nejake pismeno opakuje (nastastie nanajvys jedno
# a nanajvys dva krat), oznacim toto pismeno 'a', v tomto pripade ulozim aj povodnu permutaciu, takze kluc ma format "povodne_poradie,permutacia", na zaklade tychto spermutovanych dvojic hladam permutacie stvorcov
# s rovnakou dlzkou a nasledne kontrolujem od najvacsej dlzky, ci pre permutaciu slov existuje permutacia stvorcov

def findSquarePerms(l):
    DS = {}
    for b in range(ceil(sqrt(10**(l - 1))), int(sqrt(10**l - 1)) + 1):
        sq = b*b
        k = ''.join(sorted(str(sq)))
        if k not in DS:
            DS[k] = []
        DS[k] += [sq]
    
    SP = {}
    for sp in DS:
        if len(DS[sp]) > 1:
            if len(sp) - len(set(sp)) == 1:         # s opakujucim sa cislom (v permutaciach zadanych slov sa opakuje nanajvys jeden znak a nanajvys dva krat)
                r = ''
                R = Counter(sp)
                for rr in R:
                    if R[rr] > 1:
                        r = rr
                        break
                
                for pair in combinations(DS[sp], 2):
                    sp0 = str(pair[0])
                    pp = []
                    c = 65
                    for ch in sp0:
                        if ch == r:
                            pp += ['a']
                        else:
                            pp += [chr(c)]
                            c += 1
                    pp += [',']
                    
                    for ch in str(pair[1]):
                        pp += [pp[sp0.index(ch)]]
                    
                    SP[''.join(pp)] = pair
            else:
                for pair in combinations(DS[sp], 2):
                    sp0 = str(pair[0])
                    pp = []
                    for ch in str(pair[1]):
                        pp += [chr(65 + sp0.index(ch))]
                    
                    SP[''.join(pp)] = pair
    
    return SP
    
def problem98():
    n = "p098_words.txt"
    f = open(n, "r")
    ct = f.read()
    f.close()
    ct = ct.split(",")
    DW = {}
    for w in ct:
        W = w[1:-1:]
        k = ''.join(sorted(W))
        if k not in DW:
            DW[k] = []
        DW[k] += [W]
    
    lengths = set()
    WP = {}
    for wp in DW:
        if len(DW[wp]) > 1:
            lengths.add(len(wp))
            if len(set(wp)) < len(wp):                  # s opakujucimi sa znakmi
                R = Counter(wp)
                DS = {}
                dc = 97     # 'a'
                for ch in R:
                    if R[ch] > 1:
                        DS[ch] = chr(dc)
                        dc += 1
                
                for pair in combinations(DW[wp], 2):
                    pp = []
                    c = 65                              # 'A'
                    for ch in pair[0]:
                        if ch in DS:
                            pp += [DS[ch]]
                        else:
                            pp += [chr(c)]
                            c += 1
                    pp += [',']
                    for ch in pair[1]:
                        pp += [pp[pair[0].index(ch)]]
                
                    WP[''.join(pp)] = pair
            
            else:                                       # bez opakujucich sa znakov
                for pair in combinations(DW[wp], 2):
                    pp = []
                    for ch in pair[1]:
                        pp += [chr(65 + pair[0].index(ch))]
                    
                    WP[''.join(pp)] = pair
    
    SQ = [{} for _ in range(max(lengths) + 1)]
    
    for l in reversed(sorted(lengths)):
        SQ[l] = findSquarePerms(l)
        Mn = 0
        for wpk in WP:
            if len(WP[wpk][0]) == l:
                if wpk in SQ[l]:
                    if max(SQ[l][wpk]) > Mn:
                        Mn = max(SQ[l][wpk])
        
        if Mn > 0:
            return Mn
    
