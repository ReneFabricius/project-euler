from euclidean_alg import lcm
from collections import defaultdict
from math import gcd


def cycles_naive(n):
    cycles = []
    for i in range(n):
        cyc = [i]
        while (cyc[-1] * i) % n != i:
            cyc.append((cyc[-1] * i) % n)

        cycles.append(cyc)
        print(f"cyc: {cyc},\t\tlen: {len(cyc)}")

    return cycles


def cycles_reuse(n):
    cyc_lens: list[None | int] = [None for _ in range(n)]
    for i in range(n):
        if cyc_lens[i] is not None:
            continue

        cur_cyc = [i]
        while (nxt := (cur_cyc[-1] * i) % n) != i:
            cur_cyc.append(nxt)

        for mem_pos, cyc_mem in enumerate(cur_cyc):
            if cyc_lens[cyc_mem] is not None:
                continue

            cyc_lens[cyc_mem] = lcm(mem_pos + 1, len(cur_cyc)) // (mem_pos + 1)

    return cyc_lens


def check_cyc_comp(n):
    cycles = cycles_naive(n)
    cyc_lens = cycles_reuse(n)
    for i in range(n):
        if len(cycles[i]) != cyc_lens[i]:
            print(
                f"Conflict for i: {i}, len: {len(cycles[i])}, computed: {cyc_lens[i]}, cycle: {cycles[i]}"
            )


def pr182(p, q):
    phi = (p - 1) * (q - 1)
    cyc_lens = cycles_reuse(p * q)
    len_occurs = defaultdict(int)
    for cyc_len in cyc_lens:
        len_occurs[cyc_len] += 1

    eq_pow_occurs = [0 for _ in range(phi)]
    for cyc_len, occurences in len_occurs.items():
        k = 0
        while 1 + k * cyc_len < phi:
            eq_pow_occurs[1 + k * cyc_len] += occurences
            k += 1

    occur_lens = defaultdict(list)
    for eq_pow, occurs in enumerate(eq_pow_occurs):
        occur_lens[occurs].append(eq_pow)

    for occurs in sorted(occur_lens.keys()):
        ret = []
        for cyc_len in occur_lens[occurs]:
            if (1 < cyc_len < phi) and gcd(cyc_len, phi) == 1:
                ret.append(cyc_len)

        if ret:
            return ret
