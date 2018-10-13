def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	for i in range(2, n):
		if not n % i:
			return False
	return True

def primesum():
	n = 2000000
	val = 0
	for i in range(n):
		if is_prime(i):
			val += i
	return val
#primesum()


def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)
    return primes

#print primes_sieve(2000000)


###MOST EFFERCTIVE METHOD###
sieve = [True] * 2000000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

print sum(i for i in xrange(2, len(sieve)) if sieve[i])
