from math import sin, cos, atan2, radians, degrees


def pr177():
    EPS = 10 ** (-9)
    found = set()
    for a in range(2, 180):
        print(f"Processing a: {a}")
        for b in range(2, min(180, 360 - a - 4 + 1)):
            for c in range(2, min(180, 360 - a - b - 2 + 1)):
                d = 360 - a - b - c
                for b_1 in range(max(180 - a - d + 1, 1), min(180 - a - 1 + 1, b)):
                    a_r, b_r, c_r, d_r, b_1_r = (radians(x) for x in (a, b, c, d, b_1))
                    nom = sin(b_r - b_1_r) * sin(d_r) * sin(a_r)
                    denom = sin(c_r + b_r - b_1_r) * sin(b_r) + sin(b_r - b_1_r) * sin(
                        d_r
                    ) * cos(a_r)
                    a_1_r = atan2(nom, denom)
                    a_1 = degrees(a_1_r)
                    if abs(a_1 - round(a_1)) > EPS:
                        continue

                    a_1 = round(a_1)
                    if a_1 < 1 or a_1 > a - 1:
                        continue

                    a_2 = a - a_1
                    b_2 = b - b_1
                    c_1 = 180 - b - a_2
                    if c_1 < 1 or c_1 > c - 1:
                        continue

                    c_2 = c - c_1
                    d_1 = 180 - c - b_2
                    d_2 = d - d_1
                    found_ql = (a_1, a_2, b_1, b_2, c_1, c_2, d_1, d_2)
                    found.add(found_ql)
                    # print(f"Found: {found_ql}")

    unique = set()
    for qd in found:
        rotations = {(*qd[d:], *qd[:d]) for d in range(0, 8, 2)}
        mirrored = {qd[::-1] for qd in rotations}
        similar = rotations | mirrored
        if not unique & similar:
            unique.add(qd)

    return unique
