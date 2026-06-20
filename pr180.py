from itertools import combinations_with_replacement
from fractions import Fraction
from line_profiler import profile
from math import comb as combi_coef


@profile
def pr180(ord=35):
    possible_fracs = set()
    for d in range(2, ord + 1):
        for n in range(1, d):
            possible_fracs.add(Fraction(n, d))

    trpl_sums = set()
    combs_to_test = combi_coef(len(possible_fracs) - 1 + 3, 3)

    combs_tested = 0
    triples_found = 0
    for comb in combinations_with_replacement(possible_fracs, r=3):
        combs_tested += 1
        if combs_tested % 100000 == 0:
            print(f"Tested: {combs_tested}/{combs_to_test}")

        for neg in range(3):
            neg_fr = comb[neg]
            pos_frs = comb[:neg] + comb[neg + 1 :]

            def is_zero(n_val):
                if n_val > 0:
                    return (
                        (
                            pos_frs[0].numerator
                            * pos_frs[1].denominator
                            * neg_fr.denominator
                        )
                        ** n_val
                        + (
                            pos_frs[1].numerator
                            * pos_frs[0].denominator
                            * neg_fr.denominator
                        )
                        ** n_val
                        - (
                            neg_fr.numerator
                            * pos_frs[0].denominator
                            * pos_frs[1].denominator
                        )
                        ** n_val
                    ) == 0

                return (
                    (pos_frs[0].denominator * pos_frs[1].numerator * neg_fr.numerator)
                    ** (-n_val)
                    + (pos_frs[1].denominator * pos_frs[0].numerator * neg_fr.numerator)
                    ** (-n_val)
                    - (neg_fr.denominator * pos_frs[0].numerator * pos_frs[1].numerator)
                    ** (-n_val)
                ) == 0

            found = False
            for n_val in (1, 2, -1, -2):
                if is_zero(n_val):
                    trpl_sums.add(sum(comb))
                    # print(f"Found triple: {comb}, n: {n_val}")
                    triples_found += 1
                    found = True
                    break

            if found:
                break

    print(f"Found {len(trpl_sums)} unique sums from {triples_found} triples.")
    sums_sum = sum(trpl_sums)
    return sums_sum.numerator + sums_sum.denominator, trpl_sums


if __name__ == "__main__":
    pr180(10)
