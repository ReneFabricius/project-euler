from math import factorial

def sumDigitsFact100():
    f = factorial(100)
    D = []
    while f != 0:
        D += [f % 10]
        f //= 10
    return sum(D)
