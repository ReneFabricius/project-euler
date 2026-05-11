from chinese_remainders import solve_congruence_system
import pytest
from contextlib import nullcontext


@pytest.mark.parametrize(
    "rems, mods, expectation",
    [
        ([1, 2, 4, 6, 10], [2, 3, 5, 7, 11], nullcontext()),
        ([1, 3], [5, 10], pytest.raises(ValueError)),
        ([11, 70, 1023, 0], [15, 77, 1024, 19], nullcontext()),
    ],
)
def test_solve_congruence_system(rems, mods, expectation):
    with expectation:
        cong = solve_congruence_system(rems=rems, mods=mods)
        assert cong[0] < cong[1]
        for r, m in zip(rems, mods):
            assert cong[0] % m == r
