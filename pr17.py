import inflect

def numberLetterCount(l):
    N = range(1, l + 1)
    p = inflect.engine()
    W = [p.number_to_words(n) for n in N]
    c = 0
    for w in W:
        for ch in w:
            if ch != ' ' and ch != '-':
                c += 1
                
    return c
