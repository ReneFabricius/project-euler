def longstCollSeqSBel(l):
    MS = []
    for s in range(3, l, 2):
        S = [s]
        while S[-1] != 1:
            if S[-1] % 2 == 0:
                S.append(S[-1] / 2)
            else:
                S.append(S[-1] * 3 + 1)
        if len(S) > len(MS):
            MS = S
    
    return len(MS), MS
