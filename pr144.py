from math import tan, atan, isclose, sqrt

def countReflec():
    P0 = (0.0, 10.1)
    P1 = (1.4, -9.6)
    
    c = 1
    while True:
        ra = tan(2*atan(-4*P1[0]/P1[1]) - atan((P1[1] - P0[1])/(P1[0] - P0[0])))
        x2 = (-ra * (P1[1] - ra * P1[0]) + 2 * sqrt(25 * (4 + ra**2) - (P1[1] - ra * P1[0])**2)) / (4 + ra**2)
        if isclose(x2, P1[0]):
            x2 = (-ra * (P1[1] - ra * P1[0]) - 2 * sqrt(25 * (4 + ra**2) - (P1[1] - ra * P1[0])**2)) / (4 + ra**2)
            
        y2 = ra * (x2 - P1[0]) + P1[1]
        if -0.01 <= x2 <= 0.01 and y2 > 0:
            break
        P0 = P1
        P1 = (x2, y2)
        c += 1
    return c
