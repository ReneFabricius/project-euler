from primes import primes, isPrimeMillerRabin


def squbes_frm_prms(put):
    P = primes(put)
    SQ = []
    last_sq = P[0]**3*P[-1]**2
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            sq1 = P[i]**3*P[j]**2
            if sq1 > last_sq:
                break

            SQ.append(sq1)
            sq2 = P[i]**2*P[j]**3
            if sq2 <= last_sq:
                SQ.append(sq2)

    SQ.sort()
    return SQ


def is_p_proof(num):
    k = 15
    str_n = list(str(num))
    for di in range(len(str_n)):
        for i in range(10):
            str_m = str_n.copy()
            str_m[di] = i
            nnum = int(''.join([str(oo) for oo in str_m]))
            if isPrimeMillerRabin(nnum, k):
                return False

    return True


def pr200(k):
    ps = 1000
    fstr = '200'
    PPSQS = []
    last_instpected = None
    while True:
        print("Working with primes up to {}".format(ps))
        print("Retrieving squbes")
        SQ = squbes_frm_prms(ps)
        print("Squbes retrieved")
        if last_instpected is not None:
            ind = SQ.index(last_instpected)
            print("Continuing from index {}".format(ind + 1))
            SQ = SQ[ind + 1:]

        print("Squbes to inspect {}".format(len(SQ)))
        last_instpected = SQ[-1]
        for sq in SQ:
            sq_str = str(sq)
            if sq_str.find(fstr) >= 0:
                if is_p_proof(sq):
                    PPSQS.append(sq)
                    if len(PPSQS) == k:
                        return PPSQS

        ps *= 10

if __name__ == "__main__":
    pr200(50)


