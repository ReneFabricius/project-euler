def getDigits(n):
    D = []
    while n:
        D += [n % 10]
        n //= 10
    return list(reversed(D))

def isPalindrome(D):
    a = 0
    b = len(D) - 1
    while a < b:
        if D[a] != D[b]:
            return False
        a += 1
        b -= 1
        
    return True
    
    
def isLychel(n):
    D = getDigits(n)
    for i in range(49):
        n += sum(D[i] * 10**i for i in range(len(D)))
        D = getDigits(n)
        if isPalindrome(D):
            return False
    
    return True

def lychelCount():
    c = 0
    for n in range(1, 10000):
        if isLychel(n):
            c += 1
    
    return c
