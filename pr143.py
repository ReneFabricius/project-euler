from math import sqrt, gcd

def findSomeNmbrs():
    i = 1
    while True:
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                a = sqrt(i*i + i*j + j*j)
                b = sqrt(i*i + i*k + k*k)
                c = sqrt(j*j + j*k + k*k)
                if a.is_integer() and b.is_integer() and c.is_integer():
                    print(i, j, k, a, b, c)
        i += 1
                
def problem143(l):
    m = 1
    L = int(sqrt(l))
    P_1 = {}
    while m <= L:
        for p_n in range(1, m):
            if gcd(p_n, m) == 1:
                n = -p_n
                b_x = (n*n-2*m*n)
                b_y = (m*m-n*n)
                if b_x % 3 == 0 and b_y % 3 == 0:
                    b_x /= 3
                    b_y /= 3
                x = b_x
                y = b_y
                while x + y < l:
                    if x in P_1:
                        P_1[x].add(y)
                    else:
                        P_1[x] = set([y])
                    
                    if y in P_1:
                        P_1[y].add(x)
                    else:
                        P_1[y] = set([x])
                    x += b_x
                    y += b_y
        
        m += 1
    
    T = []
    
    while P_1:
        pr = P_1.popitem()
        while pr[1]:
            sc = pr[1].pop()
            for tc in P_1[sc]:
                if tc in pr[1]:
                    T += [(pr[0], sc, tc)]
            P_1[sc].remove(pr[0])
    
    
    S = set()        
    for t in T:
        if sum(t) <= l:
            S.add(sum(t))
    
    return T, sum(S)
                
                
