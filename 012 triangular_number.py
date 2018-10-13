# def tri_sum(n):
# 	tri_sum = 0
# 	for i in range(n + 1):
# 		tri_sum += i
# 	return tri_sum
# a = 7
# def tri_num(n):
# 	for x in range(n):
# 		tri = tri_sum(x)
# 	count = 0
# 	result = []
# 	for i in range(1,5555):
# 		if not tri % i:
# 			result.append(i)
# 			count += 1
# 			if count == 500:
# 				print 'yay!'
# 				break
# 	#print tri_sum(x)
# 	#print result
# 	print result
# 	print len(result)
# tri_num(20000)

#shamelessly stolen from the net
import math
from time import time
t = time()
def divisors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            number_of_factors +=2
        else:
            continue
    return number_of_factors

x=1
for y in range(2,1000000):
    x += y
    if divisors(x) >= 500:
        print x
        break
tt = time()-t
print tt

