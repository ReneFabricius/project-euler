class MyCacher:
    D = {}
    def __init__(self, func):
        self.func = func
        
    def __call__(self, n):
        if n in self.D:
            return self.D[n]
        res = self.func(n)
        self.D[n] = res
        return res
        

def countBlockCombs(l):
    
    
    @MyCacher
    def computeWays(n):
        c = 1
        ml = 4
        if n < ml:
            ml = n
            
        for bl in range(2, ml + 1):
            for bp in range(0, n - bl + 1):
                rl = n - bp - bl
                if rl >= 2:
                    c += computeWays(rl)
                else:
                    c += 1
        
        return c
                
    w = computeWays(l)
    return w
