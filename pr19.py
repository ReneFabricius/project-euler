
def countMondays1st():
    n = 0
    c = 0
    for y in range(1900, 2001):
        for m in range(1, 13):
            if n % 7 == 6 and y > 1900:
                c += 1
            if m == 2:
                if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                    n += 29
                else:
                    n +=  28
            elif m in[4, 6, 9, 11]:
                n += 30
            else:
                n += 31
    
    return c
                    
