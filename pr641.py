import primes
import math
import more_itertools as mi

def incr_R(R, cur_r, PE, P, n):
    for ri in range(len(R) - 1, 0, -1):
        if R[ri - 1] > R[ri]:
            if cur_r * P[ri]**(PE[R[ri] + 1] - PE[R[ri]]) <= n:
                cur_r *= P[ri]**(PE[R[ri] + 1] - PE[R[ri]])
                R[ri] += 1
                return True, cur_r

        cur_r /= P[ri]**(PE[R[ri]])
        R[ri] = 0

    if R[0] < len(PE) - 1 and cur_r * P[0]**(PE[R[0] + 1] - PE[R[0]]) <= n:
        cur_r *= P[0]**(PE[R[0] + 1] - PE[R[0]])
        R[0] += 1
        return True, cur_r

    return False, cur_r


def count_divs(R, PE):
    cd = 1
    for i in range(len(R)):
        if R[i] == 0:
            return cd

        cd *= (PE[R[i]] + 1)

    return cd


def find_max_div_count(n):
    max_exp = int(math.log2(n))
    P = primes.primes(100)
    PE = [0]
    for i in range(1, max_exp + 1):
        if (i + 1) % 2 != 0 and (i + 1) % 3 != 0:
            PE.append(i)

    repr_len = 1
    k = 1
    i = 0
    while k <= n:
        repr_len = i
        k *= P[i]**PE[1]
        i += 1

    R = [0]*repr_len

    max_divs = 0
    cur_r = 1
    incrsd, cur_r = incr_R(R, cur_r, PE, P, n)
    while incrsd:
        c_divs = count_divs(R, PE)
        if c_divs > max_divs and c_divs % 6 == 1:
            max_divs = c_divs

        incrsd, cur_r = incr_R(R, cur_r, PE, P, n)

    return max_divs


def count_occurs(P, PCs, fc, n):
    fcr = []
    for e in fc:
        if e > 1:
            fcr.append(e - 1)
        else:
            break

    if len(fcr) == 1:
        return PCs[int(n**(1/fcr[0]))]

    c = 0
    for el in sorted(mi.distinct_permutations(fcr), reverse=True):
        indxs = [i for i in range(len(fcr) - 1)]
        fin = False
        while not fin:
            c_base = 1
            for eii in range(len(indxs)):
                c_base *= P[indxs[eii]]**el[eii]

            inc_last = True
            while inc_last:
                count = PCs[int((n/c_base)**(1/el[-1]))] - PCs[P[indxs[-1]]]

                if count <= 0:
                    break
                c += count
                c_base /= P[indxs[-1]]**el[-2]
                indxs[-1] += 1
                c_base *= P[indxs[-1]]**el[-2]

            inc_ind = len(indxs) - 2
            while inc_ind >= 0:
                start = indxs[inc_ind] + 1
                for ii in range(len(indxs) - inc_ind):
                    indxs[inc_ind + ii] = start + ii

                num = 1
                for ejj in range(len(indxs)):
                    num *= P[indxs[ejj]]**el[ejj]

                occur_c = PCs[int((n/num)**(1/el[-1]))] - PCs[P[indxs[-1]]]
                if occur_c <= 0:
                    inc_ind -= 1
                else:
                    break

            if inc_ind < 0:
                fin = True

    return c


def pr641(n):
    mdc = find_max_div_count(n)
    primes.initGlobalPrimes(int(math.sqrt(mdc) + 2))

    FCRZTSN = []
    i = 1
    while 6*i + 1 <= mdc:
        FCRZTSN += primes.all_decompositions_preinitialized_initializing(6*i + 1)
        i += 1

    max2p = math.log2(n)

    min_pow = 4
    prime_lim = int((n/2**min_pow)**(1/min_pow))
    if prime_lim < 10:
        prime_lim = 10
    P = primes.primes(prime_lim)
    PCs = [0]*(prime_lim + 1)
    pi = 0
    pc = 0
    for i in range(2, prime_lim + 1):
        if pi < len(P) and P[pi] == i:
            pc += 1
            pi += 1
        PCs[i] = pc

    c = 1 if n > 0 else 0

    CHSN = []
    for fc in FCRZTSN:
        if fc[0] - 1 > max2p:
            continue

        c += count_occurs(P, PCs, fc, n)

    return c