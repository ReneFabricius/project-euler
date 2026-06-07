from euclidean_alg import ext_euclid
from collections import Counter
from primes import prime_fact_decomp
from math import prod


def pr176_naive(count, cathe_lim=10000):
    vis_caths: set[tuple[int, int]] = set()
    cathetus_counter = Counter()
    n = -1
    while True:
        n += 2
        n2 = n * n
        m = n
        exhausted = True
        while True:
            m += 2
            gcd, _, _ = ext_euclid(m, n)
            if gcd > 1:
                continue

            a = m * n
            b = (m * m - n2) // 2
            a, b = (a, b) if a < b else (b, a)
            if a > cathe_lim:
                break

            exhausted = False

            if (a, b) in vis_caths:
                continue

            vis_caths.add((a, b))

            for k in range(1, cathe_lim // a + 1):
                cathetus_counter[k * a] += 1
                cathetus_counter[k * b] += 1

        if exhausted:
            break

    cand = 0
    found_cand = None
    while True:
        cand += 1
        if cand > cathe_lim:
            raise ValueError("Insufficient cathetus limit")

        if cathetus_counter[cand] == count:
            found_cand = cand
            break

    return {
        k: cathetus_counter[k] for k in cathetus_counter if k <= cathe_lim
    }, found_cand


def decomp_formula(cathe):
    """
    Formula for computing number of pythagorean triplets that contain cathe as one of their cathete.
    Derived from Euclids formula variant form for cathetus: a = 2*e*m*n (wiki).
    Counting the partitionings of cathetus length into a multiplier k and remainder a from above
    leads to elementary symmetric polynomials and using their generating function we arrive at the
    formula.

    Problem result derived by hand from the formula.
    """
    dec = prime_fact_decomp(cathe)
    xs = (exp if pri != 2 else exp - 1 for pri, exp in dec.items())
    trips = (prod([1 + 2 * x for x in xs]) - 1) // 2
    return trips


def check_formula(lim):
    counts, k = pr176_naive(1, lim)
    for cathe, count in counts.items():
        form_count = decomp_formula(cathe)
        if count != form_count:
            print(
                f"Error for cathetus: {cathe}, count: {count}, form count: {form_count}"
            )
