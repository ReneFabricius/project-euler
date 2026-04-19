from math import sqrt
from numpy import sign
from diophantine_equation import ReccurentSolution, SolutionFlag, quadraticDiophantineEq

def problem137(l):
	r_1 = ReccurentSolution(0, 1, -9, -4, -2, -20, -9, -4)
	r_2 = ReccurentSolution(0, 1, 161, 72, 32, 360, 161, 72)
	r_3 = ReccurentSolution(0, 1, -9, 4, -2, 20, -9, 4)
	r_4 = ReccurentSolution(0, 1, 161, -72, 32, -360, 161, -72)
	r_5 = ReccurentSolution(0, -1, -9, -4, -2, -20, -9, -4)
	r_6 = ReccurentSolution(0, -1, 161, 72, 32, 360, 161, 72)
	r_7 = ReccurentSolution(0, -1, -9, 4, -2, 20, -9, 4)
	r_8 = ReccurentSolution(0, -1, 161, -72, 32, -360, 161, -72)
	r_9 = ReccurentSolution(-1, 2, -9, -4, -2, -20, -9, -4)
	r_10 = ReccurentSolution(-1, 2, 161, 72, 32, 360, 161, 72)
	r_11 = ReccurentSolution(-1, 2, -9, 4, -2, 20, -9, 4)
	r_12 = ReccurentSolution(-1, 2, 161, -72, 32, -360, 161, -72)
	r_13 = ReccurentSolution(-1, -2, -9, -4, -2, -20, -9, -4)
	r_14 = ReccurentSolution(-1, -2, 161, 72, 32, 360, 161, 72)
	r_15 = ReccurentSolution(-1, -2, -9, 4, -2, 20, -9, 4)
	r_16 = ReccurentSolution(-1, -2, 161, -72, 32, -360, 161, -72)
	L = []
	R = [r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8, r_9, r_10, r_11, r_12, r_13, r_14, r_15, r_16]
	RS = {}
	min_k = 0
	while len(L) < l:
		for r in R:
			k, s = r.nextSol()
			if k >= 0 and k not in RS:
				RS[k] = s
			
			while abs(k) < min_k:
				k, s = r.nextSol()
				if k >= 0 and k not in RS:
					RS[k] = s
		
		min_k = min(RS)
		
		LinS = []
		f, sol = quadraticDiophantineEq(0, 0, 0, abs(RS[min_k]) - min_k - 1, 2*min_k, 0)
		LinS += [tuple([f, sol])]
		f, sol = quadraticDiophantineEq(0, 0, 0, -abs(RS[min_k]) - min_k - 1, 2*min_k, 0)
		LinS += [tuple([f, sol])]
		
		RS.pop(min_k)
		
		for linS in LinS:
			if linS[0] == SolutionFlag.PARAMETRIC_SOL:
				if sign(linS[1].getCoefs()[0]) == sign(linS[1].getCoefs()[2]) and abs(linS[1].getCoefs()[0]) < abs(linS[1].getCoefs()[2]):
					L += [tuple([min_k, abs(linS[1].getCoefs()[0]), abs(linS[1].getCoefs()[2])])]
		
		if len(RS) == 0:
			min_k = 0
		else:
			min_k = min(RS)
		
	return L
		
def testSols(l):
	BFS = set()
	for s in range(1, l):
		k_1 = (-1+sqrt(5*s*s-4))/5
		k_2 = (-1-sqrt(5*s*s-4))/5
		if k_1.is_integer():
			BFS.add(tuple([k_1, s]))
		if k_2.is_integer():
			BFS.add(tuple([k_2, s]))
	
	r_1 = ReccurentSolution(0, 1, -9, -4, -2, -20, -9, -4)
	r_2 = ReccurentSolution(0, 1, 161, 72, 32, 360, 161, 72)
	r_3 = ReccurentSolution(0, 1, -9, 4, -2, 20, -9, 4)
	r_4 = ReccurentSolution(0, 1, 161, -72, 32, -360, 161, -72)
	r_5 = ReccurentSolution(0, -1, -9, -4, -2, -20, -9, -4)
	r_6 = ReccurentSolution(0, -1, 161, 72, 32, 360, 161, 72)
	r_7 = ReccurentSolution(0, -1, -9, 4, -2, 20, -9, 4)
	r_8 = ReccurentSolution(0, -1, 161, -72, 32, -360, 161, -72)
	S = set()
	R = [r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8]
	for i in range(len(BFS)):
		for r in R:
			S.add(r.nextSol())
	
	for bfs in BFS:
		if bfs not in S:
			print(bfs)
	
	return BFS, S

