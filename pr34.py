from math import factorial
from itertools import combinations_with_replacement as c_w_r

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
    C = list(c_w_r(range(10), 7))               # pre 9999999 je sucet fektorialov mensi ako cislo
    for n in range(10, 362880 * 7 + 1):      
        if n == getSumOfFacts(n):
            s += n
    
    return s
