from typing import Callable
from euclidean_alg import ext_euclid


def hensells_lemma(
    poly: Callable[[int], int],
    poly_der: Callable[[int], int],
    root: int,
    power: int,
    prime: int,
) -> list[int]:
    """
    Lift a polynomial poly root modulo prime ** power to a poly root modulo
    prime ** (power + 1).

    Args:
        poly (Callable[[int], int]): Function computing integer polynomial value.
        poly_der (Callable[[int], int]): Function computing integer polynomial
            derivation value.
        root (int): Root of poly mod prime ** power
        power (int): Prime power from which to lift
        prime (int): Prime

    Returns:
        list[int]: Zero or more lifted roots.
    """
    der_mod_p = poly_der(root) % prime
    if der_mod_p != 0:
        _, inv_der_mod_p, _ = ext_euclid(der_mod_p, prime)
        t = int(-inv_der_mod_p * poly(root) / prime**power)
        return [root + t * prime**power]
    else:
        if poly(root) % prime == 0:
            return [root + t * prime**power for t in range(0, prime**power)]
        else:
            return []
