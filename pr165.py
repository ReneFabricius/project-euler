

def true_intersect(A, B, C, D):
    den = (D[0] - C[0])*(B[1] - A[1]) - (D[1] - C[1])*(B[0] - A[0])
    if den == 0:
        return None

    inom = (D[0] - C[0])*(C[1] - A[1]) - (C[0] - A[0])*(D[1] - C[1])
    jnom = (C[1] - A[1])*(B[0] - A[0]) - (B[1] - A[1])*(C[0] - A[0])

    i = inom/den
    j = jnom/den

    if i <= 0 or i >= 1 or j <= 0 or j >= 1:
        return None

    if den < 0:
        den = -den
        inom = -inom
        jnom = -jnom

    Xn = C[0]*den + jnom*(D[0] - C[0])
    Yn = C[1]*den + jnom*(D[1] - C[1])

    gcdX = gcd(Xn, den)
    gcdY = gcd(Yn, den)

    return ((Xn/gcdX, den/gcdX), (Yn/gcdY, den/gcdY))


def BBS(S, M, m, l):
    for i in range(l):
        S = (S*S) % M
        yield S % m


def get_lines(n):
    L = [t for t in BBS(290797, 50515093, 500, n*4)]
    R = [((L[i], L[i+1]), (L[i+2], L[i+3])) for i in range(0, len(L), 4)]
    return R


def pr165(n):
    S = set()
    L = get_lines(n)
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            I = true_intersect(L[i][0], L[i][1], L[j][0], L[j][1])
            if I is not None:
                S.add(I)

    return S


def gcd(a, b):
    while b > 0:
        t = a % b
        a = b
        b = t

    return a