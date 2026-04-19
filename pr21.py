from primes import findDivisors

def sumAmicableBel(n):
    A = set()
    for i in range(2, n):
        di = sum(findDivisors(i)) - i
        ddi = sum(findDivisors(di)) - di
        if (ddi == i and i != di):
            A.add(i)
    
    return sum(A)
