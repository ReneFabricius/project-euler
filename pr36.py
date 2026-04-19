def checkPalindromity(n):
    sn = str(n)
    sni = sn[::-1]
    return sn == sni
    
def problem36(l):
    L = []
    for i in range(1, l):
        if checkPalindromity(i) and checkPalindromity(bin(i)[2::]):
            L += [i]
    
    return L
    
        
