def problem53(l):
    c = 0
    for n in range(1, l + 1):
        x = 1
        for r in range(1, n//2):
            x *= n - r + 1
            x //= r
            if x > 10**6:
                c += n + 1 - 2 * r
                break
    
    return c
