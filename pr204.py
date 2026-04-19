from primes import primes

def problem204(p, l):
    b = primes(p)

    s = [1]
    c_i = [0 for k in b]
    c = [p for p in b]
    i = 1
    while True:
        nxt = min(c)
        if nxt > l:
            return s
        s+= [nxt]
        i += 1

        for ind, val in enumerate(c):
            if val == nxt:
                c_i[ind] += 1
                c[ind] = b[ind] * s[c_i[ind]]

