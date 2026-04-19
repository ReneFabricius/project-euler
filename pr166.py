import torch
from timeit import default_timer as timer


def pr166():
    ts = timer()
    INn = 9
    F = torch.zeros(INn, 1, dtype=torch.float).cuda()
    D = torch.tensor(
        [[1,0,1,1,0,-1,0,-1,0],
         [-2,0,-1,-1,1,2,1,1,0],
         [1,1,1,1,-1,-1,-1,0,0],
         [0,0,0,-1,1,1,1,0,-1],
         [1,1,1,0,0,0,-1,-1,0],
         [1,0,1,1,-2,-1,-1,0,1],
         [-1,1,0,0,2,1,0,0,-1]], dtype=torch.float).cuda()

    eqc = D.size()[0]
    count = 0
    m = 10**(INn - 2)
    for i in range(10**5):
        if i % m == 0:
            print(i//m)

        V = torch.mm(D, F)

        if sum((0 <= V) * (V <= 9)) == eqc:
            count += 1

        k = INn - 1
        while F[k][0] == 9 and k >= 0:
            F[k][0] = 0
            k -= 1

        if k >= 0:
            F[k][0] += 1

    return count, timer() - ts


