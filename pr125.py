def isPalindromic(n):
    sn = str(n)
    for i in range(int(len(sn)/2)):
        if sn[i] != sn[-(i+1)]:
            return False
    
    return True
    
def problem125(l):
    sp = 1
    L = []
    while True:
        s_s = sp*sp + (sp + 1)*(sp + 1)
        if s_s > l:
            break
        
        n = 2
        while s_s < l:
            if isPalindromic(s_s):
                L += [s_s]
            
            s_s += (sp + n)*(sp + n)
            n += 1
        
        sp += 1
    
    return sum(set(L))
