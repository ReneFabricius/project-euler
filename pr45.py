from math import sqrt

def isPentagonal(n):
    return (sqrt(24*n + 1) + 1) % 6 == 0

def isHexagonal(n):
    return (sqrt(8*n+1) + 1) % 4 == 0

def triangle(n):
    return int(n*(n+1)/2)

def problem45():
    t_n = 286
    while True:
        t = triangle(t_n)
        if isHexagonal(t) and isPentagonal(t):
            return t, t_n
        t_n += 1
