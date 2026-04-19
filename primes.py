from math import sqrt, log, ceil
from functools import reduce
from random import seed, randrange
from collections import Counter

prod = lambda L: reduce(lambda x, y: x*y, L, 1)

Pg = []
def initGlobalPrimes(n):
    global Pg
    Pg = primes(n)


def primes(n):
    "Vrati list prvocisel mensich alebo rovnych parametru"
    L = [True] * (n + 1)
    L[:2] = [False] * 2
    l = int(sqrt(n))
    for i in range(2,l + 1):
        if (L[i]):
            m = int(n/i) - i
            L[i*i::i] = [False] * (m + 1)
            
    return [p for p in range(len(L)) if L[p]]


def nthPrime(n):
    "Vrati n-teprvocislo"
    if (n < 6):
        P = primes(11)
        return P[n - 1]
    
    m = ceil(n * (log(n) + log(log(n))))
    P = primes(m)
    return P[n - 1]


def primeFactDecomp(n):
    "Najde prvociselny rozklad cisla"
    F = Counter()
    if (n == 1):
        F[1] += 1
        return F
        
    a = int(sqrt(n))
    c = False
    if (a > 10000000):
        a = 10000000
        c = True
    P = primes(a)
    for p in P:
        while (n % p == 0):
            n = n / p
            F[p] += 1
        if (n == 1):
            return F
            
    F[int(n)] += 1
    
    if not c:
        return F            # n musi byt prvocislo
        
    F[0] += 1
    return F                 # Nevieme urcit, ci n je prvocislo


def primeFactDecompPreinitialized(n):
    "Najde prvociselny rozklad cisla s pomocou vopred inicializovaneho zoznamu prvocisel (minimalne po sqrt(n))"
    F = Counter()
    if (n == 1):
        F[1] += 1
        return F
        
    a = int(sqrt(n))
    c = False
    
    for p in Pg:
        while (n % p == 0):
            n = n / p
            F[p] += 1
        if (n == 1):
            return F
        if (p > a):
            break
            
    F[int(n)] += 1
    
    return F


def divisorsNumber(n):
    "Najde pocet delitelov cisla"
    P = primeFactDecomp(n)
    P = Counter(P)
    d = 1
    for p in P:
        d *= P[p] + 1
    
    return d


def divisorsNumberPreinitialized(n):
    "Najde pocet delitelov cisla"
    P = primeFactDecompPreinitialized(n)
    P = Counter(P)
    d = 1
    for p in P:
        d *= P[p] + 1
    
    return d


def findDivisors(n):
    "Najde delitelov cisla"
    a = int(sqrt(n)) + 1
    D = set()
    for i in range(1, a):
        if (n % i == 0):
            D.add(i)
            D.add(int(n/i))
    
    return sorted(D)
    

def isPrime(n):
    if n <= 1:
        return False
    
    for p in range(2, int(sqrt(n)) + 1):
        if (n % p == 0):
            return False
    
    return True


def isPrimePreinitialised(n):
    if n <= 1:
        return False
    sq = int(sqrt(n))
    for p in Pg:
        if p > sq:
            break
        if n % p == 0:
            return False
    
    return True


def isPrimeMillerRabin(n, k):
    "Zisti, ci n je prvocislo, pravdepodobnost chyby je nanajvys 1/4**k"
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    m = n - 1
    t = 0
    while m % 2 == 0:
        t += 1
        m //= 2
        
    seed()
    for o in range(k):
        a = randrange(2, n - 1)
        x = pow(a, m, n)
        if x == 1 or x == n - 1:
            continue
        
        i = 1
        br = False
        while i < t:
            x = x*x % n
            i += 1
            if x == 1:
                return False
            if x == n - 1:
                br = True
                break
        if br:
            continue
        return False
    
    return True
    
    
def primesRang(m, n):
    "Najde prvocisla v zadanom rozsahu vratane medzi"
    P = primes(int(sqrt(n)))
    L = [True] * (n - m + 1)
    for p in P:
        s = ceil(m / p) * p                 # prvy nasobok p v zadanom rozsahu
        if (s > n):
            continue
        q = int((n - s) / p) + 1            # pocet vyskytov nasobkov p v zadanom rozsahu
        L[s - m::p] = [False] * q
        
    return [p + m for p in range(len(L)) if L[p]]
    

def totient(n):
    "Spocita Eulerovu funkciu argumentu"
    P = primeFactDecomp(n)
    P = set(P)
    t = n * prod([(1 - 1 / p) for p in P])
    return int(round(t))


def totientPreinitialized(n):
    "Spocita Eulerovu funkciu argumentu, nutne mat preinicializovane prvocisla minimalne do sqrt(n)"
    P = primeFactDecompPreinitialized(n)
    P = set(P)
    t = n * prod([(1 - 1 / p) for p in P])
    return int(round(t))


def isN_smooth(a, N):
    "Zisti, ci je cislo N-hladke"
    P = primes(N)
    for p in P:
        while a % p == 0:
            a //= p
    
    return a == 1


