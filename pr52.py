from collections import Counter

def getSetOfDigits(n):
    S = Counter()
    while n:
        S[n % 10] += 1
        n //= 10
    return S

def findPerm():
    i = 1
    while True:
        D = getSetOfDigits(i)
        for j in range (2, 7):
            S = getSetOfDigits(j * i)
            if D != S:
                break
            if j == 6:
                return i
        i += 1
