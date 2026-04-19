from itertools import combinations, permutations, product

def getTargetConsLength(L):
    T = set()
    O = ['+', '-', '*', '/']
    B = [   ('', '', '', '', '', ''),
            ('(', '', ')', '', '', ''),
            ('', '', '', '(',  '', ')'),
            ('', '(', '', '', ')', ''),
            ('(', '', '', '', ')', ''),
            ('', '(', '', '', '', ')'),
            ('((', '', ')', '', ')', ''),
            ('(', '(', '', '', '))', ''),
            ('', '((', '', '', ')', ')'),
            ('', '(', '', '(', '', '))')]
    for dp in permutations(L):
        for op in product(O, repeat = 3):
            for b in B:
                try:
                    x = eval(b[0] + dp[0] + op[0] + b[1] + dp[1] + b[2] + op[1] + b[3] + dp[2] + b[4] + op[2] + dp[3] + b[5])
                except ZeroDivisionError:
                    x = 0.1
                if x % 1 == 0 and x > 0:
                    T.add(int(x))
    
    lc = 0
    T = list(T)
    pt = 0
    cc = 0
    for t in T:
        if t - pt == 1:
            cc += 1
            if cc > lc:
                lc = cc
        else:
            cc = 1
        pt = t
            
    return lc
    
def problem93():
    Lc = ()
    Lcl = 0
    for c in combinations([str(x) for x in range(10)], 4):
        ccl = getTargetConsLength(c)
        if ccl > Lcl:
            Lcl = ccl
            Lc = c
    
    return Lc
