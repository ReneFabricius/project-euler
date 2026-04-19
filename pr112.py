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
    
def problem112(p):
    b = 0
    n = 1
    while True:
        if isBouncy(n):
            b += 1
        if b >= p*n:
            break
        n += 1
    
    return b, n
