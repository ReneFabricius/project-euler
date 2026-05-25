from primes import (
    prime_fact_decomp,
    prime_fact_decomp_preinitialized,
    primes,
)
from quadratic_residues import tonelli_shanks


def study_divs(k_lim=200, n_lim=10000):
    rets = []
    for k in range(1, k_lim + 1):
        sp = k**2 + 1
        dp = prime_fact_decomp(sp)
        klp = 1
        for n in range(2, n_lim + 1):
            sc = n**2 + k**2
            dc = prime_fact_decomp(sc)
            lp = max((set(dp.keys()) & set(dc.keys())) | {1})
            sp = sc
            dp = dc
            if lp > klp:
                klp = lp
                print(
                    f"k: {k:<5}, n: {n - 1:>6}, lp: {lp:>6}, 2n + 1: {2 * (n - 1) + 1:>6}"
                )
        rets.append(klp)

    return rets


def pr659(k_lim):
    ret = 0
    Ps = primes(2 * k_lim + 10)
    for k in range(1, k_lim + 1):
        if (
            (k < 10000 and k % 1000 == 0)
            or (k < 100000 and k % 10000 == 0)
            or (k % 100000 == 0)
        ):
            print(f"k: {k}")

        dec = prime_fact_decomp_preinitialized(n=4 * k**2 + 1, P=Ps)
        p = max(dec.keys())
        # print(f"n: {4 * k ** 2 + 1}, max p: {p}")
        ret += p

    return ret


def pr659_resid(k_lim):
    ret = 0
    Ps = primes(2 * k_lim + 10)
    k_vals = [4 * k * k + 1 for k in range(1, k_lim + 1)]
    facs = [set() for k in range(1, k_lim + 1)]
    for p in Ps:
        if p % 4 != 1:
            continue

        r = tonelli_shanks(p, p - 1)
        inv2 = (p + 1) // 2
        k1, k2 = (-r * inv2) % p, (r * inv2) % p
        for k_sol in (k1, k2):
            for k_seq in range(k_sol, k_lim + 1, p):
                while k_vals[k_seq - 1] % p == 0:
                    k_vals[k_seq - 1] //= p
                    facs[k_seq - 1].add(p)

    for k, k_val in enumerate(k_vals):
        if k_val != 1:
            facs[k].add(k_val)

        # print(f"n:{4 * (k + 1) ** 2 + 1}, max p: {max(facs[k])}")
        ret += max(facs[k])

    return ret
