def explore_slow(n, l):
    a = 2
    b = 2 * n + 1
    seq = [a, b]
    cmb = [(i, []) for i in range(l)]
    cmb[a + b][1].append((a, b))
    for cand in range(b + 1, l):
        if len(cmb[cand][1]) == 1:
            seq.append(cand)
            for prev in seq[:-1]:
                sm = prev + cand
                if sm < l:
                    cmb[sm][1].append((prev, cand))

    return seq, cmb


def explore(n, l):
    a = 2
    b = 2 * n + 1
    seq = [a, b]
    seq_s = set(seq)
    gen = 2 * b + a
    cycles = []
    for cand in range(a + b, l, a):
        if cand - 1 == gen:
            seq.append(gen)
            seq_s.add(gen)

        if ((cand - a) in seq_s) ^ ((cand - gen) in seq_s):
            seq.append(cand)
            seq_s.add(cand)

        if (cand + a - b) % gen == 0:
            cur_cyc = [
                cyc_cand in seq_s
                for cyc_cand in range(
                    len(cycles) * gen + b, (len(cycles) + 1) * gen + b, 2
                )
            ]

            if cycles and cycles[0] == cur_cyc:
                print(f"Found cycle period {len(cycles)}")
                return seq, cycles

            cycles.append(cur_cyc)


def compute_member(n, k, cycles):
    if k == 1:
        return 2
    b = 2 * n + 1
    gen = 2 * len(cycles[0])
    a = 2
    seq_start = [a, b]
    mem = b
    while True:
        mem += a
        if mem >= gen + b:
            break
        if gen == mem - 1:
            seq_start.append(gen)
        seq_start.append(mem)

    if k - 1 < len(seq_start):
        return seq_start[k - 1]

    period = len(cycles)
    per_membs = sum([sum(ccl) for ccl in cycles])
    zsk = k - 3
    per_n = zsk // per_membs
    per_pos = zsk % per_membs
    per_start = b + gen * period * per_n
    count_mem = 0
    count_pos = 0
    for cycle in cycles:
        for mem in cycle:
            if mem:
                if count_mem == per_pos:
                    return per_start + count_pos
                count_mem += 1
            count_pos += 2

    raise ValueError(f"Didn't find member! n: {n}, k: {k}")


def check_computation():
    L = 10**9
    L_slow = 1000
    for n in range(2, 11):
        print(f"Checking for n: {n}")
        seq, cyc = explore(n=n, l=L)
        seq_s, cmb_s = explore_slow(n=n, l=L_slow)
        for k, mmb in enumerate(seq_s):
            if k < len(seq) and seq_s[k] != seq[k]:
                print(f"Error, seq is not equal seq_s for n: {n}, k: {k}")

            comp_mmb = compute_member(n=n, k=k + 1, cycles=cyc)
            if mmb != comp_mmb:
                print(
                    f"Error for n: {n} at k: {k + 1}. Real memb: {mmb}, computed: {comp_mmb}"
                )

        for km in range(len(seq) - 1, len(seq) - 3, -1):
            comp_mmb = compute_member(n=n, k=km + 1, cycles=cyc)
            if seq[km] != comp_mmb:
                print(
                    f"Error for n: {n} at k: {km + 1}. Real memb: {seq[km]}, computed: {comp_mmb}"
                )


def solve_pr167():
    L = 10**9
    ret = 0
    k = 10**11
    for n in range(2, 11):
        print(f"Checking for n: {n}")
        seq, cyc = explore(n=n, l=L)
        mem = compute_member(n=n, k=k, cycles=cyc)
        print(f"Found member {mem}")
        ret += mem

    return ret
