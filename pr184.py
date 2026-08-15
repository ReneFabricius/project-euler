from math import atan2, pi, sqrt, ceil, floor
from bisect import bisect


def circle_points(r: int) -> list[tuple[int, int]]:
    valid = []
    r2 = r * r
    for x in range(-r + 1, r):
        x2 = x * x
        for y in range(-r + 1, r):
            if x2 + y * y < r2:
                valid.append((x, y))

    return valid


def ring_points(r: int) -> list[tuple[int, int, float]]:
    points = []
    rp2 = (r - 1) ** 2
    r2 = r * r
    for x in range(1, r):
        x2 = x * x
        for y in range(ceil(sqrt(rp2 - x2)), ceil(sqrt(r2 - x2))):
            cx, cy = x, y
            for _ in range(4):
                points.append((cx, cy, atan2(cy, cx) % (2 * pi)))
                cx, cy = -cy, cx

    points = sorted(points, key=lambda pt: pt[2])

    return points


def center_inside(
    x: tuple[int, int, int], y: tuple[int, int, int], z: tuple[int, int, int]
) -> bool:
    def center_dir(a: tuple[int, int], b: tuple[int, int]) -> int:
        return a[0] * b[1] - a[1] * b[0]

    [x, y, z] = sorted([x, y, z], key=lambda pt: pt[2])

    for a, b in [
        ((y[0] - x[0], y[1] - x[1]), (-x[0], -x[1])),
        ((z[0] - y[0], z[1] - y[1]), (-y[0], -y[1])),
        ((x[0] - z[0], x[1] - z[1]), (-z[0], -z[1])),
    ]:
        if center_dir(a, b) <= 0:
            return False

    return True


def pr184_naive(r):
    triangs = 0
    circle_points = []
    for ring in range(2, r + 1):
        print(f"Ring: {ring}")
        ring_pts = ring_points(ring)

        three_on_ring = []
        for f_i, f in enumerate(ring_pts):
            for s_i, s in enumerate(ring_pts[f_i + 1 :], f_i + 1):
                for t in ring_pts[s_i + 1 :]:
                    if center_inside(f, s, t):
                        three_on_ring.append((f[:2], s[:2], t[:2]))

        print(f"Three: {len(three_on_ring)}")
        triangs += len(three_on_ring)

        two_on_ring = []
        for f_i, f in enumerate(ring_pts):
            for s in ring_pts[f_i + 1 :]:
                for t in circle_points:
                    if center_inside(f, s, t):
                        two_on_ring.append((f[:2], s[:2], t[:2]))

        print(f"Two: {len(two_on_ring)}")
        triangs += len(two_on_ring)

        one_on_ring = []
        one_on_ring_fq = []
        for f_i, f in enumerate(ring_pts):
            for s_i, s in enumerate(circle_points):
                for t in circle_points[s_i + 1 :]:
                    if center_inside(f, s, t):
                        one_on_ring.append((f[:2], s[:2], t[:2]))
                        if f[0] > 0 and f[1] >= 0 and s[2] < f[2] + pi:
                            one_on_ring_fq.append((f[:2], s[:2], t[:2]))

        print(f"One: {len(one_on_ring)}")
        triangs += len(one_on_ring)

        circle_points.extend(ring_pts)
        circle_points = sorted(circle_points, key=lambda pt: pt[2])

    return triangs


def pr184(r):
    triangs = 0
    circle_points = []
    for ring in range(2, r + 1):
        print(f"Ring: {ring}")
        rp2 = (ring - 1) ** 2
        ring_pts = ring_points(ring)
        # three on ring
        q = len(ring_pts) // 4
        three_on_ring = 4 * q * (q - 1) * (2 * q - 1) // 3
        print(f"Three: {three_on_ring}")
        triangs += three_on_ring

        # two on ring
        two_on_ring = 0
        for f_i, first in enumerate(ring_pts):
            if first[0] == 0:
                break
            for second in ring_pts[f_i + 1 :]:
                if second[0] == -first[0] and second[1] == -first[1]:
                    break

                if second[0] > 0:
                    x_end = -1
                elif second[1] > 0:
                    x_end = -second[0] - 1
                else:
                    x_end = ring - 2

                for x in range(-first[0] + 1, x_end + 1):
                    cands = [floor(-sqrt(rp2 - x * x)) + 1]
                    if second[0] > 0:
                        cands.append(floor(x * (second[1] / second[0])) + 1)
                    y_start = max(cands)

                    if x <= 0:
                        y_end = ceil(x * first[1] / first[0]) - 1
                    else:
                        y_end = ceil(x * second[1] / second[0]) - 1

                    two_on_ring += y_end - y_start + 1

        print(f"Two: {4 * two_on_ring}")
        triangs += 4 * two_on_ring

        # one on ring
        # one_on_ring_fq = []
        one_on_ring = 0
        for first in ring_pts:
            if first[0] == 0:
                break
            s_i = bisect(circle_points, first[2], key=lambda pt: pt[2])
            for second in circle_points[s_i:]:
                if second[2] >= first[2] + pi:
                    break

                if second[0] > 0:
                    x_end = -1
                elif second[1] > 0:
                    x_end = (
                        ceil(
                            sqrt(
                                rp2 * second[0] ** 2 / (second[0] ** 2 + second[1] ** 2)
                            )
                        )
                        - 1
                    )
                else:
                    x_end = ring - 2

                for x in range(-first[0] + 1, x_end + 1):
                    cands = [floor(-sqrt(rp2 - x * x)) + 1]
                    if second[0] > 0:
                        cands.append(floor(x * (second[1] / second[0])) + 1)
                    y_start = max(cands)

                    if x <= 0:
                        y_end = ceil(x * first[1] / first[0]) - 1
                    else:
                        y_end = ceil(x * second[1] / second[0]) - 1

                    # for y in range(y_start, y_end + 1):
                    #    one_on_ring_fq.append((first[:2], second[:2], (x, y)))

                    one_on_ring += y_end - y_start + 1

        print(f"One: {4 * one_on_ring}")
        triangs += 4 * one_on_ring

        circle_points.extend(ring_pts)
        circle_points = sorted(circle_points, key=lambda pt: pt[2])

    return triangs


if __name__ == "__main__":
    pr184_naive(2)
    pr184(3)
