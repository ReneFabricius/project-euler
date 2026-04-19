def problem48(l):
    s = 0
    d = 10**10
    for i in range(1, l + 1):
        s += pow(i, i, d)
        s = s % d
    return s
