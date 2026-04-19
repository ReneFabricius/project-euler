import primes


def sum_from_base(b, ci, P, l):
    i = ci + 1
    ret = l//b
    while i < len(P):
        if b*P[i]**3 <= l:
            cb = b*P[i]**3
            while cb <= l:
                ret += sum_from_base(cb, i, P, l)
                cb*=P[i]
        else:
            break

        i += 1

    return ret


def pr694(l):
    P = primes.primes(round(l**(1/3)))
    return sum_from_base(1, -1, P, l)


def count_c_full_divs(n):
    D = primes.primeFactDecompPreinitialized(n)
    res = 1
    for p in D:
        if D[p] >= 3:
            res *= (D[p] - 1)

    return res

def pr694_naive(l):
    primes.initGlobalPrimes(round(l**(1/2)))
    ret = 0
    for i in range(1, l + 1):
        ret += count_c_full_divs(i)

    return ret