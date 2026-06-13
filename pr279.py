from math import gcd


def pr_279(lim=10**8):
    # there are only three options for a rational cosinus of a rational angle (in degrees)
    # 60, 90, 120
    counted_prims = set()
    count = 0
    for m in range(2, lim + 1):
        if m % 100 == 0:
            print(f"processing m: {m}")
        over_60 = False
        over_90 = False
        over_120 = False
        m_half = m / 2
        broke_at_first = False
        for n in range(1, m):
            if gcd(m, n) > 1:
                continue

            if m % 2 == 1 and n % 2 == 1 and not over_90:
                a_90 = m * n
                b_90 = (m * m - n * n) // 2
                c_90 = (m * m + n * n) // 2
                triang_90 = tuple(sorted([a_90, b_90, c_90]))
                peri_90 = sum(triang_90)
                if peri_90 > lim:
                    over_90 = True
                else:
                    if triang_90 not in counted_prims:
                        counted_prims.add(triang_90)
                        count += int(lim / peri_90)

            if n <= m_half and not over_60:
                a_60 = m * m + n * n - m * n
                b_60 = 2 * m * n - n * n
                c_60 = m * m - n * n
                if a_60 % 3 == 0 and b_60 % 3 == 0 and c_60 % 3 == 0:
                    a_60, b_60, c_60 = a_60 // 3, b_60 // 3, c_60 // 3
                triang_60 = tuple(sorted([a_60, b_60, c_60]))
                peri_60 = sum(triang_60)
                if peri_60 > 3 * lim:
                    over_60 = True
                elif peri_60 <= lim:
                    if triang_60 not in counted_prims:
                        counted_prims.add(triang_60)
                        count += int(lim / peri_60)

            if m % 3 != n % 3 and not over_120:
                a_120 = m * m + n * n + m * n
                b_120 = 2 * m * n + n * n
                c_120 = m * m - n * n
                triang_120 = tuple(sorted([a_120, b_120, c_120]))
                peri_120 = sum(triang_120)
                if peri_120 > lim:
                    over_120 = True
                else:
                    if triang_120 not in counted_prims:
                        counted_prims.add(triang_120)
                        count += int(lim / peri_120)

            if (over_60 or n > m_half) and over_90 and over_120:
                if n == 1:
                    broke_at_first = True
                print(f"m: {m}, breaking at n: {n}")
                break

        if broke_at_first:
            break

    return count, counted_prims
