def hexagons(m):
    s = 0
    c = 0
    for n in range(3, m + 1):
        for i in range(1, int(n/3) + 1):
            c += (n - (i * 3 - 1)) * i
        s += c
    return s

