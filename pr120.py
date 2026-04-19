def problem120(l,u):
    s = 0
    for a in range(l, u + 1):
        im = (2*a) % (a*a)
        m = (im + 4*a) % (a*a)
        mm = im
        while m != im:
            if m > mm:
                mm = m
            m = (m + 4*a) % (a*a)
        s += mm
    
    return s
