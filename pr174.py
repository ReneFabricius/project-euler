import math


def pr174(l, s, e):
    L = [0] * (l + 1)
    for a in range(1, int((l - 4)/4) + 1):
        for k in range(1, int((-a + math.sqrt(a**2 + l))/2) + 1):
            t = 4*k*(a + k)
            L[t] += 1

    D = {i : 0 for i in range(s, e)}
    for j in range(l + 1):
        if L[j] in D:
            D[L[j]] += 1

    return D
