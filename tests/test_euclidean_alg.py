from euclidean_alg import ext_euclid
import pytest
from math import gcd


@pytest.mark.parametrize(
    "a, b",
    [
        (5, 7),
        (-11, 3),
        (200, 1),
        (200, 300),
        (12548756985021450440564054664, 524684366468643856860234334646),
    ],
)
def test_ext_euclid(a, b):
    e_gcd, m, n = ext_euclid(a, b)
    assert m * a + n * b == e_gcd
    assert abs(e_gcd) == gcd(a, b)
