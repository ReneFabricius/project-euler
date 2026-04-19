from primes import primeFactDecomp

def findPythaTrip(s):
    "Najde Pytagorejsku trojicu ktorej sucet je rovny s"
    
    for n in range(1, int(s / 2) + 1):
        Fn = primeFactDecomp(n)
        for m in range(n + 1, int(s / 2) + 1, 2):
            Fm = primeFactDecomp(m)
            I = set.intersection(set(Fn), set(Fm))
            if (len(I) == 0):                           # Nesudelitelne m,n kde prave jedno z nich je parne generuju Pytagorejsku trojicu v zakaladnom tvare
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                if (s % (a + b + c) == 0):
                    q = s / (a + b + c)
                    return [q*a, q*b, q*c], q*a * q*b * q*c

    return [], 0
