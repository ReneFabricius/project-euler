from primes import primes, rangePrimeFactDecomposition
from itertools import combinations
from math import prod, comb


def pr268(k_lim):
    P_LIM = 100
    NUM_FAC = 4
    P = primes(P_LIM)
    coefs = {NUM_FAC: 1}
    for k in range(NUM_FAC + 1, len(P) + 1):
        k_coef = 1
        for comb_l in range(NUM_FAC, k):
            k_coef -= coefs[comb_l] * comb(k, comb_l)
        coefs[k] = k_coef

    ret = 0
    for comb_len in range(NUM_FAC, len(P) + 1):
        for combi in combinations(P, comb_len):
            val = prod(combi)
            occurs = k_lim // val
            ret += coefs[comb_len] * occurs

    return ret


def pr268_descript(k_lim):
    P_LIM = 100
    NUM_FAC = 4
    P = primes(P_LIM)
    coefs = {NUM_FAC: 1}
    for k in range(NUM_FAC + 1, len(P) + 1):
        k_coef = 1
        for comb_l in range(NUM_FAC, k):
            k_coef -= coefs[comb_l] * comb(k, comb_l)
        coefs[k] = k_coef

    ret = 0
    counters = [0 for k in range(k_lim + 1)]
    histories = [[] for k in range(k_lim + 1)]
    for comb_len in range(NUM_FAC, len(P) + 1):
        for combi in combinations(P, comb_len):
            val = prod(combi)

            for val_m in range(val, k_lim + 1, val):
                counters[val_m] += coefs[comb_len]
                histories[val_m].append((coefs[comb_len], combi))

            occurs = k_lim // val
            ret += coefs[comb_len] * occurs

    decs = rangePrimeFactDecomposition(k_lim)
    for n in range(len(counters)):
        if counters[n] > 1 or counters[n] < 0:
            print(f"N: {n}, c: {counters[n]}, h: {histories[n]}, dec: {decs[n]}")

    return counters, histories, decs


def pr268_naive(k_lim):
    P_LIM = 100
    P = set(primes(P_LIM))
    decomps = rangePrimeFactDecomposition(k_lim + 1)
    ret = 0
    for decomp in decomps[2:]:
        dec_ps = set(decomp.keys())
        if len(P & dec_ps) >= 4:
            ret += 1

    return ret
