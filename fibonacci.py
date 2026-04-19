import numpy as np
import numpy.linalg as la

def fibonacciByMatrix(n):
    M = np.array([1, 1, 1, 0], dtype=object).reshape(2, 2)
    return la.matrix_power(M, n - 1)[0,0]

def fibonacciByLoop(n):
    a = 1
    b = 1
    for i in range(n-2):
        a, b = b, a + b
        
    return b
