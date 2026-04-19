from gmpy2 import mpq

def problem155(n):
    ic = mpq(1, 1)
    c_sets = {1 : set([ic])}
    s = set(c_sets[1])
    for i in range(2, n + 1):
        c_sets[i] = set()
        f = 1
        while f <= i - f:
            for fc in c_sets[f]:
                for sc in c_sets[i - f]:
                    paralel_c = fc*sc/(fc + sc)
                    c_sets[i].add(paralel_c)
                    serial_c = fc + sc
                    c_sets[i].add(serial_c)
            
            f += 1
        s = s | c_sets[i]
    
    return s
        
