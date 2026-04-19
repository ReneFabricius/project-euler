import math
from timeit import default_timer as timer


def substrsum(divs, digs, tens):
    ps = 0
    for i, d in enumerate(divs + [len(digs)]):
        m = 0
        for di in range(d - 1, divs[i - 1] - 1 if i > 0 else -1, -1):
            ps += tens[m]*digs[di]
            m += 1

    return ps


def move_divs(divs, digs_n):
    mi = 1
    while mi <= len(divs):
        if divs[-mi] < digs_n - mi:
            break
        mi += 1

    if mi > len(divs):
        return False

    start_p = divs[-mi] + 1
    for klm in range(mi, 0, -1):
        divs[-klm] = start_p + mi - klm

    return True


def pr719(N):
    start = timer()
    ret = 0
    checks = 0
    L = int(math.sqrt(N)) + 1
    tens = [int(10**i) for i in range(int(math.log10(N)) + 2)]
    for i in range(L):
        n = i*i
        if i % (L//100) == 0:
            print(i / (L//100))

        ndigs = []
        n_temp = n
        while n_temp:
            ndigs.append(n_temp % 10)
            n_temp //= 10

        ndigs.reverse()
        mnd = len(ndigs)
        while 9*(mnd - 1) + 10**(len(ndigs) - mnd + 1) - 1 < i:
            mnd -= 1

        found = False
        for nd in range(1, mnd):
            if found:
                break
            div = [k for k in range(1, nd + 1)]
            cont = True
            while cont:
                '''
                if int(sn[:div[0]]) > i:
                    break

                for aa in range(len(div)):
                    cp = int(sn[div[aa]: (div[aa + 1] if aa < len(div) - 1 else len(sn))])
                    if cp > i:
                        if div[aa] >= len(sn) - (len(div) - aa):
                            cont = False
                            break
                        else:
                            start_p = div[aa] + 1
                            for bb in range(aa, len(div)):
                                div[bb] = start_p + bb - aa
                            break

                if not cont:
                    break
                '''

                ps = substrsum(div, ndigs, tens)

                checks += 1
                if ps == i:
                    ret += n
                    found = True
                    break

                cont = move_divs(div, len(ndigs))

    return ret, checks, timer() - start