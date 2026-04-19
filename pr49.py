from collections import Counter
from primes import primesRang, isPrime

def compareDigits(x, y):
    X = []
    while x:
        X.append(x % 10)
        x //= 10
    
    Y = []
    while y:
        Y.append(y % 10)
        y //= 10
    
    return Counter(X) == Counter(Y)
    
def findTriplets(d):
    s = 10**(d - 1)
    e = 10**d - 1
    P = primesRang(s, e)
    T = []
    for i1 in range(len(P)):
        p1 = P[i1]
        for i2 in range(i1 + 1, len(P)):
            p2 = P[i2]
            if (p2 - p1 > e - p2):
                break
            if compareDigits(p1, p2):
                p3 = p2 + p2 - p1
                if compareDigits(p2, p3):
                    if isPrime(p3):
                        T.append([p1, p2, p3])
    
    return T
