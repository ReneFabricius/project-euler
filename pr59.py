from itertools import permutations

def problem59():
    f = open('p059_cipher.txt', 'r')
    s = f.read()
    f.close()
    C = [int(c) for c in s.split(',')]
    pt = range(97, 123)         # a - z
    D = [0 for i in range(len(C))]
    for prm in permutations(pt, 3):
        for j in range(len(C)):
            D[j] = C[j] ^ prm[j % 3]
        
        Ds = ''.join(chr(ch) for ch in D)
        if 'glory' in Ds:
            print(Ds)
            return sum(D), ''.join(chr(ch) for ch in prm)
