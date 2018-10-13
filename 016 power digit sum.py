
def power_digit():
	n = str(2**1000)
	l = []
	for i in n:
		l.append(int(i))
	print sum(l)
power_digit()
