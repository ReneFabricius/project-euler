import math

def f_naive(n, d):
    c = 0
    d_c = str(d)
    for i in range(n + 1):
        i_c = str(i)
        c += i_c.count(d_c)
    
    return c

def f(n, d):
    c = 0
    if (n <= 0):
        return c
    a = int(math.log10(n))
    for i in range(1, a + 1):
        c += int((n % math.pow(10, i + 1))/math.pow(10, i))*i*math.pow(10, i-1)
        
    for j in range(a + 1):
        c += math.ceil(int((n % math.pow(10,j+1)/math.pow(10, j)))/9)*(n % math.pow(10,j+1) + 1 - abs(n % math.pow(10,j + 1) + 1 - 2*math.pow(10,j)))/2
        
    return c
