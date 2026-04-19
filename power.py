def expt_rec(a, b):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return a * expt_rec(a, b - 1)
    else:
        p = expt_rec(a, b / 2)
        return p * p
