from primes import primes
from quadratic_residues import tonelli_shanks
from hensells_lemma import hensells_lemma
from euclidean_alg import ext_euclid


def examine_formula(lim):
    P = primes(lim)
    for p in P:
        p2 = p**2
        QRs = set()
        for i in range(1, p2):
            qr = i**2 % p2
            QRs.add(qr)

        for i in range(1, p2):
            crit = (i ** int((p * (p - 1)) / 2)) % p2
            if crit == 1:
                if i not in QRs:
                    print(f"Conflict: p: {p}, number: {i}, crit: {crit} not a QR!")
            elif crit == -1:
                if i in QRs:
                    print(f"Conflict: p: {p}, number: {i}, crit: {crit} is a QR!")

        for qr in QRs:
            crit = (qr ** int((p * (p - 1)) / 2)) % p2
            if crit != 1:
                print(f"Conflict: p: {p}, qr: {qr}, crit: {crit}!")


def pr457(lim=10**7):
    P = primes(lim)
    ret = 0
    i = 1
    for p in P[1:]:  # no solution for 2
        i += 1
        if i % 10000 == 0:
            print(f"{i}/{len(P)}")
        p2 = p**2
        if pow(13, int((p - 1) / 2), p) == 1:
            sr = tonelli_shanks(p, 13) % p
            sqrsp2 = []
            for sqr in (sr, -sr % p):
                sqrsp2.extend(
                    rai % p2
                    for rai in hensells_lemma(
                        poly=lambda x: x**2 - 13,
                        poly_der=lambda x: 2 * x,
                        root=sqr,
                        power=1,
                        prime=p,
                    )
                )

            ns = []
            sqrsp2_set = set(sqrsp2)
            for sqp2 in sqrsp2:
                sqrsp2_set.add(-sqp2 % p2)
            for sqp2 in sqrsp2_set:
                _, m, _ = ext_euclid(2, p2)
                n = m * (sqp2 + 3) % p2
                if n < 0 or (n**2 - 3 * n - 1) % p2 != 0:
                    raise ValueError(f"Incorrect n: {n} found for p: {p}")
                ns.append(n)

            ret += min(ns)

    return ret


def pr457_naive(lim=10**3):
    P = primes(lim)
    ret_l = []
    for p in P:
        p2 = p**2
        for n in range(p2):
            if (n**2 - 3 * n - 1) % p2 == 0:
                ret_l.append((p, n))
                break

    return ret_l
