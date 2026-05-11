from math import factorial

FA = [factorial(i) for i in range(10)]


def getSumOfFacts(n):
    D = []
    while n:
        D += [n % 10]
        n //= 10

    F = [FA[d] for d in D]
    return sum(F)


def sumOfFactDig():
    s = 0
    for n in range(10, 362880 * 7 + 1):
        if n == getSumOfFacts(n):
            s += n

    return s
