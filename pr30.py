def problem30(e):
    l = 0
    i = 1
    while (10**i - 1 <= i*9**e):
        l = i*9**e
        i += 1
    P = []
    for n in range(10, l + 1):
        cn = n
        s = 0
        while cn > 0:
            s += (cn % 10)**e
            cn //= 10
        if s == n:
            P += [n]
    
    return P, sum(P)
