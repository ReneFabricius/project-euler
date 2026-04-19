from diophantine_equation import ReccurentSolution

def problem138(l):
	r_p = ReccurentSolution(0, 1, -9, -8, -8, -10, -9, -8)
	r_p.nextSol()
	s = 0
	for i in range(l):
		s += abs(r_p.nextSol()[1])
	return s
