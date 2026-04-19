from euclidean_alg import extEuclid

def pr175(a, b):
    gcd = extEuclid(a, b)[0]
    a, b = b // gcd, a // gcd

    path = []
    while a != 1 or b != 1:
        if a < b:
            path.append(0)
            b = b - a
        else:
            path.append(1)
            a = a - b

    level = len(path)
    pos = 0
    for i in range(len(path)):
        pos = 2 * pos + path[len(path) - i - 1]

    n = 2 ** level + pos

    return n, SBE(n)


def SBE(n):
    bn = bin(n)[2:]
    cs = '1'
    exp = []
    i = 0
    while i < len(bn):
        c = 0
        while i < len(bn) and bn[i] == cs:
            c += 1
            i += 1

        if cs == '1':
            cs = '0'
        else:
            cs = '1'

        exp.append(c)

    return exp