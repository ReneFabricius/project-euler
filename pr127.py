from functools import reduce, lru_cache
from math import gcd
import primes

primes.initGlobalPrimes(60000)

@lru_cache(maxsize = None)
def rad(n):
    decomp = primes.primeFactDecompPreinitialized(n)
    r = reduce(lambda a,b:a*b, decomp.keys())
    return r
    
def product(L):
    return reduce(lambda a, b: a*b, L)

def getNumber(F, E):
    num = 1
    for k in range(len(F)):
        num *= F[k]**E[k]
    
    return num
    
def problem127():
    AB = []
    ABC = []
    P = primes.primes(60000)
    
    s_0 = 1
    s_1 = 1
    while s_0 < 4:
        while s_0 + s_1 < 7:
            I_0 = []
            for i in range(s_0):
                I_0 += [i]
            while True:
                I_1 = []
                i_a = 0
                
                if s_0 == s_1:
                    i_a = I_0[0] + 1
                
                while len(I_1) < s_1:
                    if i_a not in I_0:
                        I_1 += [i_a]
                    i_a += 1
                if product([P[ind] for ind in (I_0 + I_1)]) >= 60000:
                    m_a = s_0 - 2
                    while m_a > -1:
                        if I_0[m_a + 1] - I_0[m_a] > 1:
                            break
                        m_a -= 1
                    
                    if m_a < 0:
                        break
                    
                    I_0[m_a] += 1
                    for m_i in range(m_a + 1, len(I_0)):
                        I_0[m_i] = I_0[m_a] + m_i - m_a
                    
                    continue
                
                while True:
                    if product([P[ind] for ind in (I_0 + I_1)]) >= 60000:
                        m_a_1 = s_1 - 2
                        t_1 = -1
                        while m_a_1 > -1:
                            if I_1[m_a_1 + 1] - I_1[m_a_1] > 1:
                                for t_1_a in range(I_1[m_a_1] + 1, I_1[m_a_1 + 1]):
                                    if t_1_a not in I_0:
                                        t_1 = t_1_a
                                        break
                                if t_1 > -1:
                                    break
                            m_a_1 -= 1
                        
                        if m_a_1 < 0:
                            break
                        
                        I_1[m_a_1] = t_1
                        for m_i_1 in range(m_a_1 + 1, len(I_1)):
                            t_i_1 = I_1[m_a_1] + m_i_1 - m_a_1
                            while t_i_1 in I_0:
                                t_i_1 += 1
                            I_1[m_i_1] = t_i_1
                            
                        continue
                    
                    # code
                    a = [P[i_0] for i_0 in I_0]
                    b = [P[i_1] for i_1 in I_1]
                    AB += [tuple([a, b])]
                    
                    E_0 = [1]*s_0
                    while True:
                        E_1 = [1]*s_1
                        if product(b) + getNumber(a, E_0) >= 120000:
                            m_e = s_0 - 2
                            while m_e > -1:
                                E_a = [E_0[j] for j in range(m_e)]
                                E_a += [E_0[m_e] + 1]
                                E_a += [1] * (s_0 - 1 - m_e)
                                if product(b) + getNumber(a, E_a) < 120000:
                                    E_0 = E_a
                                    break
                                
                                m_e -= 1
                            if m_e < 0:
                                break
                        
                        while True:
                            if getNumber(a, E_0) + getNumber(b, E_1) >= 120000:
                                m_e_1 = s_1 - 2
                                while m_e_1 > -1:
                                    E_a_1 = [E_1[o] for o in range(m_e_1)]
                                    E_a_1 += [E_1[m_e_1] + 1]
                                    E_a_1 += [1] * (s_1 - 1 - m_e_1)
                                    if getNumber(a, E_0) + getNumber(b, E_a_1) < 120000:
                                        E_1 = E_a_1
                                        break
                                    
                                    m_e_1 -= 1
                                if m_e_1 < 0:
                                    break
                            
                            # code
                            a_f = getNumber(a, E_0)
                            b_f = getNumber(b, E_1)
                            c_p = a_f + b_f
                            rad_ab = product(a + b)
                            if c_p > rad_ab:
                                rad_c = rad(c_p)
                                if rad_c * rad_ab < c_p:
                                    ABC += [tuple([a_f, b_f, c_p])]
                                        
                            
                            
                            E_1[-1] += 1
                        
                        E_0[-1] += 1
                        
                    
                    
                    t_l_1 = I_1[-1] + 1
                    while t_l_1 in I_0:
                        t_l_1 += 1
                    I_1[-1] = t_l_1
                            
                
                I_0[-1] += 1
            
            s_1 += 1
        s_0 += 1
        s_1 = s_0
    
    print("First part done")
    
    a_1 = 1
    for b_1 in range(2, 119999):
        c_1 = a_1 + b_1
        rad_abc = rad(b_1*c_1)
        if rad_abc < c_1:
            ABC += [tuple([a_1, b_1, c_1])]
    
    sum_c = sum([abc[2] for abc in ABC])
    
    return ABC, sum_c
    

def bruteForceBel1000():
    ABC = []
    for a in range(1, 500):
        for b in range(a + 1, 1000 - a):
            if gcd(a, b) == 1:
                c = a + b
                if gcd(a, c) == 1 and gcd(b, c) == 1:
                    rad_abc = rad(a*b*c)
                    if rad_abc < c:
                        ABC += [tuple([a, b, c])]
    
    return ABC
                
                
                
