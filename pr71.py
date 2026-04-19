from fractions import Fraction

def problem71(de):
    "Najde najblizsi mensi zlomok ako 3 / 7 s menovatelom nepresahujucim de"
    n = 3
    d = 7
    rf = Fraction(n, d)
    
    mf = 0
    md = de
    for dl in range(2, d + 2):
        for nl in range(1, dl):
            fl = Fraction(nl, dl)
            if fl < rf and rf - fl < md:
                mf = fl
                md = rf - fl
    
    # Pre gn / gd plati : gn / gd < rf a zaroven (gn + 1) / gd > rf teda pre dany menovatel je to najblizsi zlomok k rf mensi ako rf (1)
    # (gn + 1) / (gd + 1) je pre gn < gd vacsie ako gn / gd (2)
    # Pripocitam 1 k citatelu, aj menovatelu, vznikne mi tak najvyssi citatel pre dany menovatel, pre ktory moze byt novy zlomok nizsi ako rf
    # (Viem, ze (gn + 1) / gd > rf teda podla (2) (gn + 2) / (gd + 1) > rf a zaroven zrejme gn / (gd + 1) < gn / gd - nie je teda pre menovatel gd + 1 ina moznost pre priblizenie sa k rf zdola)
    # V pripade, ze (gn + 1) / (gd + 1) > rf, zvysim menovatel o 1, znova, gn + 1 je jedina moznost ako sa pre menovatel gd + 2 zdola priblizit k rf, pretoze: podla (2) (gn + 2) / (gd + 2) > (gn + 1) / (gd + 1) > rf a zaroven
    # gn / (gd + 2) < gn / gd
    
    gn = mf.numerator + 1               
    gd = mf.denominator + 1
    while gd <= de:
        nf = Fraction(gn, gd)
        if nf > rf:
            gd += 1
        else:
            gn += 1
            gd += 1
        
        
            
        nf = Fraction(gn, gd)
        if nf > mf and nf < rf:
            mf = nf
    
    return mf
    
# Omnoho lepsie riesenie mozne pomocou http://www.cut-the-knot.org/blue/Farey.shtml
