def adjaProd(n):
    "Najde n za sebou iducich cisel s najvacsim sucinom"
    f = open('1000-digit_number.txt', 'r')
    L = []
    while True:
        c = f.read(1)
        if not c:
            break
        if (c != '\n'):
            L.append(int(c))
        
    f.close()
    
    
    s = 1
    for i in range(n):
        s *= L[i]

    m = s
    M = L[0:n]
    
    for j in range(n, len(L)):
        if (L[j - n] == 0):
            s = 1
            for k in range(j - n + 1, j):
                s *= L[k]
        else:
            s /= L[j - n]
            
        s *= L[j]
        if (s > m):
            m = s
            M = L[j - n + 1 : j + 1]
    
    print(M)
    return m
