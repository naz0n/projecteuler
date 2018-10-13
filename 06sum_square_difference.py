def sum_square(n):
	a = 0
	b = 0
	for i in range(n+1):
		a +=  i**2
		b += i
	b = b **2
	return b - a
# def square_sum(n):
# 	a = 0
# 	for i in range(n+1):
# 		a +=  i
# 	return a**2
# print square_sum(10)
print sum_square(100)