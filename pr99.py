from math import log

def problem99():
    n = "p099_base_exp.txt"
    f = open(n, 'r')
    ln = 1
    Mln = 0
    Mv = 0
    for l in f:
        ls = l.split(',')
        v = int(ls[1]) * log(int(ls[0]))
        if v > Mv:
            Mv = v
            Mln = ln
        
        ln += 1
    f.close()
    return Mln