def wolframSols(l):
	WS = set()
	for n in range(l):
		s = (1/5 *(-5 *(9 - 4 *sqrt(5))**(2 *n) - 2 *sqrt(5) *(9 - 4 *sqrt(5))**(2 *n) - 5 *(9 + 4 *sqrt(5))**(2 *n) + 2 *sqrt(5) *(9 + 4* sqrt(5))**(2 *n)))
		k = 1/20 *(-4 *(2 *(9 - 4 *sqrt(5))**(2 *n) + sqrt(5) *(9 - 4 *sqrt(5))**(2 *n) + 2 *(9 + 4 *sqrt(5))**(2 *n) - sqrt(5) *(9 + 4 *sqrt(5))**(2 *n)) - 4) 
		WS.add(tuple([round(k),round(s)]))
		WS.add(tuple([round(k),-round(s)]))
		
	for n in range(l):
		s = (1/5 *(-5 *(9 - 4 *sqrt(5))**(2 *n + 1) - 2 *sqrt(5) *(9 - 4 *sqrt(5))**(2 *n + 1) - 5 *(9 + 4 *sqrt(5))**(2 *n + 1) + 2 *sqrt(5) *(9 + 4 *sqrt(5))**(2 *n + 1))) 
		k = 1/20 *(4 *(2 *(9 - 4 *sqrt(5))**(2 *n + 1) + sqrt(5) *(9 - 4 *sqrt(5))**(2 *n + 1) + 2 *(9 + 4 *sqrt(5))**(2 *n + 1) - sqrt(5) *(9 + 4 *sqrt(5))**(2 *n + 1)) - 4)
		WS.add(tuple([round(k),round(s)]))
		WS.add(tuple([round(k),-round(s)]))
	
	for n in range(l):
		s = (1/10 *(5 *(9 - 4 *sqrt(5))**(2 *n + 1) + sqrt(5) *(9 - 4 *sqrt(5))**(2 *n + 1) + 5 *(9 + 4 *sqrt(5))**(2 *n + 1) - sqrt(5) *(9 + 4 *sqrt(5))**(2 *n + 1))) 
		k = 1/20 *(-2 *((9 - 4 *sqrt(5))**(2 *n + 1) + sqrt(5) *(9 - 4 *sqrt(5))**(2 *n + 1) + (9 + 4 *sqrt(5))**(2 *n + 1) - sqrt(5) *(9 + 4 *sqrt(5))**(2 *n + 1)) - 4)
		WS.add(tuple([round(k),round(s)]))
		WS.add(tuple([round(k),-round(s)]))
		
	for n in range(l):
		s = (1/10 *(5 *(9 - 4 *sqrt(5))**(2 *n) + sqrt(5) *(9 - 4 *sqrt(5))**(2 *n) + 5 *(9 + 4 *sqrt(5))**(2 *n) - sqrt(5) *(9 + 4 *sqrt(5))**(2 *n))) 
		k = 1/20 *(2 *((9 - 4 *sqrt(5))**(2 *n) + sqrt(5) *(9 - 4 *sqrt(5))**(2 *n) + (9 + 4 *sqrt(5))**(2 *n) - sqrt(5) *(9 + 4 *sqrt(5))**(2 *n)) - 4)
		WS.add(tuple([round(k),round(s)]))
		WS.add(tuple([round(k),-round(s)]))
	
	for n in range(l):
		s = (1/10 *(-5 *(9 - 4 *sqrt(5))**(2 *n) + sqrt(5) *(9 - 4 *sqrt(5))**(2 *n) - 5 *(9 + 4 *sqrt(5))**(2 *n) - sqrt(5) *(9 + 4 *sqrt(5))**(2 *n))) 
		k = 1/20 *(-2 *(-(9 - 4 *sqrt(5))**(2 *n) + sqrt(5) *(9 - 4 *sqrt(5))**(2 *n) - (9 + 4 *sqrt(5))**(2 *n) - sqrt(5) *(9 + 4 *sqrt(5))**(2 *n)) - 4) 
		WS.add(tuple([round(k),round(s)]))
		WS.add(tuple([round(k),-round(s)]))
	
	for n in range(l):
		s = (1/10 *(-5 *(9 - 4 *sqrt(5))**(2 *n + 1) + sqrt(5) *(9 - 4 *sqrt(5))**(2 *n + 1) - 5 *(9 + 4 *sqrt(5))**(2 *n + 1) - sqrt(5) *(9 + 4 *sqrt(5))**(2 *n + 1))) 
		k = 1/20 *(2 *(-(9 - 4 *sqrt(5))**(2 *n + 1) + sqrt(5) *(9 - 4 *sqrt(5))**(2 *n + 1) - (9 + 4 *sqrt(5))**(2 *n + 1) - sqrt(5) *(9 + 4 *sqrt(5))**(2 *n + 1)) - 4)
		WS.add(tuple([round(k),round(s)]))
		WS.add(tuple([round(k),-round(s)]))

	r_1 = ReccurentSolution(0, 1, -9, -4, -2, -20, -9, -4)
	r_2 = ReccurentSolution(0, 1, 161, 72, 32, 360, 161, 72)
	r_3 = ReccurentSolution(0, 1, -9, 4, -2, 20, -9, 4)
	r_4 = ReccurentSolution(0, 1, 161, -72, 32, -360, 161, -72)
	r_5 = ReccurentSolution(0, -1, -9, -4, -2, -20, -9, -4)
	r_6 = ReccurentSolution(0, -1, 161, 72, 32, 360, 161, 72)
	r_7 = ReccurentSolution(0, -1, -9, 4, -2, 20, -9, 4)
	r_8 = ReccurentSolution(0, -1, 161, -72, 32, -360, 161, -72)
	r_9 = ReccurentSolution(-1, 2, -9, -4, -2, -20, -9, -4)
	r_10 = ReccurentSolution(-1, 2, 161, 72, 32, 360, 161, 72)
	r_11 = ReccurentSolution(-1, 2, -9, 4, -2, 20, -9, 4)
	r_12 = ReccurentSolution(-1, 2, 161, -72, 32, -360, 161, -72)
	r_13 = ReccurentSolution(-1, -2, -9, -4, -2, -20, -9, -4)
	r_14 = ReccurentSolution(-1, -2, 161, 72, 32, 360, 161, 72)
	r_15 = ReccurentSolution(-1, -2, -9, 4, -2, 20, -9, 4)
	r_16 = ReccurentSolution(-1, -2, 161, -72, 32, -360, 161, -72)
	S = set()
	R = [r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8, r_9, r_10, r_11, r_12, r_13, r_14, r_15, r_16]
	for i in range(l+1):
		for r in R:
			S.add(r.nextSol())
	
	print("Wolfram not reccur:")
	print(WS - S)
	
	print("Reccur not wolfram:")
	print(S - WS)
