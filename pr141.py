from math import sqrt, gcd
from diophantine_equation import quadraticDiophantineEq

def dqrforn(n):
	for d in range(1, n):
		q = n//d
		r = n % d
		if r != 0:
			if q/d == d/r:
				return d, q, r
			elif d/q == q/r:
				return d, q, r
			elif q/d == d/r:
				return d, q, r
				
def dqrfornsq(l):
	S = []
	NI = []
	for i in range(2, l):
		n = i*i
		for d in range(1, n):
			q = n//d
			r = n % d
			if r != 0:
				if q/d == d/r:
					S += [tuple([d, q, r, n])]
					if q%d != 0:
						NI += [tuple([d, q, r, n])]
				elif d/q == q/r:
					S += [tuple([d, q, r, n])]
					if d%q != 0:
						NI += [tuple([d, q, r, n])]

	
	return S, NI
	
def solFinder(m, n):
	f, s = quadraticDiophantineEq(n**3, 0, -m**3, 0, -n**3, 0)
	if s is None:
		return None
	
	s = list(set(s[0]))
	s.sort(key = lambda e: abs(e[0]) + abs(e[1]))
	CS = []
	for sol in s:
		CS += [tuple([sol[1]*m*m/n/n, sol[1]*m/n, sol[1], sol[0]])]
	
	return CS
	
def problem141(l):
	S = []
	
	for m in range(2, int(l**(1/3)) + 1):
		m3 = m**3
		nl = int((-m3 + sqrt(m3**2 + 4*l))/2)
		if m - 1 < nl:
			nl = m - 1
		for n in range(1, nl + 1):
			if gcd(m, n) == 1:
				xl = int((-n*n + sqrt(n**4+4*m3*n*l))/(2*m3*n))
				for x in range(1, xl + 1):
					ps = n*(x**2*m3 + x*n)
					s = sqrt(ps)
					if s.is_integer():
						S += [tuple([x*n**2, x*m*n, x*m**2, ps])]
	
	S = set(S)
	sm = 0
	for s in S:
		sm += s[3]
		
	return S, sm
