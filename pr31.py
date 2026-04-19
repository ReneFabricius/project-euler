def problem31(S):
    C = [1, 2, 5, 10, 20, 50, 100, 200]
    p1 = S
    c = 0
    
    def addCoins(p):
        nonlocal p1
        nonlocal c
        if p == 1:
            c += p1 // C[p] + 1
        else:
            for i in range(0, p1 // C[p] + 1):
                p1 -= i * C[p]
                addCoins(p - 1)
                p1 += i * C[p]
    
    addCoins(len(C) - 1)
    return c
