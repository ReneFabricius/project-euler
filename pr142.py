from math import sqrt
from pythagorean_quadruples import quadrupletGenerator

def problem142():
	for ql in quadrupletGenerator():
			
		s_56 = list(ql[:3])
		qsum = 0
		s_2 = 0
		for qe in ql:
			qsum += qe*qe
			if qe % 2 == 1 and qe in s_56:
				s_56.remove(qe)
				s_2 = qe
		
		
		s_3 = sqrt((qsum - 2*s_56[0]**2) / 2)
		if s_3.is_integer():
			s_4 = sqrt((qsum - 2*s_56[1]**2) / 2)
			if s_4.is_integer():
				x = (ql[3]**2 + s_2**2) / 2
				y = (s_56[0]**2 + s_56[1]**2) / 2
				z = abs((s_56[0]**2 - s_56[1]**2) / 2)
				if x > y and y > z and z > 0:
					return tuple([x, y, z])
