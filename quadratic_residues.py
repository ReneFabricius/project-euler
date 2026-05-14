from random import random


def tonelli_shanks(p: int, n: int):
    """
    Tonelli-Shanks algorithm.
    For p a prime > 2 and n a quadratic residue mod p, finds x such that
    x^2 = n mod p

    Args:
        p (int): prime
        n (int): quadratic residue
    """
    if p == 2:
        return 1

    if p % 4 == 3:
        x = pow(n, int((p + 1) / 4), p)
        if x**2 % p == n:
            return x

    Q = p - 1
    S = 0
    while Q % 2 == 0:
        Q = Q // 2
        S += 1

    z = None
    while z is None:
        z_cand = int(p * random())
        if pow(z_cand, int((p - 1) / 2), p) == p - 1:
            z = z_cand
            break

    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, int((Q + 1) / 2), p)

    while True:
        if t == 0:
            return 0

        if t == 1:
            return R

        i = 0
        tsq = t
        while tsq % p != 1:
            i += 1
            tsq = tsq**2 % p

        if i == M:
            raise ValueError(f"{n} is not a quadratic residue")

        b = pow(c, 2 ** (M - i - 1), p)
        M = i
        c = b**2 % p
        t = t * c % p
        R = R * b % p
