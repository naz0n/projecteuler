def squared(a,b,c):
	if a**2 + b**2 == c**2:
		return True
	return False

def tripsum():
	for a in xrange(500):
		for b in xrange(a + 1, 500):
			c = 1000 - (a + b)
			if squared(a,b,c):
				print a, b, c
				return a * b * c 

print tripsum()
