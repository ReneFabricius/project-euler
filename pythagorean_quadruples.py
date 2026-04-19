from math import gcd, ceil
from itertools import permutations

def sumCombinations(s, n, mp = -1):
	if n == 1:
		yield [s]
		return
	l = s
	if mp != -1 and mp < l:
		l = mp
		
	for a in range(l, ceil(s/n) - 1, -1):
		for rest in sumCombinations(s - a, n - 1, a):
			yield [a] + rest
		

def quadrupletGenerator():
	suma = 0
	while True:
		for comb in sumCombinations(suma, 4):
			if sum(comb) % 2 == 0:
				continue
			m, n, p, q = comb
			mn = gcd(m, n)
			mnp = gcd(mn, p)
			if gcd(mnp, q) == 1:
				
				a = m*m + n*n - p*p - q*q
				b = 2*(m*q + n*p)
				c = 2*(n*q - m*p)
				d = m*m + n*n + p*p + q*q
				yield(tuple(sorted([abs(a), abs(b), abs(c), abs(d)])))
				
				f = True
				if m != p and n != q:
					a = p*p + n*n - m*m - q*q
					b = 2*(p*q + m*n)
					yield(tuple(sorted([abs(a), abs(b), abs(c), abs(d)])))				# m, p
					if p == q == 0 or (m == n and q == 0):
						f = False
						
					if m != n and p != q and n != p and q != 0:
						a = m*m + q*q - p*p - n*n
						# b = m*n + p*q
						yield(tuple(sorted([abs(a), abs(b), abs(c), abs(d)])))			# n, q
						
				if m != n and p != q and q != 0:
					a = m*m + n*n - p*p - q*q
					b = 2*(n*q + m*p)
					c = 2*(m*q - n*p)
					yield(tuple(sorted([abs(a), abs(b), abs(c), abs(d)])))				# m, n
					
				if f and m != q and n != p:
					a = q*q + n*n - p*p - m*m
					b = 2*(m*q + n*p)
					c = 2*(m*n - p*q)
					yield(tuple(sorted([abs(a), abs(b), abs(c), abs(d)])))				# m, q
							
		suma += 1				

def testQuadruples(l):
	Q = []
	for q in quadrupletGenerator():
		if q[3] > l:
			break
		Q += [q]
	
	Q.sort(key = lambda e:e[3])
	return Q

