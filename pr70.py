from math import sqrt
from collections import Counter
from primes import primes, totient

def isPermutation(x, y):
    X = []
    while x:
        X.append(x % 10)
        x //= 10
    
    Y = []
    while y:
        Y.append(y % 10)
        y //= 10
    
    return Counter(X) == Counter(Y)

def totientPermutationBel(n):
    "For n above 100000"
    P = primes(int(n/2) + 1)
    N = [75841]
    mT = 1.00874
    mP = 0
    for p in range(-1, -(len(P) + 1), -1):
        if (1/((1-1/P[p])*(1-1/(int(n/P[p])))) <= mT):
            mP = P[p]
            break
    
    P = primes(mP)
    print("Running for " + str(len(P)) + " primes, highest: " + str(mP))
    
    b = False
    for i in range(-1, -(len(P) + 1), -1):
        for j in range(i - 1, -(len(P) + 1), -1):
            if P[i] * P[j] < n:
                iT = 1 / ((1 - 1/P[i])*(1-1/P[j]))
                if iT >= mT:
                    if i - 1 == j:
                        b = True
                    break
                t = P[i]*P[j]*(1 - 1/P[i])*(1-1/P[j])
                if isPermutation(P[i]*P[j], t) and iT < mT:
                    N += [P[i] * P[j]]
                    mT = iT
        
        if b:
            break
    
    T = [k/totient(k) for k in N]
    return N[T.index(min(T))], N
