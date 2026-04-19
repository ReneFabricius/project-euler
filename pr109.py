def countCheckouts(Lmt):
    P = [i for i in range(1, 21)]
    d_P = [2*i for i in P]
    t_P = [3*i for i in P]
    P = P + d_P + t_P + [25, 50]
    D = [0] * 20 + [1] * 20 + [0]*20 + [0, 1]
    counter = 0
    
    
    for k in range(len(P)):
        if D[k] == 1 and P[k] <= Lmt:
            counter += 1
        
        for l in range(k, len(P)):
            if  P[l] + P[k] <= Lmt:
                dst_1 = list(set([k, l]))
                d_d_1 = sum([D[y] for y in dst_1])
                counter += d_d_1
            
            for m in range(l, len(P)):
                if P[l] + P[k] + P[m] <= Lmt: 
                    dst_2 = list(set([k, l, m]))
                    d_d_2 = sum([D[z] for z in dst_2])
                    counter += d_d_2
                    
    return counter
