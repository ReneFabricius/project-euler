def problem44(l):
    P = []
    for i in range(1, 2*l + 1):
        P += [int((i*(3*i - 1))/2)]
    
    PS = set(P)
    m = 5482661
    PP = []
    for j in range(0, l - 1):
        for k in range(j + 1, l):
            if (P[j] + P[k]) in PS and (P[k] - P[j]) in PS:
                PP += [(j, k, P[j], P[k], P[k] - P[j])]
    
    return PP
