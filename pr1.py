def sum35MultsBel(n):
    p3 = int((n - 1) / 3)
    p5 = int((n - 1) / 5)
    p15 = int((n - 1) / 15)
    m3 = n - 1 - ((n - 1) % 3)
    m5 = n - 1 - ((n - 1) % 5)
    m15 = n - 1 - ((n - 1) % 15)
    if (p3 < 1):
        return 0
    if (p5 < 1):
        return 3
    s3 = p3 * (3 + m3) / 2
    s5 = p5 * (5 + m5) / 2
    s15 = p15 * (15 + m15) / 2
    
    return s3 + s5 - s15

def sum35MultsBelStu(n):
    s = 0
    for i in range(n):
        if (i % 3 == 0 or i % 5 == 0):
            s += i
    
    return s
