def digitSum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def findFirstN(n):
    D = {}
    b = 2
    A = []
    while len(A) < n:
        while True:
            e = 2
            if b in D:
                e = D[b] + 1
            
            D[b] = e
            p = b**e
            if digitSum(p) == b:
                A += [p]
                if len(A) >= n:
                    break
            
            
            if b > 2:
                pe = D[2] + 1
                if 2 ** pe < p*b:
                    b = 2
                    break
            
            ne = 2
            if b + 1 in D:
                ne = D[b + 1] + 1
            if (b + 1) ** ne < p:
                b += 1
                break
                
    A = sorted(A)
    print(A)
    m = A[n - 1]
    b_1 = 2
    while True:
        e_1 = 2
        if b_1 in D:
            e_1 = D[b_1] + 1
        
        while b_1 ** e_1 < m:
            p_1 = b_1 ** e_1
            if digitSum(p_1) == b_1:
                A += [p_1]
                A = sorted(A)
                m = A[n - 1]
                print(A)
            
            e_1 += 1
            
        b_1 += 1
        if b_1 ** 2 >= m:
            break
    
    
    return A
