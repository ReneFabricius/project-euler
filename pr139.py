from diophantine_equation import ReccurentSolution, linearDiophantineEq, SolutionFlag

def problem139(l):
	n = 0
	r = ReccurentSolution(1,1,3, 2, 0, 4, 3, 0)
	r.nextSol()
	k, s = r.nextSol()
	while k < l:
		f_m, sol_m = linearDiophantineEq(2*(1-k*k), 2*(k*k-s), 0)
		a, b = abs(sol_m.getSol(1)[0]), abs(sol_m.getSol(1)[1])
		c = k*abs(b-a)
		peri = a + b + c
		n += int(l/peri)
		
		k, s = r.nextSol()
	
	return n
