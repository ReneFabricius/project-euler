from itertools import combinations

def problem90():
    c = 0
    for c1 in combinations(range(10), 6):
        for c2 in combinations(range(10), 6):
            if not ((0 in c1 and 1 in c2) or (1 in c1 and 0 in c2)):        # 01
                continue
            if not ((0 in c1 and 4 in c2) or (4 in c1 and 0 in c2)):        # 04
                continue
            if not ((0 in c1 and (6 in c2 or 9 in c2)) or ((6 in c1 or 9 in c1) and 0 in c2)):          # 09
                continue
            if not ((1 in c1 and (6 in c2 or 9 in c2)) or ((6 in c1 or 9 in c1) and 1 in c2)):          # 16
                continue
            if not ((2 in c1 and 5 in c2) or (5 in c1 and 2 in c2)):        # 25
                continue
            if not ((3 in c1 and (6 in c2 or 9 in c2)) or ((6 in c1 or 9 in c1) and 3 in c2)):          # 36
                continue
            if not ((4 in c1 and (6 in c2 or 9 in c2)) or ((6 in c1 or 9 in c1) and 4 in c2)):          # 49, 64
                continue
            if not ((8 in c1 and 1 in c2) or (1 in c1 and 8 in c2)):        # 81
                continue
            c += 1
    
    return c // 2            # a1, a2 == a2, a1
