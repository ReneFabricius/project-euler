import primes
import math


def pr196(S):
    r_start = S * (S - 1) // 2 + 1
    r_end = r_start + S - 1
    prim = primes.primesRang(r_start, r_end)

    tripl_mem = []
    for pr in prim:
        if is_tripl_mem(pr):
            tripl_mem.append(pr)

    return tripl_mem


def has_p_neighbor(num, exc):
    row = int((1 + math.sqrt(1 + 8*(num - 1))) / 2)
    r_start = row * (row - 1) // 2 + 1
    r_end = r_start + row - 1
    above = num - row + 1
    below = num + row

    if num == r_start:
        neighbs = [above, above + 1, num + 1, below, below + 1]
    elif num == r_end:
        neighbs = [above - 1, num - 1, below - 1, below, below + 1]
    else:
        neighbs = [above - 1, above, above + 1, num - 1, num + 1, below - 1, below, below + 1]

    p_neighbs = []
    for n in neighbs:
        if n == exc:
            continue

        if primes.isPrimeMillerRabin(n, 15):
            p_neighbs.append(n)

    return p_neighbs


def is_tripl_mem(p):
    p_neigh = has_p_neighbor(p, None)
    if len(p_neigh) == 0:
        return False

    if len(p_neigh) > 1:
        return True

    for pn in p_neigh:
        if len(has_p_neighbor(pn, p)) > 0:
            return True

    return False