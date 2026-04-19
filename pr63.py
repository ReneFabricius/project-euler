def problem63():
    c = 0
    for n in range(1, 10):
        e = 1
        while True:
            l = len(str(n**e))
            if l == e:
                c += 1
            if l < e:
                break
            e += 1
    
    return c
