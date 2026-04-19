
def problem56():
    s = 0
    ma = 0
    mb = 0
    for a in range(1, 100):
        for b in range(1, 100):
            x = pow(a, b)
            cs = 0
            while x:
                cs += x % 10
                x //= 10
            
            if cs > s:
                s = cs
                ma = a
                mb = b
    
    return s, ma, mb
