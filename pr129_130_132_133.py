from collections import Counter
from math import sqrt, ceil
import primes
# Zalozene na fakte: R(k) * 9 = 10**k - 1, s pomocou http://mathworld.wolfram.com/MultiplicativeOrder.html
# prvocislo 1000171 dava A(p) > 10**6
primes.initGlobalPrimes(int(sqrt(9001530)))

def multiplicativeOrder129(m):
    "Spocita rad cisla 10 modulo argument"
    t = primes.totientPreinitialized(m)
    e = 2
    uO = t
    while e*e <= t:
        if t % e == 0:
            if pow(10, e, m) == 1:
                return e
            
            if pow(10, int(t/e), m) == 1:
                uO = int(t/e)
        e += 1
    
    return uO
    
def A(n):
    "Najmensia dlzka repunitu delitelneho argumentom"
    if n % 3 == 0:
        return multiplicativeOrder129(n * 9)
    else:
        return multiplicativeOrder129(n)
            
def firstOverL(L):
    "Problem 129, spocita najmensie n, pre ktore je A(n) > L"
    for n in range(ceil(ceil(L/9)/3)*3, L, 3):
        if n % 2 == 0 or n % 5 == 0:
            continue
            
        if A(n) >= L:
            return n
    
    for n in range(L, 1000172):
        if n % 2 == 0 or n % 5 == 0:
            continue
            
        if A(n) >= L:
            return n
                
def problem130():
    Pr = set(primes.primes(10000000))
    S = []
    n = 7
    while len(S) < 25:
        if n % 2 != 0 and n % 5 != 0 and n not in Pr:
            a = A(n)
            if (n - 1) % a == 0:
                S += [n]
        n += 1
    
    print(S)
    return sum(S)
    
def problem132(k, l):
    "Najde prvych l prvociselnych faktorov repunitu o dlzke 10**k"
    P = primes.primes(10000000)
    P = P[3::]
    S = []
    for p in P:
        a = A(p)
        i = k
        while a % 2 == 0:
            a //= 2
            i -= 1
        if i < 0:
            continue
        
        i = k
        while a % 5 == 0:
            a //= 5
            i -= 1
        if i >= 0 and a == 1:
            S += [p]
            if len(S) == l:
                print(S)
                return sum(S)
    
    print(S)
    return sum(S)
    
def problem133(l):
    "Najde sumu vsetkych prvocisel mensich ako l, ktore nemozu delit repunit o dlzke 10**n"
    P = primes.primes(l)
    s = 10              # 2 + 3 + 5
    for i in range(3, len(P)):
        n = A(P[i])
        while n % 5 == 0:
            n //= 5
        while n % 2 == 0:
            n //= 2
        
        if n != 1:
            s += P[i]
    
    return s
