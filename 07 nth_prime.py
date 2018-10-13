def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	for i in range(2, n):
		if not n % i:
			return False
	return True

def nth_prime(n):
	list_ = []
	for x in range(0, 99999999):
		if is_prime(x):
			list_.append(x)
		if len(list_) == 10002:
			break
	return list_[n-1]
print nth_prime(10001)
