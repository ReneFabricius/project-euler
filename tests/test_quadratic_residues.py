import pytest
from quadratic_residues import tonelli_shanks
from primes import primes


def test_tonelli_shanks(lim=5000):
    P = primes(lim)

    for p in P[:20] + P[-2:]:
        QRs = set()
        for i in range(1, p):
            QRs.add(i**2 % p)

        for i in range(1, p):
            if i in QRs:
                r = tonelli_shanks(p=p, n=i)
                assert r**2 % p == i
            else:
                with pytest.raises(ValueError):
                    _ = tonelli_shanks(p=p, n=i)
