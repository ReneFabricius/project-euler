from math import sqrt
from diophantine_equation import quadraticDiophantineEq, ReccurentSolution

def testSq(n):
	for i in range(n):
		g_n = (5-7*sqrt(5))/10*((1-sqrt(5))/2)**i + (5+7*sqrt(5))/10*((1+sqrt(5))/2)**i
		print(g_n)

def testA_G(m, n):
	return (n*m+3*m*m)/(n*n-m*n-m*m)
	
def findBasicSols():
	f, s = quadraticDiophantineEq(5, 0, -1, 14, 0, 1)
	LB = set(s[0])
	R_sols = set()
	bsols = set([tuple([0,1]), tuple([0, -1]), tuple([2,7]), tuple([2,-7]), tuple([-3,2]), tuple([-3,-2]), tuple([5,-14]), tuple([-4,5]), tuple([-10,19]), tuple([21,-50])])
	reccurS = [[-9, -4, -14, -20, -9, -28], [161, 72, 224, 360, 161, 504]]
	R = []
	for bsol in bsols:
		for reccur in reccurS:
			R += [ReccurentSolution(*bsol, *reccur)]
	
	
	for r in R:
		for n in range(len(LB)):
			R_sols.add(r.nextSol())

	
	
	return LB - R_sols, LB, R_sols

def problem140():
	f, s = quadraticDiophantineEq(5, 0, -1, 14, 0, 1)
	GN = set()
	for ps in s[0]:
		if ps[0] > 0:
			GN.add(ps[0])
	
	return GN
