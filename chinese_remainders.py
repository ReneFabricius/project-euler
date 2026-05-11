from euclidean_alg import ext_euclid


def solve_congruence_system(rems: list[int], mods: list[int]) -> tuple[int, int]:
    """
    Solves linear system of pairwise coprime moduli.

    Args:
        rems (list[int]): remainders, 0 <= rems[i] < mods[i] is assumed
        mods (list[int]): moduli, assumed pairwise coprime

    Returns:
        tuple[int, int]: solution and product of moduli
    """
    congs = [(rems[i], mods[i]) for i in range(len(rems))]
    while len(congs) > 1:
        if len(congs) > 2:
            congs = sorted(congs, key=lambda cong: cong[1])
        new_congs = []
        i, j = 0, len(congs) - 1
        while i < j:
            e_gcd, m, n = ext_euclid(congs[i][1], congs[j][1])
            if e_gcd != 1:
                raise ValueError("Non-coprime moduli: %s, %s", congs[i][1], congs[j][1])
            new_mod = congs[i][1] * congs[j][1]
            new_rem = (
                congs[j][0] * m * congs[i][1] + congs[i][0] * n * congs[j][1]
            ) % new_mod
            new_congs.append((new_rem, new_mod))

            i += 1
            j -= 1

        if i == j:
            new_congs.append(congs[i])

        congs = new_congs

    return congs[0]
