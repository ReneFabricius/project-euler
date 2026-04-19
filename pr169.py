def pr169(N):
    if N == 0:
        return 1
    
    b = bin(N)[2:]
    N = 1
    P = 0
    pos = len(b) - 1
    while pos >= 0:
        A = 0
        while b[pos] != '1':
            pos -= 1
            A += 1

        nN = N + P
        P = A*N + (A + 1)*P
        N = nN
        pos -= 1

    return N + P
