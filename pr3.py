from math import sqrt
from primes import primeFactDecomp

def largestPFact(n):
	D = primeFactDecomp(n)
			
	return D[-1]
