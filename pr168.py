def pr168(o, O):
    M = 10**5
    s = 0
    for k in range(o, O):
        for l in range(1, 10):
            for c in range(1, 10):
                nm = c*(10**k - 1)
                dn = 10*l - 1
                if nm % dn == 0:
                    m = nm // dn
                    if 10**(k - 1) < m < 10**k:
                        print(m)
                        s = (s + m) % M

    return s
