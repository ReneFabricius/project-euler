def pr288(p, q, m):
    S_0 = 290797
    SM = 50515093
    cur_s = S_0
    cur_s = pow(cur_s, 2, SM)

    cur_p = 1
    cur_p_sum = 1

    res = 0
    for k in range(1, q + 1):
        res = (res + (cur_s % p) * cur_p_sum) % m

        cur_s = pow(cur_s, 2, SM)

        cur_p = (cur_p * p) % m
        cur_p_sum = (cur_p_sum + cur_p) % m

    return res
