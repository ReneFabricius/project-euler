class MyCacher:
    D = {}
    def __init__(self, func):
        self.func = func
        
    def __call__(self, m, n):
        if (m, n) in self.D:
            return self.D[(m, n)]
        res = self.func(m, n)
        self.D[(m, n)] = res
        return res
        

def F(m, l):
    @MyCacher
    def computeWays(b, n):
        c = 1
        
        for bl in range(b, n + 1):
            for bp in range(0, n - bl + 1):
                rl = n - bp - bl - 1
                if rl >= b:
                    c += computeWays(b, rl)
                else:
                    c += 1
        
        return c
                
    w = computeWays(m, l)
    return w
