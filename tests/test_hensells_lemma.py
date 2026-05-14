from hensells_lemma import hensells_lemma
import pytest


@pytest.mark.parametrize(
    "poly, poly_der, prime, root, power, exp_roots",
    [
        (lambda x: x**2 - 1, lambda x: 2 * x, 2, 1, 1, True),
        (lambda x: x**2 - 1, lambda x: 2 * x, 5, 4, 1, True),
        (lambda x: x**2 - 1, lambda x: 2 * x, 5, 24, 2, True),
        (lambda x: x**2, lambda x: 2 * x, 5, 25, 2, True),
        (lambda x: x**3 + 2 * x**2 - 17, lambda x: 3 * x**2 + 4 * x, 13, 10, 1, True),
    ],
)
def test_hensells_lemma(poly, poly_der, prime, root, power, exp_roots: bool):
    lifted_roots = hensells_lemma(
        poly=poly, poly_der=poly_der, root=root, power=power, prime=prime
    )
    if not exp_roots:
        assert len(lifted_roots) == 0
    else:
        assert lifted_roots
        for lifted_root in lifted_roots:
            assert poly(lifted_root) % prime ** (power + 1) == 0
