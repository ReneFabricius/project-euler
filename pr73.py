from math import ceil, gcd
    
def problem73(d, ff, sf):
    "Spocita pocet prvkov vo Fareyho postupnosti pre d medzi ff a sf"
    F = [ff, sf]
    f = False
    while not f:
        f = True
        Fn = []
        for i in range(len(F) - 1):
            Fn.append(F[i])
            nf = (F[i][0] + F[i + 1][0], F[i][1] + F[i + 1][1])
            if nf[1] <= d:
                Fn.append(nf)
                f = False
        Fn.append(F[-1])
        F = Fn
    
    return F, len(F) - 2
    
def problem73Count(d, ff, sf):
    fd = ff[0] / ff[1]
    sd = sf[0] / sf[1]
    c = 0
    for dv in range(ff[1]+sf[1], d + 1):
        for n in range(ceil(fd * dv), int(sd * dv) + 1):
            if gcd(dv, n) == 1:
                c += 1

    return c
