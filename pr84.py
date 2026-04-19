# Nepouzitelne pomale

from enum import Enum

class Box(Enum):
    GO      = 0
    A1      = 1
    CC1     = 2
    A2      = 3
    T1      = 4
    R1      = 5
    B1      = 6
    CH1     = 7
    B2      = 8
    B3      = 9
    JAIL    = 10
    C1      = 11
    U1      = 12
    C2      = 13
    C3      = 14
    R2      = 15
    D1      = 16
    CC2     = 17
    D2      = 18
    D3      = 19
    FP      = 20
    E1      = 21
    CH2     = 22
    E2      = 23
    E3      = 24
    R3      = 25
    F1      = 26
    F2      = 27
    U2      = 28
    F3      = 29
    G2J     = 30
    G1      = 31
    G2      = 32
    CC3     = 33
    G3      = 34
    R4      = 35
    CH3     = 36
    H1      = 37
    T2      = 38
    H2      = 39
    
D6 = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]             # Probabilities of sums 2...12 on two 6-sided dices
D4 = [1/16, 2/16, 3/16, 4/16, 3/16, 2/16, 1/16]                                     # Probabilities of sums 2...8 on two 4-sided dices

def problem84(dc, dpt):
    B = [0 for _ in range(40)]
    
    def play(box, cp, st, cdpt, cst):                                                # box - index of box on which player landed, cp - current probability, st - starting call, cdpt - current depth, cst - consecutive two - sums
        nonlocal B
        if cst == 3:                            # 3 consecutive twos - go to JAIL
            box = 10                
            cst = 0
        
        if box == 30:                           # G2J box
            box = 10
        
        if box in {2, 17, 33}:                  # Community chest
            play(0, cp * 1/16, False, cdpt, cst)    # Advance to GO
            play(10, cp * 1/16, False, cdpt, cst)   # GTJ
            cp *= 14 / 16
        
        if box in {7, 22, 36}:                  # Chance
            play(0, cp * 1/16, False, cdpt, cst)    # Advance to GO
            play(10, cp * 1/16, False, cdpt, cst)   # GTJ
            play(11, cp * 1/16, False, cdpt, cst)   # Go to C1
            play(24, cp * 1/16, False, cdpt, cst)   # Go to E3
            play(39, cp * 1/16, False, cdpt, cst)   # Go to H2
            play(5, cp * 1/16, False, cdpt, cst)   # Go to R1
            
            if box == 7:                                            # CH1
                play(15, cp * 2/16, False, cdpt, cst)   # Go to R2
                play(12, cp * 1/16, False, cdpt, cst)   # Go to U1
            
            elif box == 22:                                           # CH2
                play(25, cp * 2/16, False, cdpt, cst)   # Go to R3
                play(28, cp * 1/16, False, cdpt, cst)   # Go to U2
            
            else:                                                   # CH3
                play(5, cp * 2/16, False, cdpt, cst)   # Go to R1
                play(12, cp * 1/16, False, cdpt, cst)   # Go to U1
            
            play(box - 3, cp * 1/16, False, cdpt, cst)   # Go back 3 squares
            cp *= 6/16
        
        if not st:
            B[box] += cp
        
        if cdpt == 0:
            return
        
        
        if dc == 6:
            play((box + 2) % 40, cp * D6[0], False, cdpt - 1, cst + 1)
            for s in range(1, 11):
                play((box + s + 2) % 40, cp * D6[s], False, cdpt - 1, 0)
        
        elif dc == 4:
            play((box + 2) % 40, cp * D4[0], False, cdpt - 1, cst + 1)
            for s in range(1, 7):
                play((box + s + 2) % 40, cp * D4[s], False, cdpt - 1, 0)
    
    
    
    
    
    play(0, 1, True, dpt, 0)
    
    B[:] = [b / dpt for b in B]
    
    for bi in range(len(B)):
        print(Box(bi).name + ": " + str(B[bi]))
    
    return sum(B)
