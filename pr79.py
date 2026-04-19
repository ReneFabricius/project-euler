def problem79():
    f = open('p079_keylog.txt', 'r')
    fr = f.read().splitlines()
    f.close()
    D = [(set(), set()) for _ in range(10)]
    for l in fr:
        for di in range(len(l)):
            for pi in range(0, di):
                D[int(l[di])][0].add(int(l[pi]))
            for fi in range(di + 1, len(l)):
                D[int(l[di])][1].add(int(l[fi]))
    
    Rd = set()              # cifry ktore sa v hesle musia vyskytovat
    for d in range(10):
        Rd = Rd.union(D[d][0])
        Rd = Rd.union(D[d][1])
    
    P = []                  # heslo
    PS = set()              # heslo ako set
    Pf = set()              # cifry ktore este musia nasledovat za aktualnym heslom
    while Rd or Pf:
        Ad = []                                 # kandidati na dalsiu cifru v hesle (nepotrebuju pred sebou ziadnu cifru ktora by uz v hesle nebola)
        for d in range(10):
            if d in Rd or d in Pf:
                if not bool(D[d][0] - PS):
                    Ad += [d]
        
        Mr = -1
        Md = None                               # kandidat na dalsiu cifru v hesle ktory potrebuje za sebou najviac cifier
        for ad in Ad:
            if len(D[ad][1]) > Mr:
                Mr = len(D[ad][1])
                Md = ad
        
        Rd = Rd - set([Md])
        P += [Md]
        PS.add(Md)
        Pf = Pf - set([Md])
        Pf = Pf.union(D[Md][1])
    
    return ''.join([str(x) for x in P])
