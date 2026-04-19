from math import factorial

def nThPerm(n, d):
    n -= 1
    P = []
    R = [i for i in range(0, d)]
    for i in range(d - 1, 0, -1):
        o = n//factorial(i)
        P += [R[o]]
        R.remove(R[o])
        n -= o * factorial(i)
        
    P += [R[0]]
    
    return P
