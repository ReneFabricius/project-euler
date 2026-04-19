import math

def naive_bad_solution(n, lc):
    ct = 0
    for nz in range(n - lc + 1):
        ct += 10**(n-lc-nz)

    nms = []
    cts = []
    for i in range(2, 10**lc):
        if i % 10 != 0:
            nms.append(i)
            cts.append(ct)
            cl = math.ceil(math.log(i, 10))
            cts[-1] += lc - cl


    res = 1
    for i in range(nms.__len__()):
        print(nms[i], " ", cts[i])
        res *= nms[i]**cts[i]

    return res, math.factorial(10**n)

def proof_of_concept(n, lc):
    cf = 0
    modulator = 10**lc
    res = 1
    for i in range(2, 10**n):
        j = i
        while j % 5 == 0:
            j //= 5
            cf += 1

        while cf > 0 and j % 2 == 0:
            j //= 2
            cf -= 1

        j %= modulator

        res *= j
        res %= modulator

    f = math.factorial(10**n)
    while f % 10 == 0:
        f //= 10

    return res, f % modulator

def pr160(n, lc):
    fin_num = 10**n
    nums = [i for i in range(2, 10**lc)]
    pows = [0 for i in range(2, 10**lc)]

    considering = []

    bds = [2, 5]
    mult = 10**lc
    ii = 0
    while True:
        denoi = bds[0]**ii
        if denoi > fin_num:
            break

        jj = 0
        while True:
            deno = denoi * bds[1]**jj

            if deno > fin_num:
                break

            for i in range(nums.__len__()):
                if nums[i]*deno > fin_num:
                    break
                if nums[i] % 2 != 0 and nums[i] % 5 != 0:
                    '''count = 1 + max(int((fin_num/deno - nums[i])/mult), 0)
                    print("For ", deno, " considering ", nums[i], " times ", count)
                    for ci in range(count):
                        considering.append((ci*mult + nums[i])*deno)'''
                    pows[i] += 1 + max(int((fin_num/deno - nums[i])/mult), 0)

            jj += 1

        ii += 1

    counts = [0, 0]
    for bdi in range(bds.__len__()):
        deno = bds[bdi]
        while deno <= fin_num:
            counts[bdi] += int(fin_num/deno)
            deno *= bds[bdi]

    pows[0] = counts[0] - counts[1]

    res = 1
    for i in range(nums.__len__()):
        res *= pow(nums[i], pows[i], mult)
        res %= mult

    '''for i in range(nums.__len__()):
        if pows[i] != 0:
            print(nums[i], " ",  pows[i])'''

    return res


def naive_sol(n, lc):
    mod = 10**lc
    res = 1
    for i in range(2, 10**n + 1):
        res *= i

    while res % 10 == 0:
        res //= 10

    res %= mod

    return res

if __name__ == "__main__":
    pr160(2, 5)