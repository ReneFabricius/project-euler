def extEuclid(a, b):
    sw = False
    if a < b:
        a, b = b, a
        sw = True
    
    r = [a, b]
    s = [1, 0]
    t = [0, 1]
    while r[1] != 0:
        s = [s[1], s[0] - (r[0] // r[1]) * s[1]]
        t = [t[1], t[0] - (r[0] // r[1]) * t[1]]
        r = [r[1], r[0] % r[1]]
    
    if sw:
        return (r[0], t[0], s[0])
    
    return (r[0], s[0], t[0])
