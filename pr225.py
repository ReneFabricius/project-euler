def pr225(k):
    NDs = [False for i in range(10**6)]
    cur_k = 0
    cand = 1
    while True:
        cand += 2
        if NDs[cand]:
            cur_k += 1
            if cur_k == k:
                return cand
            continue

        pres_trp: set[tuple[int, int, int]] = set([(1, 1, 1)])
        cur_trp: tuple[int, int, int] = (1, 1, 1)
        while True:
            nxt = sum(cur_trp) % cand
            if nxt == 0:
                break
            else:
                n_trp = (*cur_trp[1:], nxt)
                if n_trp in pres_trp:
                    print(
                        f"Found cycle len: {len(pres_trp)} starting with: {n_trp} for cand: {cand}"
                    )
                    cur_k += 1
                    if cur_k == k:
                        return cand
                    for cand_mult in range(
                        cand, len(NDs), 2 * cand
                    ):  # only interested in odd numbers
                        NDs[cand_mult] = True
                    break
                else:
                    pres_trp.add(n_trp)
                    cur_trp = n_trp
