from continued_fractions import continuedFracSQroot
        
def problem64(b):
    c = 0
    for n in range(2, b + 1):
        F = continuedFracSQroot(n)
        if len(F) % 2 == 0:
            c += 1
    
    return c
