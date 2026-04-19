import primes


def mod_tot(m, PL):
    c = m
    mask = 1
    p_count = len(PL)
    mask_lim = 2**p_count
    while mask < mask_lim:
        pos_count = 0
        ch = 1
        ind = 0
        cur_num = m
        while ch < mask_lim:
            if (ch & mask) > 0:
                pos_count += 1
                cur_num /= PL[ind]

            ch <<= 1
            ind += 1

        c += (-1 if pos_count & 1 else 1)*int(cur_num)
        mask += 1

    return c


def pr634(n):
    b_lim = int((n/4)**(1/3)) + 1
    DEC = primes.rangePrimeFactDecomposition(b_lim)
    c = 0

    for b in range(2, b_lim):
        val = True
        PS = []
        for p in DEC[b]:
            if DEC[b][p] & 1 == 0:
                val = False
                break
            elif DEC[b][p] != 1:
                PS.append(p)

        if val:
            sq_bases = int((n/b**3)**(1/2))
            fitting_c = mod_tot(sq_bases, PS) - 1
            c += fitting_c

    return c
