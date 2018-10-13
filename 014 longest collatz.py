def collatz_sequence(x): #shamelessly stolen, since initial code was buggy
    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1 
       seq.append(x)    
    return seq

def longest_finder():
	length = 0
	max_ = 1000000
	while True:
		a = collatz_sequence(max_)
		if len(a) > length:
			length = len(a)
			print len(a)
			print max_
		max_ -= 1
		if max_ == 1000:
			print 'done'
longest_finder()

