from math import ceil, sqrt
from primes import primes

def cycleN(n):
    c = ceil((-3+sqrt(12*n-3))/6)
    c_N = n - 3*c*c + 3*c -1
    return c, c_N

def c_E(c):
    if c == 0:
        return 1
    return 3*c*c + 3*c + 1

def c_B(c):
    if c == 0:
        return 1
    return 3*c*c - 3*c + 2
    
def curCNGBRS(c_N, c):
    cyc_B = c_B(c)
    if c_N == 1:
        return [cyc_B + c_N, cyc_B + c*6 - 1]
    elif c_N == 6*c:
        return [cyc_B, cyc_B + c_N - 2]
    
    return [cyc_B + c_N, cyc_B + c_N - 2]
        

def getNeighbours(n):
    NGBRS = []
    c, c_N = cycleN(n)
    one_prev = ((c_N - 1) % c == 0)
    prev_beg = c_B(c - 1)
    next_beg = c_B(c + 1)
    if one_prev:
        dir_n = int((c_N - 1) / c)
        
        NGBRS += [prev_beg + (c-1)*dir_n]
        
        dir_next = next_beg + (c+1)*dir_n
        NGBRS += [dir_next]
        NGBRS += curCNGBRS((c+1)*dir_n + 1, c + 1)
    
    else:
        # 2 prev
        last_dir_n = (c_N - 1) // c
        mod = (c_N - 1) % c
        if mod == c - 1:
            next_dir_n = (last_dir_n + 1) % 6
            if next_dir_n == 0:
                NGBRS += [prev_beg, prev_beg + 6*(c - 1) - 1]
            else:
                NGBRS += [prev_beg + next_dir_n*(c-1), prev_beg + next_dir_n*(c-1) - 1]
        else:
            NGBRS += [prev_beg + (c-1)*last_dir_n + mod - 1, prev_beg + (c-1)*last_dir_n + mod]
        
        # 2 fol
        
        NGBRS += [next_beg + (c+1)*last_dir_n + mod, next_beg + (c+1)*last_dir_n + mod + 1]
            
    
    NGBRS += curCNGBRS(c_N, c)
    
    return NGBRS
    
def problem128(th):
    L = 10**7
    PS = set(primes(L))
    PD = [1]
    c = 1
    while len(PD) < th:
        cyc_B = c_B(c)
        cyc_E = c_E(c)
        for w_n in range(2):
            if w_n == 0:
                n = cyc_B
            else:
                n = cyc_E
            
            NGBRS = getNeighbours(n)
            DIFF = [abs(n - ngbr) for ngbr in NGBRS]
            pc = 0
            for diff in DIFF:
                if diff > L:
                    print("Limit prekroceny: " + str(diff))
                if diff in PS:
                    pc += 1
                    if pc == 3:
                        PD += [n]
                        break
            
        c += 1
    
    return PD
        
    
