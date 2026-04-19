from itertools import permutations

def problem43():
    D = "0123456789"
    s = 0
    for p in permutations(D):
        if p[0] == '0':
            continue
        if int(p[3]) % 2 != 0:      # 2
            continue
        if int(p[5]) % 5 != 0:      # 5
            continue
        if int(''.join(p[2:5:])) % 3 != 0:      # 3
            continue
        if int(''.join(p[4:7:])) % 7 != 0:      # 7
            continue
        if int(''.join(p[5:8:])) % 11 != 0:      # 11
            continue
        if int(''.join(p[6:9:])) % 13 != 0:      # 13
            continue
        if int(''.join(p[7::])) % 17 != 0:      # 17
            continue
        
        s += int(''.join(p))
    
    return s
        
