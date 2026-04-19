from fractions import Fraction
from math import log

def problem57(l):
    c = 0
    f = Fraction(3, 2)
    for i in range(l - 1):
        f = Fraction(2*f.denominator + f.numerator, f.denominator + f.numerator)
        if int(log(f.numerator, 10)) > int(log(f.denominator, 10)):
            c += 1
    
    return c
