from itertools import combinations
from math import ceil

# Zakomentovana cast kodu je nepouzitelne pomala, ale su v nej veci ktore mozno niekedy pouzijem
'''
def testWays(n):
    W = {}
    def waysToSum(nn):
        nonlocal W
        if nn in W:
            return W[nn]
        
        Wnn = []
        for i in range(1, ceil(nn/2 - 1) + 1):
            j = nn - i
            Wnn += [frozenset([i, j])]
            Wi = waysToSum(i)
            Wj = waysToSum(j)
            for wi in Wi:
                if j not in wi:
                    Wnn += [wi | frozenset([j])]
                for wj in Wj:
                    if not wi & wj:
                        Wnn += [wi | wj]
            
            for wj in Wj:
                if i not in wj:
                    Wnn += [wj | frozenset([i])]
        
        Wnn = list(frozenset(Wnn))
        W[nn] = Wnn
        return Wnn
    
    return waysToSum(n)


def problem103(n):
    W = {}
    def waysToSum(nn):
        nonlocal W
        if nn in W:
            return W[nn]
        
        Wnn = []
        for i in range(1, ceil(nn/2 - 1) + 1):
            j = nn - i
            Wnn += [frozenset([i, j])]
            Wi = waysToSum(i)
            Wj = waysToSum(j)
            for wi in Wi:
                if j not in wi:
                    Wnn += [wi | frozenset([j])]
                for wj in Wj:
                    if not wi & wj:
                        Wnn += [wi | wj]
            
            for wj in Wj:
                if i not in wj:
                    Wnn += [wj | frozenset([i])]
        
        Wnn = list(frozenset(Wnn))
        W[nn] = Wnn
        return Wnn
    
    
    D = [1] * n * 100      # -1 - contains, 0 - cannot contain, 1 - can contain
    D[0] = 0
    mS = set([1, 2])
    mSs = 3
    
    def findCandidates(aS, dl, NL):
        mx = int((mSs - sum(aS))/(dl - len(aS)) + (dl - len(aS) - 1)/2)
        if len(aS) >= 2:
            mst = mx
            SL = sorted(list(aS))
            for k in range(2, (len(aS) + 2)//2 + 1):
                amst = sum(SL[:k]) - sum(SL[-1:1-k:-1]) - 1
                if amst < mst:
                    mst = amst
            
            if mx > mst:
                mx = mst
        
        
        aD = [0] + [1]*mx
        aSL = list(aS)
        for am in aSL:
            if am <= mx:
                aD[am] = -1
        for nc in NL:
            if nc <= mx:
                aD[nc] = 0
        for cl in range(2, len(aS) + 1):
            for cmb in combinations(aS, cl):
                if sum(cmb) <= mx:
                    aD[sum(cmb)] = 0
                for w in waysToSum(sum(cmb)):
                    dif = w - (aS - set(cmb))
                    if len(dif) == 1:
                        ntd = list(dif)[0]
                        if ntd <= mx:
                            aD[ntd] = 0
        
        return aD
    
    def findNext(aS, dl, NL):
        nonlocal mS
        nonlocal mSs
        if len(aS) == dl:
            if sum(aS) < mSs:
                mS = aS
                mSs = sum(aS)
            return
        
        if sum(aS) >= mSs:
            return
            
        aD = findCandidates(aS, dl, NL)
        
        for ci in range(1, len(aD)):
            if aD[ci] == 1:
                NL += [ci]
                findNext(set(aS) | set([ci]), dl, NL[:])
    
    for sl in range(3, n + 1):
        mSL = sorted(list(mS))
        me = mSL[len(mSL)//2]
        mS = set([me] + [x + me for x in mSL])
        mSs = sum(mS)
        findNext(set(), sl, [])
    
    return mS

'''


def problem103Checking(n):
    CTl = [[], [], [], []]
    
    def findControllableFor(n):
        d = range(n)
        S = set(d)
        CT = []
        for cl in range(2, n//2 + 1):
            for fc in combinations(d, cl):
                fcl = sorted(list(fc))
                for sc in combinations(S - set(fc), cl):
                    scl = sorted(list(sc))
                    if fcl[0] > scl[0]:
                        continue
                    
                    for i in range(1, cl):
                        if fcl[i] > scl[i]:
                            CT += [(fcl, scl)]
                            break
        
        return CT
    
    for sl in range(4, n + 1):
        CTl += [findControllableFor(sl)]
    
    def isValidSet(S):
        SL = sorted(list(S))
        for sp in CTl[len(S)]:
            fss = sum([SL[fsi] for fsi in sp[0]])
            sss = sum([SL[ssi] for ssi in sp[1]])
            if fss == sss:
                return False
        
        return True
    
    mS = set([1, 2])
    mSs = 3
    
    def findNext(aS, dl):
        nonlocal mS
        nonlocal mSs
        if len(aS) == dl:
            if sum(aS) < mSs:
                mS = aS
                mSs = sum(aS)
            return
        
        if sum(aS) >= mSs:
            return
            
        mx = int((mSs - sum(aS))/(dl - len(aS)) + (dl - len(aS) - 1)/2) - 1
        SL = sorted(list(aS))
        if len(aS) >= 2:
            mst = mx
            for k in range(2, (len(aS) + 2)//2 + 1):
                amst = sum(SL[:k]) - sum(SL[-1:1-k:-1]) - 1
                if amst < mst:
                    mst = amst
            
            if mx > mst:
                mx = mst
        if not SL:
            SL = [1]
            
        for ne in range(SL[-1] + 1, mx + 1):
            if ne + sum(aS) >= mSs:
                break
            if ne not in aS and isValidSet(aS | set([ne])):
                findNext(set(aS) | set([ne]), dl)
        
    
    for sl in range(3, n + 1):
        mSL = sorted(list(mS))
        me = mSL[len(mSL)//2]
        mS = set([me] + [x + me for x in mSL])
        mSs = sum(mS)
        findNext(set(), sl)
    
    return mS
