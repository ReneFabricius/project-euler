
import math

def pr686(L, n):
    count = 0
    cur_n = L
    mult = 1
    last_pow = 0
    DIFS = []
    MCS = []
    if math.log2(L) % 1 == 0:
        count += 1
        last_pow = int(math.log2(L))

    mc = 0
    while count != n:
        bit_l = cur_n.bit_length()
        add_m = (1 << bit_l) - cur_n
        if add_m < mult:
            if last_pow > 0:
                DIFS.append(bit_l - last_pow)
                MCS.append(mc)

            last_pow = bit_l
            count += 1

        mult *= 10
        cur_n *= 10
        mc += 1

    return last_pow


def pr686_fast(L, n):
    count = 0
    i = 0
    last_exp = 0

    l2p = math.log2(L)
    l210 = math.log2(10)
    ln2 = math.log(2)
    lnp1 = math.log(L + 1)
    ln10 = math.log(10)

    while count < n:
        exp = math.ceil(l2p + i*l210)
        if ln2*exp < lnp1 + i*ln10:
            count += 1
            last_exp = exp

        i += 1

    return last_exp


def ugly_hack(n):
    des = 123
    cur_p = 90
    count = 1
    cur_n = 1 << cur_p
    DS = [196, 289]
    while count < n:
        can0 = cur_n << DS[0]
        if can0 // (10**((int)(math.log10(can0)) - 2)) == des:
            cur_p += DS[0]
            cur_n = can0
        else:
            can1 = cur_n << DS[1]
            if can1 // (10**((int)(math.log10(can1)) - 2)) == des:
                cur_p += DS[1]
                cur_n = can1
            else:
                can2 = cur_n << (DS[0] + DS[1])
                cur_p += DS[0] + DS[1]
                cur_n = can2

        count += 1

    return cur_p
