from itertools import combinations
from functools import reduce

def computeProbability(t):
    ml = int((t-1)/2)
    n = 1
    mul = lambda a, b: a*b
    for l in range(1, ml + 1):
        for c in combinations(range(1, t + 1), l):
            n += reduce(mul, c)
    
    d = reduce(mul, range(2, t + 2))
    return n, d 

def problem121(t):
    n, d = computeProbability(t)
    return int(d/n)
