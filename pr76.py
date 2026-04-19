def problem76(n):
    W = [0 for _ in range(n + 1)]
    for mN in range(1, n + 1):
        for s in range(mN + 1, n + 1):
            W[s] += W[s - mN]
            if s - mN <= mN:
                W[s] += 1
    
    return W[n]

# PDF k problemu 31
