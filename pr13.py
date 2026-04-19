def sumNumb():
    f = open("pr13_numbers.txt", 'r')
    N = []
    for l in f:
        N.append(int(l))
    f.close()
    s = sum(N)
    return s
