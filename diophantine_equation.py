from enum import Enum
from math import ceil, sqrt, copysign
from gmpy2 import is_square, isqrt, gcd
from continued_fractions import nthConvergentSQrootPrecomputed, continuedFracSQroot, periodicContinuedFraction, nConvergentsQuadraticSurdPrecomputed
from euclidean_alg import extEuclid
from primes import findDivisors, primeFactDecomp

def pellEqu(D, n, maxPer = 0):
    "Najde prvych n rieseni Pellovej rovnice x**2 + D*y**2 = 1, v pripade, ze perioda retazoveho zlomku prekroci maxPer, zastavi vypocet"
    F = continuedFracSQroot(D, maxPer)
    if F == 0:
        return 0
        
    if len(F) == 1:
        return []
        
    r = len(F) - 2
    x1 = 0
    y1 = 0
    c = 0
    if r % 2 == 1:
        C = nthConvergentSQrootPrecomputed(F, r)
    else:
        C = nthConvergentSQrootPrecomputed(F, 2*r + 1)
    
    x1 = C.numerator
    y1 = C.denominator
    
    if n == 1:
        return [(x1, y1)]
    
    
    S = [(x1, y1)]
    
    for k in range(2, n + 1):
        S += [(S[0][0]*S[k-2][0] + D*S[0][1]*S[k-2][1], S[0][0]*S[k-2][1] + S[0][1]*S[k-2][0])]
    
    return S
    

class ParametricSolution:
    def __init__(self, x0, y0, xq, xq2, yq, yq2):
        "x0 , y0 - pociatocne riesenie, xq, yq - koeficienty pri x, y, xq2, yq2 - koeficienty pri x**2, y**2"
        self.x0 = int(x0)
        self.y0 = int(y0)
        self.xq = int(xq)
        self.xq2 = int(xq2)
        self.yq = int(yq)
        self.yq2 = int(yq2)
        
    def getSol(self, t):
        return (self.x0 + t*self.xq + t*t*self.xq2, self.y0 + t*self.yq + t*t*self.yq2)
    
    def getCoefs(self):
        return (self.xq, self.xq2, self.yq, self.yq2)

class ReccurentSolution:
    def __init__(self, X0, Y0, P, Q, K, R, S, L):
        "Rekurencia Xn+1 = P*Xn + Q*Yn + K, Yn+1 = R*Xn + S*Yn + L"
        self.Xn = int(X0)
        self.Yn = int(Y0)
        self.P = int(P)
        self.Q = int(Q)
        self.K = int(K)
        self.R = int(R)
        self.S = int(S)
        self.L = int(L)
    
    def getCoefs(self):
        return (self.P, self.Q, self.K, self.R, self.S, self.L)
    
    def nextSol(self):
        rX, rY = self.Xn, self.Yn
        self.Xn, self.Yn = self.P*self.Xn + self.Q*self.Yn + self.K, self.R*self.Xn + self.S*self.Yn + self.L
        return rX, rY

class SolutionFlag(Enum):
    NO_SOLUTION                             = 1
    LIST_SOLUTIONS                          = 2
    NONE_IN_SOL                             = 4
    PARAMETRIC_SOL                          = 8
    PARAMETRIC_SOL_LIST                     = 16
    LIST_OF_SOLS_AND_LIST_OF_RECCUR_COEFS   = 32
    ONE_SOL_AND_LIST_OF_RECCUR_COEFS        = 64
    
