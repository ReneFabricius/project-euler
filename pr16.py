def sumOfDigPow2(p):
    n = 2**p
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    
    return s
