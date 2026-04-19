

def simple_comb(a, b, n):
    L = []
    L.append((0, 0, 0))
    while len(L) <= n:
        mv = (n+1)*b
        mi = [0, 0]
        for pvi in range(len(L)):
            if L[-1][0] < L[pvi][0] + a < mv:
                mv = L[pvi][0] + a
                mi = [L[pvi][1] + 1, L[pvi][2]]
            if L[-1][0] < L[pvi][0] + b < mv:
                mv = L[pvi][0] + b
                mi = [L[pvi][1], L[pvi][2] + 1]

        L.append((mv, mi[0], mi[1]))

    return L


def real_exhaust_comb(a, b, n):
    L = [(a, 1, 0), (b, 0, 1)]
    ST = 10**25

    while len(L) <= n:
        Dn = {}
        Dc = {}
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                num = L[i][0] + L[j][0]
                com = (L[i][1] + L[j][1], L[i][2] + L[j][2])
                if num in Dn:
                    Dn[num] += 1
                else:
                    Dn[num] = 1
                    Dc[num] = com

        fn = ST
        for num in Dn:
            if Dn[num] == 1:
                if L[-1][0] < num < fn:
                    fn = num

        L.append((fn, Dc[fn][0], Dc[fn][1]))

    return L


def real_difs(a, b, n):
    L = real_exhaust_comb(a, b, n)
    D = []
    for i in range(1, len(L)):
        D.append(L[i][0] - L[i - 1][0])

    return L, D


def pr167(a, b, n):
    L = [(a, 1, 0, -1, -1), (b, 0, 1, -1, -1)]
    while len(L) < n:
        Dn = {}
        Di = {}
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                num = L[i][0] + L[j][0]
                ins = (i, j)
                if num in Dn:
                    Dn[num] += 1
                else:
                    Dn[num] = 1
                    Di[num] = ins

        cand = 10 ** 25
        for nc in Dn:
            if Dn[nc] == 1 and L[-1][0] < nc < cand:
                cand = nc

        L.append((cand,
                  L[Di[cand][0]][1] +
                  L[Di[cand][1]][1],
                  L[Di[cand][0]][2] +
                  L[Di[cand][1]][2],
                  Di[cand][0], Di[cand][1]))

    return L


def comp_difs(L):
    D = []
    for i in range(1, len(L)):
        D.append(L[i][0] - L[i - 1][0])

    return D


def find_cycles(D):
    mln = len(D)
    for ln in range(len(D) // 2, 0, -1):
        val = True
        for ii in range(ln, len(D)):
            if D[ii] != D[(ii % ln) + ln]:
                val = False
                break

        if val:
            mln = ln

    for s in range(mln):
        val = True
        for ss in range(s, len(D)):
            cp = ss
            while cp < len(D):
                if D[cp] != D[ss]:
                    val = False
                cp += mln

        if val:
            return s, mln


def print_cycles(a, b, n):
    L = pr167(a, b, n)
    D = comp_difs(L)
    s, l = find_cycles(D)
    for ss in range(s, s + l):
        cp = ss
        while cp < len(L):
            print('[' + str(cp) + '] ' + str(L[cp][0]) + ',' +
                  str(L[cp][3]) + ',' + str(L[cp][4])
                  + '\t')
            cp += l

        print('\n')


def try_find_cycle(L, Pos, rep, cont_inds):

    Inds = Pos[tuple(L[-1][cont_inds[i]] for i in range(len(cont_inds)))]
    for kk in range(len(Inds) - 2, -1, -1):
        ccl = Inds[-1] - Inds[kk]
        valid = True
        for ri in range(rep - 2):
            ri_loc = Inds[-1] - ccl * (ri + 2)
            if ri_loc < 0:
                valid = False
                break

            equals = True
            for ii in range(len(cont_inds)):
                equals &= (L[ri_loc][cont_inds[ii]] == L[-1][cont_inds[ii]])

            if not equals:
                valid = False
                break

        if valid:
            CYCS = []
            for lci in range(len(L) - 1, len(L) - 1 - ccl, -1):
                lcci = lci - ccl
                cyc_c = 0
                while lcci >= 0:
                    equals = True
                    for ii in range(len(cont_inds)):
                        equals &= (L[lci][cont_inds[ii]] == L[lcci][cont_inds[ii]])

                    if not equals:
                        break

                    cyc_c += 1
                    lcci -= ccl

                lcci += ccl

                if cyc_c < rep:
                    valid = False
                    break

                CYCS.append(cyc_c)

            if valid:
                min_cyc = min(CYCS)
                cyc_longer = min_cyc + 1
                last_longer = -1
                for lli in range(len(CYCS)):
                    if CYCS[lli] >= cyc_longer:
                        last_longer = lli
                    else:
                        break

                min_ind = len(L) - 1 - last_longer - cyc_longer * ccl

                if min_ind < len(L) // 2:
                    return min_ind, ccl

    return None


def compute_cycles(a, b, cont_inds):
    L = [(a, 1, 0, -1, -1, a), (b, 0, 1, -1, -1, b - a)]
    c_f = False
    M = 10**106
    A = set()
    U = set()
    C = {}

    step = 500
    repeats = 3
    Pos = {}

    while not c_f:
        jj = len(L) - 1
        for i in range(len(L) - 1):
            r = L[jj][0] + L[i][0]
            if r in A:
                if r in U:
                    U.remove(r)

            else:
                A.add(r)
                U.add(r)
                C[r] = (i, jj)

        mn = M
        for cn in U:
            if L[-1][0] < cn < mn:
                mn = cn

        L.append((mn, L[C[mn][0]][1] + L[C[mn][1]][1], L[C[mn][0]][2] + L[C[mn][1]][2], C[mn][0], C[mn][1] - len(L), mn - L[-1][0]))
        key = tuple(L[-1][cont_inds[i]] for i in range(len(cont_inds)))
        if key in Pos:
            Pos[key].append(len(L) - 1)
        else:
            Pos[key] = [len(L) - 1]

        if len(L) % step == 0:
            print("Testing " + str(len(L) // step))
            ret = try_find_cycle(L, Pos, repeats, cont_inds)
            if ret:
                return ret


def comp_L(a, b, n):
    L = [(a, 1, 0, -1, -1, a), (b, 0, 1, -1, -1, b - a)]
    M = 10 ** 106
    A = set()
    U = set()
    C = {}

    while len(L) < n:
        jj = len(L) - 1
        for i in range(len(L) - 1):
            r = L[jj][0] + L[i][0]
            if r in A:
                if r in U:
                    U.remove(r)

            else:
                A.add(r)
                U.add(r)
                C[r] = (i, jj)

        mn = M
        TR = []
        for cn in U:
            if L[-1][0] < cn < mn:
                mn = cn

            if cn <= L[-1][0]:
                TR.append(cn)

        for tr in TR:
            U.remove(tr)

        L.append(
            (mn, L[C[mn][0]][1] + L[C[mn][1]][1], L[C[mn][0]][2] + L[C[mn][1]][2], C[mn][0], C[mn][1] - len(L), mn - L[-1][0]))

    return L


def comp_combined(n):
    L = []
    for s in range(2, 11):
        L.append(comp_L(s, 2*s + 1, n))

    FL = [sum([L[li][ni][0] for li in range(len(L))]) for ni in range(n)]

    return FL


def save_to_file(L, f):
    file = open(f, 'w')
    for l in L:
        for li in range(len(l)):
            file.write(str(l[li]))
            file.write('\t\t')
        file.write('\n')

    file.close()