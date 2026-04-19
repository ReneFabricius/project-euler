from pythagoreanTriplets import EuklidsFormPeriNG

def problem75(o):
    T = EuklidsFormPeriNG(o)
    Le = [0 for i in range(o + 1)]
    for t in T:
        for m in range(1, o // t[3] + 1):
            Le[t[3] * m] += 1
    
    c = 0
    for l in Le:
        if l == 1:
            c += 1
    
    return c
