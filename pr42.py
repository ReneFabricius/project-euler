
def wordValue(w):
    v = 0
    for l in w:
        v += ord(l) - 64
        
    return v

def problem42():
    T = set()
    s = 0
    for n in range(1, 51):
        s += n
        T.add(s)
        
    c = 0
    f = open('p042_words.txt', 'r')
    for l in f:
        for w in l.split(','):
            if wordValue(w[1:-1:]) in T:
                c += 1
    
    f.close()
    
    return c
