def countNonBouncyBel(e):
    D_p = [1]*10
    I_p = [1]*9
    s = 0
    for i in range(e - 1):
        I = []
        for j in range(9):
            I += [sum(I_p[j::])]
        s += sum(I)
        I_p = I
        
        D = []
        for k in range(10):
            D += [sum(D_p[k::])]
        s += sum(D) - 10
        D_p = D
    
    return s + 9

def isBouncy(n):
    i = False
    d = False
    ldig = n % 10
    n //= 10
    while n:
        dig = n % 10
        n //= 10
        if dig > ldig:
            if i:
                return True
            d = True
        elif dig < ldig:
            if d:
                return True
            i = True
        ldig = dig
    
    return False
    
def countNonBouncyBelSimul(e):
    c = 0
    for nbr in range(1, 10**e):
        if not isBouncy(nbr):
            c += 1
    
    return c
