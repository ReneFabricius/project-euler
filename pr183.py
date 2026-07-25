from math import e, floor


def pr183(end, start=5):
    res = 0
    for n in range(start, end + 1):
        infl = n / e
        c1 = floor(infl)

        k = c1 if ((c1 + 1) ** (c1 + 1)) / (c1**c1 * n) > 1 else c1 + 1
        while k % 2 == 0:
            k //= 2
        while k % 5 == 0:
            k //= 5

        if n % k == 0:
            res -= n
        else:
            res += n

    return res
