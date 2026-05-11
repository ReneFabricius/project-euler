from primes import prime_fact_decomp
from chinese_remainders import solve_congruence_system
from collections import defaultdict
from itertools import product


def pr271(n):
    decomp = prime_fact_decomp(n)
    if 0 in decomp:
        raise ValueError("too big")

    factors = [p ** decomp[p] for p in decomp]
    # naive factor roots finding, since factors should be small
    roots = defaultdict(list)
    for factor in factors:
        for i in range(1, factor):
            if (i**3 - 1) % factor == 0:
                roots[factor].append(i)

    roots_list = [roots[factor] for factor in factors]
    root_sum = 0
    for pr in product(*roots_list):
        cong = solve_congruence_system(rems=list(pr), mods=factors)
        if cong[0] > 1:
            root_sum += cong[0]

    return root_sum, roots_list
