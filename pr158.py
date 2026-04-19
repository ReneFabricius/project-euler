from math import factorial
from itertools import permutations

def fun_p(p):
    n = 26
    nom = factorial(n) * (2**p - 2 - (p - 1))
    denom = factorial(p) * factorial(n - p)
    res = nom // denom

    return res

def fun_p_brute(p):
    n = 26
    L = [i for i in range(n)]
    I = [i for i in range(p)]
    count = 0
    fin = False
    while not fin:
        SE = [L[i] for i in I]

        for perm in permutations(SE):
            c_io = 0
            for i in range(1, p):
                if perm[i - 1] < perm[i]:
                    c_io += 1

            if c_io == 1:
                count += 1

        chi = p - 1
        while I[chi] == n - p + chi:
            chi -= 1
            if chi < 0:
                fin = True
                break

        if not fin:
            I[chi] += 1
            for i in range(chi + 1, p):
                I[i] = I[i - 1] + 1

    return count


def pr158():
    # Vo vsetkych p prvkovych klesavych podmnozinach mozes prehodit poradie 2 podmnozin, z ktorych jedna je neprazdna a neuplna a nie je spojita od zaciatku
    n = 26
    max = 0
    for p in range(2, n + 1):
        res = fun_p(p)
        if res > max:
            max = res
        print("p: " + str(p) + " : " + str(res))

    return max