def isN_smoothPreinitialized(a, N):
    "Zisti, ci je cislo N-hladke, nutne mat preinicializovane prvocisla minimalne do N"
    for p in Pg:
        if p > N:
            break
        while a % p == 0:
            a //= p
    
    return a == 1


def rangePrimeFactDecomposition(l):
    "Vrati dekompoziciu vsetkych cisel mensich ako l"
    SD = [Counter() for i in range(1, l)]
    SD = [None] + SD    # Dekompozicie
    SD[1][1] = 1
    PS = [True for i in range(l)]       # Priznaky prvociselnosti
    for pc in range(2, l):
        if PS[pc]:                      # Je prvocislo
            pcp = pc                    # Mocnina pc
            while pcp < l:
                pcm = pcp               # Nasobok mocniny pcm
                while pcm < l:
                    SD[pcm][pc] += 1
                    pcm += pcp
                pcp *= pc

            for np in range(pc * pc, l, pc):
                PS[np] = False          # Eraostenes

    return SD


def increment_PES(PES, DC):
    pi = 0
    for p in DC:
        if PES[pi] < DC[p]:
            PES[pi] += 1
            return True
        else:
            PES[pi] = 0
        pi += 1

    return False


Factors = []
DCs = []


def comp_factors(n):
    global Factors
    global DCs

    if len(Factors) <= n:
        Factors += [None]*(n + 1 - len(Factors))

    if len(DCs) <= n:
        DCs += [None]*(n + 1 - len(DCs))

    if DCs[n] is None:
        DCs[n] = primeFactDecompPreinitialized(n)

    if Factors[n] is None:
        if n == 1:
            Factors[n] = [1]
            return

        PES = [0]*len(DCs[n])
        Factors[n] = []
        Factors[n].append(1)
        while increment_PES(PES, DCs[n]):
            f = 1
            pi = 0
            for p in DCs[n]:
                f *= p**PES[pi]
                pi += 1

            Factors[n].append(f)

        Factors[n].sort(reverse=True)


def get_pick(CHS, RS):
    ts = [1] * len(CHS)
    for i in range(len(CHS)):
        ts[i] = Factors[RS[i]][CHS[i]]

    return ts


def change_pick(RS, CHS):
    for i in range(len(CHS) - 1, -1, -1):
        if i < len(CHS) - 1 and CHS[i] < len(Factors[RS[i]]) - 1:
            CHS[i] += 1
            valid = True
            for j in range(i + 1, len(CHS)):
                RS[j] = RS[j - 1]//Factors[RS[j - 1]][CHS[j - 1]]
                comp_factors(RS[j])
                pi = 0
                while Factors[RS[j]][pi] > Factors[RS[j - 1]][CHS[j - 1]]:
                    pi += 1

                if j == len(CHS) - 1 and pi > 0:
                    valid = False
                    break

                CHS[j] = pi

            if valid:
                return True

        else:
            CHS[i] = 0
            RS[i] = 0

    return False


def all_decompositions_preinitialized_initializing(n):
    global Factors
    global DCs

    if len(DCs) <= n:
        DCs += [None]*(n + 1 - len(DCs))

    if DCs[n] is None:
        DCs[n] = primeFactDecompPreinitialized(n)


    e_sum = 0
    for p in DCs[n]:
        e_sum += DCs[n][p]

    RS = [n if i == 0 else 1 for i in range(e_sum)]
    CHS = [0]*e_sum
    comp_factors(n)
    comp_factors(1)
    RES = []

    changed = True
    while changed:
        RES.append(get_pick(CHS, RS))
        changed = change_pick(RS, CHS)

    return RES

def find_divisors_range(l):
    """
    Find divisors for all numbers in range [1, l]
    """
    decomps = rangePrimeFactDecomposition(l)
    
    def _compute_divisors(n):
        if n == 0:
            return []
        if n == 1:
            return [1]
        
        dec = decomps[n]
        divs = [1]
        pris = [p for p in dec]
        max_pows = [dec[p] for p in pris]
        cur_pows = [0 for p in pris]
        def _incr():
            nonlocal cur_pows
            cur_ind = len(cur_pows) - 1
            while cur_pows[cur_ind] == max_pows[cur_ind]:
                cur_ind -= 1
                if cur_ind < 0:
                    return False
            
            cur_pows[cur_ind] += 1
            for zero_ind in range(cur_ind + 1, len(cur_pows)):
                cur_pows[zero_ind] = 0
            return True
        
        while _incr():
            divs.append(prod([pris[i]**cur_pows[i] for i in range(len(cur_pows))]))
        
        return sorted(divs)
    
    divisors = [_compute_divisors(n) for n in range(l)]
    return divisors


def find_divisors_range_simple(l):
    """
    Simpler and faster version.
    """
    divisors = [[]] + [[1] for _ in range(1, l)]
    for d in range(2, l):
        if d < 100 or (d < 1000 and d % 100 == 0) or (d < 10000 and d % 1000 == 0) or (d < 100000 and d % 10000 == 0) or d % 100000 == 0:
            print(f"Applying d: {d}")
        for mult in range(d, l, d):
            divisors[mult].append(d)
    
    return divisors
