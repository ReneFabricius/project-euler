from math import factorial, prod
from primes import prime_fact_decomp, findDivisors, isPrimeMillerRabin
from collections import Counter
from copy import copy


def _small_decomp(n) -> Counter:
    P = [2, 3, 5, 7, 11, 13]
    c: Counter[int] = Counter()
    for p in P:
        while n % p == 0:
            c[p] += 1
            n //= p
            if n == 1:
                return c

    return c


def finish_from_decomp(rem_decomp: Counter[int]) -> tuple[int | None, set[int] | None]:
    dec_c = copy(rem_decomp)
    num = 1
    power_primes = set()
    while dec_c:
        mp = max(dec_c.keys())
        mp_pow = dec_c.pop(mp)
        power_primes.add(mp)
        if mp - 1 > 1:
            dec_mp = _small_decomp(mp - 1)
            for mp_p, mp_p_pow in dec_mp.items():
                dec_c[mp_p] -= mp_p_pow
                if dec_c[mp_p] < 0:
                    return None, None
                if dec_c[mp_p] == 0:
                    dec_c.pop(mp_p)
        num *= mp ** (mp_pow + 1)

    return num, power_primes


def pr248():
    MR_CONST = 40
    fct = factorial(13)
    fct_decomp = prime_fact_decomp(fct)
    fct_divs = findDivisors(fct)
    fct_pm1_divs = [div for div in fct_divs if isPrimeMillerRabin(div + 1, MR_CONST)]

    numbers = set()
    div_ss: set[tuple[int, ...]] = set()

    def find_div_sss(rem_divs: set[int], rem_tot: int, cur_divs: set[int]):
        for div in rem_divs:
            if rem_tot % div != 0:
                continue

            new_divs = cur_divs | {div}
            new_divs_tpl = tuple(sorted(new_divs))
            if new_divs_tpl in div_ss:
                continue

            div_ss.add(new_divs_tpl)

            find_div_sss(
                rem_divs=rem_divs - {div}, rem_tot=rem_tot // div, cur_divs=new_divs
            )

    find_div_sss(rem_divs=set(fct_pm1_divs), rem_tot=fct, cur_divs=set())

    print(f"Found {len(div_ss)} divisor subsets")

    for dss in div_ss:
        divs_dec = Counter()
        for div in dss:
            divs_dec.update(_small_decomp(div))

        rem_dec = fct_decomp - divs_dec

        num, pow_primes = finish_from_decomp(rem_dec)

        if num is None or pow_primes is None:
            continue

        invalid = False
        for div in dss:
            if (div + 1) in pow_primes:
                invalid = True
                break

        if invalid:
            continue

        numbers.add(prod([div + 1 for div in dss]) * num)
        if len(numbers) % 10000 == 0:
            print(f"found {len(numbers)} numbers")

    return sorted(numbers)
