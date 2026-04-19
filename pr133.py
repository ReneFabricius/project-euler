from primes import primes
# prva verzia, lepsia v pr129.py

M = [[0] for i in range(10)]
M[1] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
M[3] = [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]
M[7] = [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
M[9] = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def findRepunit(p):
    ps = str(p)
    B = M[int(ps[-1])][1] * p
    f = str(M[int(ps[-1])][1])
    while B != 1:
        B //= 10
        d = B % 10
        r = 0
        if d > 1:
            r = 11 - d
        else:
            r = 1 - d
            
        m = M[int(ps[-1])][r]
        f += str(m)
        B += m * p
        
    
    return int(f[::-1]) * p

def sumPrimes(l):
    P = primes(l)
    s = 10              # 2 + 3 + 5
    for i in range(3, len(P)):
        n = len(str(findRepunit(P[i])))
        while n % 5 == 0:
            n //= 5
        while n % 2 == 0:
            n //= 2
        
        if n != 1:
            s += P[i]
    
    return s
