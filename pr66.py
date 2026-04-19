from Pell_equation import pellEqu

def problem66(lD):
    m = 0
    mD = 0
    for D in range(2, lD + 1):
        S = pellEqu(D, 1)
        if S:
            if S[0][0] > m:
                m = S[0][0]
                mD = D
    
    return mD
