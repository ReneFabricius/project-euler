def pr162(N):
    res = 0
    for n in range(3, N+1):
        c_0f = 1
        for c_0 in range(1, n-2+1):
            c_0f *= c_0
            c_1f = 1
            for c_1 in range(1, n-c_0-1+1):
                c_1f *= c_1
                c_Af = 1
                for c_A in range(1, n-c_0-c_1+1):
                    c_Af *= c_A
                    cr = (n-c_0)*13**(n-c_0-c_1-c_A)
                    for i in range(n-c_0-c_1-c_A+1, n-1+1):
                        cr *= i
                    cr //= (c_0f*c_1f*c_Af)
                    res += cr
    return res

def pr162_bf(N):
    i = 1
    res = 0
    chs = ['0', '1', 'a']
    while len(hex(i)) <= N + 2:
        h = hex(i)
        hs = [False, False, False]
        for chi in range(2, len(h)):
            for tsti in range(len(chs)):
                if h[chi] == chs[tsti]:
                    hs[tsti] = True

        if sum(hs) == 3:
            res += 1
        i += 1

    return res