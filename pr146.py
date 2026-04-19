import primes

def problem146(l, K):
	N = []
	step = 210
	bases = [10, 80, 130, 200]
	to_be_offsets = [1, 3, 7, 9, 13, 27]
	not_to_be_offset = 21
	t = 0
	while t*step + bases[0] < l:
		t_step = t*step
		for base in bases:
			n = t_step + base
			n2 = n**2
			disproven = False
			for t_b_off in to_be_offsets:
				if not primes.isPrimeMillerRabin(n2 + t_b_off, K):
					disproven = True
					break
			
			if not disproven:
				if not primes.isPrimeMillerRabin(n2 + not_to_be_offset, K):
					N += [n]
					
		t += 1
		
	return N
	
