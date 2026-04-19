def problem92(l):
    E1 = set([1])
    E89 = set([89])
    for n in range(1, l):
        sq = n
        while True:
            if sq in E1:
                E1.add(n)
                break
            if sq in E89:
                E89.add(n)
                break
            nsq = 0
            while sq:
                nsq += (sq % 10)*(sq % 10)
                sq //= 10
            sq = nsq
    
    return len(E89)
