def palinFrom23Ciph():
    "Najde najvacsi palindrom ktory vznikne sucinom dvoch trojcifernych cisel"
    p = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            x = j * i
            x0 = x % 10
            x5 = int(x / 100000)
            if (x5 == x0):
                x1 = (x % 100 - x0) / 10
                x4 = int((x - x5 * 100000) / 10000)
                if (x1 == x4):
                    x3 = int((x - x5 * 100000 - x4 * 10000) / 1000)
                    x2 = int((x - x5 * 100000 - x4 * 10000 - x3 * 1000) / 100)
                    if (x3 == x2):
                        if (x > p):
                            p = x
    
    return p
