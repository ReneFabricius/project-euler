from copy import copy
from collections import defaultdict
from math import comb


def pr181(num_w, num_b):
    sq_len = max(num_w, num_b)
    res = [[set() for _ in range(sq_len)] for _ in range(sq_len)]
    res[0][0].add(frozenset({}.items()))
    for b in range(1, num_b):
        for prev_sol in res[b - 1][0]:
            prev_dict = defaultdict(lambda: 0, prev_sol)
            prev_dict_c = copy(prev_dict)
            prev_dict_c[(1, 0)] += 1
            res[b][0].add(frozenset(prev_dict_c.items()))
            for present in prev_dict:
                prev_dict_c = copy(prev_dict)
                prev_dict_c[present] -= 1
                if prev_dict_c[present] == 0:
                    del prev_dict_c[present]
                prev_dict_c[(present[0] + 1, present[1])] += 1
                res[b][0].add(frozenset(prev_dict_c.items()))

        for w in range(1, b + 1):
            for prev_sol in res[b][w - 1]:
                prev_dict = defaultdict(lambda: 0, prev_sol)
                prev_dict_c = copy(prev_dict)
                prev_dict_c[(0, 1)] += 1
                res[b][w].add(frozenset(prev_dict_c.items()))
                for present in prev_dict:
                    prev_dict_c = copy(prev_dict)
                    prev_dict_c[present] -= 1
                    if prev_dict_c[present] == 0:
                        del prev_dict_c[present]
                    prev_dict_c[(present[0], present[1] + 1)] += 1
                    res[b][w].add(frozenset(prev_dict_c.items()))

    for w in range(num_w):
        print(f"w: {w}: {[len(res[max(w, k)][min(w, k)]) for k in range(num_b)]}")
    return res


def all_partits(num_w, num_b):
    res = 0
    for s in range(min(num_w, num_b) + 1):
        res += comb(num_w, s) * comb(num_b, s) * 2 ** (num_b + num_w - s - 1)

    return res
