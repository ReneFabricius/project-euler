import math


def pr172(n):
    c = 0
    Vs = [3, 2, 1]
    Cs = [0, 0, 0]
    Fs = [6, 2, 1]
    nf = math.factorial(n)
    ff = math.factorial(10) / 10 * 9
    fi = 0
    while True:
        ai = 0
        for j in range(fi, len(Cs)):
            Cs[j] = 0

        while sum([Cs[i] * Vs[i] for i in range(len(Cs))]) != n:
            Cs[fi + ai] = (n - sum([Cs[i] * Vs[i] for i in range(len(Cs))])) // Vs[fi + ai]
            ai += 1

        if sum(Cs) <= 10:
            cc = nf
            cc = cc / Fs[0]**Cs[0] / Fs[1]**Cs[1] / Fs[2]**Cs[2]
            cc = cc / math.factorial(Cs[0]) / math.factorial(Cs[1]) / math.factorial(Cs[2])
            cc = cc * ff / math.factorial(10 - sum(Cs))
            c += cc

        if Cs[1] != 0 and sum(Cs) < 10:
            Cs[1] -= 1
            fi = 2
        elif Cs[0] != 0:
            Cs[0] -= 1
            fi = 1
        else:
            break

    return c