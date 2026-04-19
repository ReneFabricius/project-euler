import gmpy2

def problem80(l):
    gmpy2.get_context().precision = 500
    s = 0
    for n in range(2, l + 1):
        sq = gmpy2.sqrt(n)
        if sq == int(sq):
            continue
        sq *= 10**(100 - int(gmpy2.log10(int(sq))) - 1)
        sq = int(sq)
        while sq:
            s += sq % 10
            sq //= 10
    
    return s
