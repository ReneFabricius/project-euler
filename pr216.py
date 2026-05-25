from primes import primes
from quadratic_residues import tonelli_shanks
from math import sqrt


def pr216_resid(k_lim):
    ret = 0
    Ps = primes(int(sqrt(2) * k_lim) + 10)
    t_vals = [2 * k * k - 1 for k in range(2, k_lim + 1)]
    max_f = [1 for k in range(2, k_lim + 1)]
    for p in Ps[1:]:
        inv2 = (p + 1) // 2
        e_crit = pow(inv2, (p - 1) // 2, p)
        if e_crit != 1:
            continue

        r = tonelli_shanks(p=p, n=inv2)

        for k_sol in (-r % p, r):
            for k_seq in range(k_sol, k_lim + 1, p):
                while t_vals[k_seq - 2] % p == 0:
                    t_vals[k_seq - 2] //= p
                    if p > max_f[k_seq - 2]:
                        max_f[k_seq - 2] = p

    for k, t_val in enumerate(t_vals):
        if t_val != 1:
            if t_val > max_f[k]:
                max_f[k] = t_val

        if max_f[k] == 2 * (k + 2) ** 2 - 1:
            ret += 1

    return ret
