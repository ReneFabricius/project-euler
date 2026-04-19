def problem145(l):
	c = 0
	R = []
	for n in range(1, l):
		if n % 10 != 0:
			stn = str(n)
			rn = int(stn[::-1])
			suma = rn + n
			not_r = False
			suma_s = suma
			while suma:
				d = suma % 10
				suma //= 10
				if d % 2 == 0:
					not_r = True
					break
			
			if not not_r:
				c += 1
				R += [tuple([n, suma_s])]
	
	return R, c
	
""" Inspiraciou z ciastocnych vysledkov brute-forcu na papier pre jednotlive pocty cifier, princip je urcit, do ktorych pozicii je nutne, carry (11 a viac v sucte na vyssej pozicii) a do ktorych
je to naopak vylucene, kombinacie suctov do jednotlivych druhov policok vzhladom k potrebe carry, ponasobit"""
