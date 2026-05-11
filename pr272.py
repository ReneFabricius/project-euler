from primes import primes, prime_fact_decomp
from math import prod, log
from utils import SubsetIterator, BoundedCustomSmoothIterator
import bisect


def pr272(limit=10**11, c_value=242):
    num_3 = round(log(c_value + 1, 3))
    if 3**num_3 != c_value + 1:
        raise ValueError(f"Invalid c-value {c_value} - must be a power of 3 - 1")
    P1000 = primes(1000)
    P1000_gen = [p for p in P1000 if (p - 1) % 3 == 0]
    min_base = prod(P1000_gen[: (num_3 - 2)]) * 9  # 3 ** 2 (and higher) are generating
    max_prime = limit // min_base
    P = [2] + primes(max_prime)[2:]  # skip 3
    P_gen = [p for p in P if (p - 1) % 3 == 0]
    bisect.insort(P_gen, 9)
    P_nogen = [p for p in P if (p - 1) % 3 != 0]

    res = 0
    counter = 0
    for gen in SubsetIterator(candidates=P_gen, limit=limit, set_size=num_3):
        counter += 1
        gen_val = prod(gen)
        rem = limit // gen_val
        if counter % 100000 == 0:
            print(f"Processing {counter}-th gen with rem: {rem}")
        if rem < 2:
            res += gen_val
            continue

        nogen_bis = bisect.bisect_right(P_nogen, rem)
        avail_nogen = P_nogen[:nogen_bis]
        gen_has_3 = False
        for p in gen:
            if p == 9 and 3 <= rem:
                bisect.insort(avail_nogen, 3)
                gen_has_3 = True
                continue
            if p <= rem:
                bisect.insort(avail_nogen, p)

        extensions = [
            ext for ext in BoundedCustomSmoothIterator(primes=avail_nogen, limit=rem)
        ]
        if not gen_has_3:
            extra_exts = []
            for ext in extensions:
                if ext * 3 <= rem:
                    extra_exts.append(ext * 3)
                else:
                    break

            extensions.extend(extra_exts)

        res += sum(extensions) * gen_val

    return res


def pr272_naive(limit=10**5, c_value=8):
    num_3 = int(log(c_value + 1, 3))
    if 3**num_3 != c_value + 1:
        raise ValueError("Invalid c-value - must be a power of 3 - 1")
    res = []
    for x in range(3, limit + 1):
        dec = prime_fact_decomp(x)
        gen_count = 0
        for p in dec:
            if (p - 1) % 3 == 0:
                gen_count += 1

        if gen_count == num_3:
            res.append(x)

    return res


def study_p(p, pow):
    for i in range(1, pow):
        n = p**i
        sols = []
        for x in range(1, n):
            if x**3 % n == 1:
                sols.append(x)

        print(f"Power {i}, solutions: {sols}")
