from math import log
from fibonacci import fibonacciByMatrix

def isPandigital(c):
    P = set(range(1, 10))
    D = set()
    while c:
        D.add(c % 10)
        c //= 10
    return P == D
    
def fibonacciPandigEnd(n):
    "Najde fibonacciho cisla s pandigitalnym koncovym 9-cislim"
    a = 1
    b = 1
    Pd = []
    for n in range(3, n + 1):
        a, b = b, a + b
        a = a % 1000000000
        b = b % 1000000000
        
        if b >= 123456789 and b % 9 == 0:
            if isPandigital(b):
                Pd += [n]
                
    return Pd

def fibonacciPandig(n):
    Pe = fibonacciPandigEnd(n)
    for fi in Pe:
        f = fibonacciByMatrix(fi)
        df = int(log(f,10)) + 1         # Pocet cifier f
        f //= 10**(df-9)
        if isPandigital(f):
            return fi
    
    return "Not found"
        
        
