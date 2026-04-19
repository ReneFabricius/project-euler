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
        
        for bl in range(3, n + 1):
            for bp in range(0, n - bl + 1):
                rl = n - bp - bl - 1
                if rl >= 3:
                    c += computeWays(n - bp - bl - 1)
                else:
                    c += 1
        
        return c
                
    w = computeWays(l)
    return w
