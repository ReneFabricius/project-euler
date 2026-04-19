def difSumoSSoSum(n):
    "Najde rozdiel suctu stvorcov po n vratane a stvorca suctu po n vratane"
    sSq = 0
    sqS = 0
    for i in range(1, n + 1):
        sSq += i * i
        sqS += i
    sqS *= sqS
    return sqS - sSq
    
    
    
