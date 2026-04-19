from math import sqrt
from operator import add
import gmpy2
from gmpy2 import mpfr

gmpy2.get_context().precision=400

def compTime(x):
    m = gmpy2.sqrt(2)*50
    a = (100 - m)/2
    T = (gmpy2.sqrt(2*x[0]*x[0] + a*a + 2*x[0]*a) + gmpy2.sqrt(2*x[5]*x[5] + a*a - 2*x[5]*a)) / 10
    for i in range(1, 6):
        T += gmpy2.sqrt((m/5 - (x[i-1] - x[i]))**2 + (x[i-1] - x[i])**2)/(10 - i)
    
    return T

def compPartialDerVector(x):
    m = gmpy2.sqrt(2)*50
    a = (100 - m)/2
    V = []
    v_0 = (2*x[0] + a)/(10*gmpy2.sqrt(2*x[0]*x[0] + a*a + 2*x[0]*a)) + (2*x[0] - 2*x[1] - m/5)/(9*gmpy2.sqrt((m/5 - x[0] + x[1])**2 + (x[0] - x[1])**2))
    V.append(v_0)
    
    for i in range(1, 5):
        v_i = (m/5 - 2*x[i-1] + 2*x[i])/((10-i)*gmpy2.sqrt((m/5 - x[i-1] + x[i])**2 + (x[i-1] - x[i])**2)) + (2*x[i] - 2*x[i+1] - m/5)/((9 - i)*gmpy2.sqrt((m/5 - x[i] + x[i+1])**2 + (x[i] - x[i+1])**2))
        V.append(v_i)
    
    v_5 = (m/5 - 2*x[4] + 2*x[5])/(5*gmpy2.sqrt((m/5 - x[4] + x[5])**2 + (x[4] - x[5])**2)) + (2*x[5] - a)/(10*gmpy2.sqrt(2*x[5]*x[5] + a*a - 2*x[5]*a))
    V.append(v_5)
    
    return V
    
def vectorLenght(x):
    ss = 0
    for e in x:
        ss += e*e
    return sqrt(ss)

def optimalize(x_0, d):
    X = []
    X.append(tuple(x_0))
    V = []
    V.append(compTime(x_0))
    i = 0
    step = 10
    
    while True:
        der = compPartialDerVector(X[i])
        der_len = vectorLenght(der)
        dire = [-e/der_len*step for e in der]
        x_next = tuple(map(add, X[i], tuple(dire)))
        t_next = compTime(x_next)
        if t_next < V[i]:
            X.append(x_next)
            V.append(t_next)
            if V[i] - t_next < d:
                return X, V 
            i += 1
        else:
            step /= 2
        