def linearDiophantineEq(D, E, F):
    if D == E == 0:
            if F == 0:
                return SolutionFlag.LIST_SOLUTIONS.value | SolutionFlag.NONE_IN_SOL.value, [(None, None)]               # All x, y pairs are solution
            else:
                return SolutionFlag.NO_SOLUTION, None                                                       # No solution
        
    if D == 0:
        if F % E == 0:
            return SolutionFlag.LIST_SOLUTIONS.value | SolutionFlag.NONE_IN_SOL.value, [(None, -F//E)]
        return SolutionFlag.NO_SOLUTION, None                                                               # No solution
    
    if E == 0:
        if F % D == 0:
            return SolutionFlag.LIST_SOLUTIONS.value | SolutionFlag.NONE_IN_SOL.value, [(-F//D, None)]
        return SolutionFlag.NO_SOLUTION, None                                                               # No solution
    
    g, dc, ec = extEuclid(D, E)
    if F % g != 0:
        return SolutionFlag.NO_SOLUTION, None
    
    d, e, f = D // g, E // g, F // g
    return SolutionFlag.PARAMETRIC_SOL, ParametricSolution(-f*dc, -f*ec, e, 0, -d, 0)

def findSolAmongConvergents(A, B, C, F, nd, per_q):
    S = []
    # Riesenie medzi konvergentami korenov A*t*t + B*t + C = 0
    CF1, pi1, neg1 = periodicContinuedFraction(-B, B*B - 4*A*C, 2*A)
    pl1 = len(CF1) - pi1
    CVG1 = []
    if pl1 % 2 == 0:
        CVG1 = nConvergentsQuadraticSurdPrecomputed(CF1, pi1, pi1 + per_q*pl1, neg1)
    else:
        CVG1 = nConvergentsQuadraticSurdPrecomputed(CF1, pi1, pi1 + 2*per_q*pl1, neg1)
    
    CF2, pi2, neg2 = periodicContinuedFraction(B, B*B - 4*A*C, -2*A)
    pl2 = len(CF2) - pi2
    CVG2 = []
    if pl2 % 2 == 0:
        CVG2 = nConvergentsQuadraticSurdPrecomputed(CF2, pi2, pi2 + per_q*pl2, neg2)
    else:
        CVG2 = nConvergentsQuadraticSurdPrecomputed(CF2, pi2, pi2 + 2*per_q*pl2, neg2)
    
    CVG = CVG1 + CVG2
    
    for cvg in CVG:
        # print(str(cvg.numerator) + ", " + str(cvg.denominator) + ", " + str(A*cvg.numerator**2 + B*cvg.numerator*cvg.denominator + C*cvg.denominator**2 + F))
        if A*cvg.numerator**2 + B*cvg.numerator*cvg.denominator + C*cvg.denominator**2 + F == 0:
            S += [(int(cvg.numerator), int(cvg.denominator))]
            if not nd:
                S += [(int(-cvg.numerator), int(-cvg.denominator))]
    
    return S

def homogenousHyperbolicDiophantineEqFewSols(A, B, C, F, nd, per_q):
    "Najde niekolko zakladnych rieseni homogennej hyperbolickej rovnice A*x**2 + B*x*y + C*y**2 + F = 0, nd = True - nevracat riesenia prenasobene -1, per_q - qocient pre pocet prechadzanych period"
    if F == 0:
        if is_square(B*B - 4*A*C):
            f1, s1 = linearDiophantineEq(2*A, B + isqrt(B*B - 4*A*C), 0)
            f2, s2 = linearDiophantineEq(2*A, B * isqrt(B*B - 4*A*C), 0)
            if s1 == s2 == None:
                return SolutionFlag.NO_SOLUTION, None
            if s1 != None and s2 != None:
                return SolutionFlag.PARAMETRIC_SOL_LIST, [s1, s2]
            if s1 != None:
                return SolutionFlag.PARAMETRIC_SOL, s1
            return SolutionFlag.PARAMETRIC_SOL, s2
        return SolutionFlag.LIST_SOLUTIONS, [(0, 0)]
    
    if is_square(B*B - 4*A*C):
        k = isqrt(B*B - 4*A*C)
        DV = findDivisors(abs(4*A*F))
        s = []
        for dv in DV:
            if (dv + 4*A*F // dv) % (2*k) == 0:
                yp = (dv + 4*A*F // dv) // (2*k)
                if (dv - (B + k)*yp) % (2*A) == 0:
                    s += [((dv - (B + k)*yp) // (2*A), yp)]
            if not nd:
                if (-dv + 4*A*F // (-dv)) % (2*k) == 0:
                    ym = (-dv + 4*A*F // (-dv)) // (2*k)
                    if (-dv - (B + k)*ym) % (2*A) == 0:
                        s += [((-dv - (B + k)*ym) // (2*A), ym)]
        
        if s:
            return SolutionFlag.LIST_SOLUTIONS, s
        return SolutionFlag.NO_SOLUTION, None
    
    g = gcd(A, gcd(B, C))
    if F % g != 0:
        return SolutionFlag.NO_SOLUTION, None
    
    A, B, C, F = A//g, B//g, C//g, F//g
    
    # find squares in F
    PD = primeFactDecomp(abs(F))
    sqn = 1
    for pd in PD:
        if PD[pd] > 1:
            sqn *= pd**(PD[pd]//2)
    
    Dsqn = findDivisors(sqn)    # Square roots of squares in F
    Sl = []
    Slpn = []
    for dv in Dsqn:
        Sldv = []
        dF = F // (dv*dv)
        
        if 4*dF*dF < B*B - 4*A*C:
            Sldv = findSolAmongConvergents(A, B, C, dF, nd, per_q)
        else:                                       # 4*dF**2 >= B*B - 4*A*C
            if gcd(A, gcd(B, dF)) == 1:
                S = []
                for ps in range(abs(dF)):
                    if (A*ps*ps + B*ps + C) % dF == 0:
                        S += [ps]
                for s in S:
                    Sldvyzs = findSolAmongConvergents(-(A*s*s + B*s + C)//dF, 2*A*s + B, -A*dF, - 1, nd, per_q)
                    for sldvyzs in Sldvyzs:
                        Sldv += [(s*sldvyzs[0] - dF*sldvyzs[1], sldvyzs[0])]
            
            elif gcd(B, gcd(C, dF)) == 1:
                S = []
                for ps in range(abs(dF)):
                    if (C*ps*ps + B*ps + A) % dF == 0:
                        S += [ps]
                
                for s in S:
                    Sldvxzs = findSolAmongConvergents(-(C*s*s + B*s + A)//dF, 2*C*s + B, -C*dF, -1, nd, per_q)
                    for sldvxzs in Sldvxzs:
                        Sldv += [(sldvxzs[0], s*sldvxzs[0] - sldvxzs[1]*dF)]
            
            else:               # gcd(A, B, dF) > 1 && gcd(B, C, dF) > 1
                i = 0
                m = 0
                fin = False
                for i_ in range(abs(dF)):
                    for m_ in range(i):
                        if gcd(i_, m_) == 1:
                            k = A*i_*i_ + B*i_*m_ + C*m_*m_
                            if gcd(k, dF) == 1:
                                i = i_
                                m = m_
                                fin = True
                                break
                    if fin:
                        break
                
                if i != 0 and m != 0:
                    lf, lS = linearDiophantineEq(i, -m, -1)
                    if lf == SolutionFlag.PARAMETRIC_SOL:
                        j, n = lS.getSol(0)
                        a = A*i*i + B*i*m + C*m*m
                        b = 2*A*i*j + B*i*n + B*j*m + 2*C*m*m
                        c = A*j*j + B*j*n + C*n*n
                        hf, hS = homogenousHyperbolicDiophantineEqFewSols(a, b, c, dF, nd, per_q)
                        if hS:
                            for hs in hS:
                                Sldv += [(i*hs[0] + j*hs[1], m*hs[0] + n*hs[1])]
        
        for sldv in Sldv:
            Sl +=[(int(sldv[0]*dv), int(sldv[1]*dv))]
        
        
    
    if Sl:
        return SolutionFlag.LIST_SOLUTIONS, Sl
    
    return SolutionFlag.NO_SOLUTION, None
    
    
        
def quadraticDiophantineEq(A, B, C, D, E, F):
    "Vyriesi diofanticku rovnicu Ax**2 + Bxy + Cy**2 + Dx + Ey + F = 0, navratova hodnota je usporiadana dvojica f, s, kde f je flaga poskytujuca informacie o druhu riesenia a s je riesenie"
    # Hodnoty pre f:
    # 1 - nema riesenie, s == None
    # 2 - list rieseni - s je list usporiadanych dvojic
    # 4 - specialna hodnota None v usporiadanych dvojiciach - tato premenna moze nadobudat lubovolnu hodnotu
    # 8 - parametricke riesenie, s je objekt triedy ParametricSolution s metodou getSol ktora vracia usporiadane dvojice rieseni na zaklade poskytnuteho parametra a metodou getCoefs ktora vracia koeficienty
    # 16 - list parametrickych rieseni
    # 32 - list niekolkych rieseni a list koeficientov (P, Q, R, S) pre rekurencie Xn+1 = P Xn + Q Yn, Yn+1 = R Xn + S Yn
    
    
    if A == B == C == 0:                            # Linear case Dx + Ey + F = 0
        return linearDiophantineEq(D, E, F)
    
    
    
    if A == C == 0:                                 # Simple hyperbolic case Bxy + Dx + Ey + F = 0
        if D*E - B*F == 0:
            if E % B != 0 and D % B != 0:
                return SolutionFlag.NO_SOLUTION, None
            s = []
            if E % B == 0:
                s += [(-E // B, None)]
            if D % B == 0:
                s += [(None, -D // B)]
            
            return SolutionFlag.LIST_SOLUTIONS | SolutionFlag.NONE_IN_SOL, s
        
        # D*E - B*F != 0
        DV = findDivisors(D*E - B*F)
        s = []
        for dv in DV:
            if (dv - E) % B == 0 and ((D*E - B*F) // dv - D) % B == 0:
                s += [((dv - E) // B, ((D*E - B*F) // dv - D) // B)]
            if (-dv - E) % B == 0 and ((D*E - B*F) // (-dv) - D) % B == 0:
                s += [((-dv - E) // B, ((D*E - B*F) // (-dv) - D) // B)]
        
        if s:
            return SolutionFlag.LIST_SOLUTIONS, s
        return SolutionFlag.NO_SOLUTION, None
    
    
    
    if B*B - 4*A*C < 0:                             # Elliptical case
        det = 4*C*(D*(C*D - B*E) + A*E*E + F*(B*B - 4*A*C))
        if det < 0:
            return SolutionFlag.NO_SOLUTION, None
        
        s = []
        pxs = ceil((2*C*D - B*E + sqrt(det)) / (B*B - 4*A*C))
        pxe = int((2*C*D - B*E - sqrt(det)) / (B*B - 4*A*C))
        for px in range(pxs, pxe + 1):
            dety = (B*px + E) ** 2 - 4*C*(A*px*px + D*px + F)
            if is_square(dety):
                if (-(B*px + E) + isqrt(dety)) % (2*C) == 0:
                    s += [(px, int((-(B*px + E) + isqrt(dety)) // (2*C)))]
                if (-(B*px + E) - isqrt(dety)) % (2*C) == 0:
                    s += [(px, int((-(B*px + E) - isqrt(dety)) // (2*C)))]
        
        if s:
            return SolutionFlag.LIST_SOLUTIONS, s
        return SolutionFlag.NO_SOLUTION, None
    
    
    
    if B*B - 4*A*C == 0:                            # Parabolic case
        g = int(copysign(gcd(A, C), A))
        a, b, c = A //g, B //g, C // g
        sqr_a = isqrt(a)
        sqr_c = int(copysign(isqrt(c), B / A))
        u_limiter = sqr_c*D - sqr_a*E
        if u_limiter == 0:
            detu = D*D - 4*a*g*F
            if not is_square(detu):
                return SolutionFlag.NO_SOLUTION, None
            s1 = None
            s2 = None
            if (-D + isqrt(detu)) % (2*sqr_a*g) == 0:
                u1 = (-D + isqrt(detu)) // (2*sqr_a*g)
                f1, s1 = linearDiophantineEq(sqr_a, sqr_c, -u1)
            if (-D - isqrt(detu)) % (2*sqr_a*g) == 0:
                u2 = (-D - isqrt(detu)) // (2*sqr_a*g)
                f2, s2 = linearDiophantineEq(sqr_a, sqr_c, -u2)
            
            if s1 == s2 == None:
                return SolutionFlag.NO_SOLUTION, None
            if s1 != None and s2 != None:
                return SolutionFlag.PARAMETRIC_SOL_LIST, [s1, s2]
            if s1 != None:
                return SolutionFlag.PARAMETRIC_SOL, s1
            return SolutionFlag.PARAMETRIC_SOL, s2
            
        # sqr_c*D - sqr_a*E != 0
        U = []
        for pu in range(0, abs(u_limiter)):
            if (sqr_a*g*pu*pu + D*pu + sqr_a*F) % u_limiter == 0:
                U += [pu]
        if not U:
            return SolutionFlag.NO_SOLUTION, None
        
        s = []
        for u in U:
            s += [ParametricSolution(-(sqr_c*g*u*u + E*u + sqr_c*F) // u_limiter, (sqr_a*g*u*u + D*u + sqr_a*F) // u_limiter, -(E + 2*sqr_c*g*u), sqr_c*g*(-u_limiter), (D + 2*sqr_a*g*u), sqr_a*g*u_limiter)]
        
        return SolutionFlag.PARAMETRIC_SOL_LIST, s
    
    if B*B - 4*A*C > 0:                             # Hyperbolic case
        if D == E == 0:
            ff, fS = homogenousHyperbolicDiophantineEqFewSols(A, B, C, F, False, 1)
            if not fS:
                return SolutionFlag.NO_SOLUTION, None
                
            fr, rS = homogenousHyperbolicDiophantineEqFewSols(1, B, A*C, -1, True, 1)
            
            rC = []
            for rs in rS:
                if rs[0] != 0 and rs[1] != 0:
                    rC += [(rs[0], -C*rs[1], 0, A*rs[1], rs[0] + B*rs[1], 0)]
            
            if rC:
                return SolutionFlag.LIST_OF_SOLS_AND_LIST_OF_RECCUR_COEFS, (fS, rC)
            
            return SolutionFlag.LIST_SOLUTIONS, fS
        
        # general hyperbolic case
        ms = findOneSolGeneralHyperbolic(A, B, C, D, E, F, True)
        if not ms:
            return SolutionFlag.NO_SOLUTION, None
        
        Rc = findReccurenceCoefsGeneralHyperbolic(A, B, C, D, E, F)
        
        return SolutionFlag.LIST_OF_SOLS_AND_LIST_OF_RECCUR_COEFS, (ms, Rc)
                
        
def findOneSolGeneralHyperbolic(A, B, C, D, E, F, m):
    g = gcd(4*A*C - B*B, 2*A*E - B*D)
    a = (4*A*C - B*B) // g
    c = g
    if (4*A*(4*A*C*F-A*E*E - B*B*F + B*D*E -C*D*D)) % g != 0:
        print(str(g) + " does not divide " + str(4*A*C*F-A*E*E - B*B*F + B*D*E -C*D*D))
    f = (4*A*(4*A*C*F-A*E*E - B*B*F + B*D*E -C*D*D)) // g
    hf, hS = quadraticDiophantineEq(a, 0, c, 0, 0, f)
    
    
    if hf == SolutionFlag.LIST_OF_SOLS_AND_LIST_OF_RECCUR_COEFS:
        R = []
        for rc in hS[1]:
            for hs in hS[0]:
                R += [ReccurentSolution(*hs, *rc)]
        SS = []
        for _ in range(50):
            for r in R:
                x1, y1 = r.nextSol()
                if (y1*g - 2*A*E + B*D) % (4*A*C - B*B) == 0:
                    py = (y1*g - 2*A*E + B*D) // (4*A*C - B*B)
                    if (x1 - B*py - D) % (2*A) == 0:
                        px = (x1 - B*py - D) // (2*A)
                        SS += [(px, py)]
        
        ms = None
        mss = 10**100
        for ss in SS:
            if abs(ss[0]) + abs(ss[1]) < mss:
                mss = abs(ss[0]) + abs(ss[1])
                ms = ss
        if not m:
            return ms
        return SS
        

def tryComputeKL(A, B, C, D, E, F, r, s):
    P = r
    Q = -C*s
    R = A*s
    S = r + B*s
    if (C*D*(P + S - 2) + E*(B - B*r - 2*A*C*s)) % (4*A*C - B*B) == 0:
        K = (C*D*(P + S - 2) + E*(B - B*r - 2*A*C*s)) // (4*A*C - B*B)
        if (D*(B - B*r - 2*A*C*s) + A*E*(P + S - 2)) % (4*A*C - B*B) == 0:
            L = (D*(B - B*r - 2*A*C*s) + A*E*(P + S - 2)) // (4*A*C - B*B) + D*s
            return [(P, Q, K, R, S, L)]

def findReccurenceCoefsGeneralHyperbolic(A, B, C, D, E, F):
    rf, rS = homogenousHyperbolicDiophantineEqFewSols(1, B, A*C, -1, True, 2)
    Rc = []
    for rs in rS:
        r = rs[0]
        s = rs[1]
        KL = tryComputeKL(A, B, C, D, E, F, r, s)
        if KL:
            Rc += KL
            continue
        
        rm = -r
        sm = -s
        KL = tryComputeKL(A, B, C, D, E, F, rm, sm)
        if KL:
            Rc += KL
            continue
        
        r1 = r*r - A*C*s*s
        s1 = 2*r*s + B*s*s
        KL = tryComputeKL(A, B, C, D, E, F, r1, s1)
        if KL:
            Rc += KL
    
    return Rc

def testGeneralRecc(A, B, C, D, E, F):
    SS = findOneSolGeneralHyperbolic(A, B, C, D, E, F, True)
    Rc = findReccurenceCoefsGeneralHyperbolic(A, B, C, D, E, F)
    Sr = set()
    for rec in Rc:
        P, Q, K, R, S, L = rec
        for ss in SS:
            X, Y = ss
            Xnu = Q*(Y - L) - S*(X - K)
            de = Q*R - S*P
            Ynu = R*(X - K) - P*(Y - L)
            while Xnu % de == Ynu % de == 0 and abs(Xnu//de) < abs(X) and abs(Ynu//de) < abs(Y):
                X, Y = Xnu//de, Ynu//de
                Xnu = Q*(Y - L) - S*(X - K)
                Ynu = R*(X - K) - P*(Y - L)
                print((X, Y))
            Sr.add(str(X) + ", " + str(Y))
    
    return Sr
    
    
    RecSols = []
    for rc in Rc:
        RecSols += [ReccurentSolution(*ms, *rc)]
    while SS:
        for recSol in RecSols:
            X, Y = recSol.nextSol()
            if (X, Y) in SS:
                SS.remove((X, Y))
                print(len(SS))
    
    return True
    
