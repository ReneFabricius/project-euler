from primes import primes


def problem609(l):
    P = primes(l)
    L_P = [P[-1], len(P)]
    D_L = [l - L_P[0]]

    while L_P[-1] > 1:
        l_ind = 0
        while P[l_ind] <= L_P[-1]:
            l_ind += 1

        prim = P[l_ind - 1]
        D_L.append(L_P[-1] - prim)
        L_P[-1] = prim
        L_P.append(l_ind)

    C = {}
    for i in range(len(L_P) + 1):
        C[i] = 0

    while len(L_P) >= 2:
        prim_c = D_L[1::].count(0)
        c_l = len(L_P)
        if c_l > 2:
            C[len(L_P) - prim_c] += D_L[0]
            C[len(L_P) - prim_c - 1] += 1
            c_l -= 1

        while c_l >= 2:
            C[c_l - prim_c] += D_L[0]
            C[c_l - prim_c - 1] += 1
            c_l -= 1
            if len(D_L) > c_l and D_L[c_l] == 0:
                prim_c -= 1

        D_L[0] = -1
        ct_i = 0
        while D_L[ct_i] == -1:
            if ct_i == len(D_L) - 1:
                L_P[ct_i] = 1
                L_P = L_P[:-1:]
                D_L = D_L[:-1:]
                break

            D_L[ct_i] = L_P[ct_i] - 1 - P[L_P[ct_i + 1] + D_L[ct_i + 1] - 2]
            L_P[ct_i] = P[L_P[ct_i + 1] + D_L[ct_i + 1] - 2]

            D_L[ct_i + 1] -= 1
            ct_i += 1

    res = 1
    for k in C:
        if C[k] > 0:
            res *= C[k]
    
    return C, res % 1000000007
    
    
