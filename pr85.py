def countRec(w, h):
    s = 0
    for rw in range(1, w + 1):
        hc = w - rw + 1
        for rh in range(1, h + 1):
            s += hc * (h - rh + 1)
    return s

def problem85(L):
    mD = L
    mG = (0, 0)
    h = 1
    cont = True
    while cont:
        w = h
        fst = True
        while True:
            c = countRec(w, h)
            if abs(L - c) < mD:
                mD = abs(L - c)
                mG = (w, h)
            if c > L:
                if fst:
                    cont = False
                break
            if fst:
                fst = False
            w += 1
        h += 1
    print(mG)
    return mG[0] * mG[1]
