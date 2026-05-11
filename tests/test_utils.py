from utils import SubsetIterator, BoundedCustomSmoothIterator
import pytest
from itertools import combinations, product
from math import prod, log


@pytest.mark.parametrize(
    "candidates, set_size, limit",
    [
        ([2, 3, 5, 7, 11], 3, 200),
        (list(range(100)), 4, 10**5),
        ([1, 2, 3], 1, 3),
        (list(range(50)), 6, 10000),
    ],
)
def test_subset_iterator(candidates, set_size, limit):
    res = [
        comb
        for comb in SubsetIterator(
            candidates=candidates, set_size=set_size, limit=limit
        )
    ]
    exp_res = [
        list(comb) for comb in combinations(candidates, set_size) if prod(comb) <= limit
    ]
    assert res == exp_res


@pytest.mark.parametrize(
    "primes, limit", [([2, 3, 5], 1000), ([2], 1000000), ([7, 11, 13, 17, 19], 100000)]
)
def test_bounded_custom_smooth_iterator(primes, limit):
    res = [prd for prd in BoundedCustomSmoothIterator(primes=primes, limit=limit)]
    max_exp = int(log(limit, primes[0]))
    exp_cands = list(range(max_exp + 1))
    exp_res = sorted(
        list(
            set(
                [
                    prd
                    for prd in [
                        prod([primes[i] ** powers[i] for i in range(len(primes))])
                        for powers in product(exp_cands, repeat=len(primes))
                    ]
                    if prd <= limit
                ]
            )
        )
    )
    assert res == exp_res
