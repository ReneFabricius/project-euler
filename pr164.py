
def pr164(n):
    if n < 3:
        return 0
    en = 100
    lt1 = [0] * en
    lt2 = [0] * en

    for i in range(100, 1000):
        si = i
        ds = 0
        while si > 0:
            ds += si % 10
            si //= 10
        if ds < 10:
            lt = i % 100
            lt1[lt] += 1

    for d in range(n - 3):
        for i in range(len(lt1)):
            if lt1[i] > 0:
                cs = i % 10 + i // 10
                for ld in range(10):
                    if cs + ld < 10:
                        lt2[(i % 10) * 10 + ld] += lt1[i]

                lt1[i] = 0

        temp = lt1
        lt1 = lt2
        lt2 = temp

    return sum(lt1)