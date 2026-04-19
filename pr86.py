from math import sqrt

def problem86(l):
    M = 2
    c = 0
    while True:
        for S in range(2, 2*M + 1):
            if sqrt(M*M + S*S).is_integer():                    # Ak A <= B <= C su strany kvadra, najkratsia cesta je sqrt(C*C + (A+B)*(A+B))
                st = S - 1 - M
                if st < 0:
                    st = 0
                c += S//2 - st
        if c >= l:
            return M
        
        M += 1
