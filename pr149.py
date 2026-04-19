
def problem149():
    LF = []
    for k in range(1, 56):
        LF.append(((100003 - 200003*k + 300007*k*k*k) % 1000000) - 500000)
    
    for k in range(55, 4000000):
        LF.append(((LF[k-24] + LF[k-55] + 1000000) % 1000000) - 500000)
    
    M = []
    for i in range(2000):
        M.append(LF[i*2000:(i+1)*2000])
    
    ms = 0
    
    for row in range(2000):
        s = 0
        cms = 0
        for col in range(2000):
            s += M[row][col]
            if s < 0:
                s = 0
            if s > cms:
                cms = s
        
        if cms > ms:
            ms = cms
            
        
    
    print("Rows done")
    
    for col in range(2000):
        s = 0
        cms = 0
        for row in range(2000):
            s += M[row][col]
            if s < 0:
                s = 0
            if s > cms:
                cms = s
        
        if cms > ms:
            ms = cms
    
    print("Columns done")
    
    
    for row in range(2000):
        col = 0
        s = 0
        cms = 0
        while row >= 0 and col < 2000:
            s += M[row][col]
            if s < 0:
                s = 0
            if s > cms:
                cms = s
            
            col += 1
            row -= 1
        
        if cms > ms:
            ms = cms
    
    for col in range(2000):
        row = 1999
        s = 0
        cms = 0
        while row >= 0 and col < 2000:
            s += M[row][col]
            if s < 0:
                s = 0
            if s > cms:
                cms = s
            
            col += 1
            row -= 1
        
        if cms > ms:
            ms = cms
    
    print("Diagonals done")
    
    for row in range(2000):
        col = 0
        s = 0
        cms = 0
        while row < 2000 and col < 2000:
            s += M[row][col]
            if s < 0:
                s = 0
            if s > cms:
                cms = s
                
            row += 1
            col += 1
        
        if cms > ms:
            ms = cms
    
    for col in range(2000):
        row = 0
        s = 0
        cms = 0
        while row < 2000 and col < 2000:
            s += M[row][col]
            if s < 0:
                s = 0
            if s > cms:
                cms = s
                
            row += 1
            col += 1
        
        if cms > ms:
            ms = cms
    
    return ms
    
