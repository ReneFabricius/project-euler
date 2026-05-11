from primes import prime_fact_decomp


def largestPFact(n):
    D = prime_fact_decomp(n)

    return D[-1]
