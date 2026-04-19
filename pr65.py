from fractions import Fraction

def nthCoef(n):
    if n == 1:
        return 2
    
    if n % 3 == 0:
        return n // 3 * 2
    
    return 1

def nthConv(n):
    if n == 1:
        return nthCoef(n)
    f = Fraction(1, nthCoef(n))
    for i in range(n - 1, 1, -1):
        f = Fraction(1, nthCoef(i) + f)
    
    return nthCoef(1) + f
    
def problem65(n):
    c = nthConv(n)
    n = c.numerator
    s = 0
    while n:
        s += n % 10
        n //= 10
    
    return s
