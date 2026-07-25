from primes import primes, totient_preinitialized, prime_fact_decomp_preinitialized
from math import sqrt


def find_examples(lim):
    P = primes(int(sqrt(lim)) + 10)
    found = []
    for n in range(2, lim + 1):
        tot = totient_preinitialized(n, P)
        if (n - 1) % (n - tot) == 0:
            dec = prime_fact_decomp_preinitialized(n, P)
            if len(dec) > 1:
                dec_m1 = prime_fact_decomp_preinitialized(n - 1, P)
                dec_tot = prime_fact_decomp_preinitialized(tot, P)
                dec_num = prime_fact_decomp_preinitialized(n - tot, P)
                dec_rest = dec_m1 - dec_num
                found.append((n, dec, dec_m1, dec_tot, dec_num, dec_rest))

    return found
