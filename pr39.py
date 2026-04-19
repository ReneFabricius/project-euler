from pythagoreanTriplets import EuklidsFormPeriNG

def problem39(l):
    C = [0] * (l + 1)
    T = EuklidsFormPeriNG(l)
    for t in T:
        for p in range(t[3], l + 1, t[3]):
            C[p] += 1
    
    return C.index(max(C))
    
