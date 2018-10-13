def dictionumb(n):
	d = {'1': 'one', '2': 'two', '3': 'three','4': 'four', '5': 'five','6': 'six', '7': 'seven', '8': 'eight', '9':'nine'}
	tens = {'1': 'ten', '2': 'twenty', '3': 'thirty','4': 'forty', '5': 'fifty','6': 'sixty', '7': 'seventy', '8': 'eighty','9': 'ninety'}
	teens = {'1':'eleven', '2':'twelve','3':'thirteen','4':'fourteen','5':'fifteen','6':'sixteen','7':'seventeen','8':'eighteen','9':'nineteen'}
	keyList = []
	a = str(n)
	for item in a:
		for i in item:
			if i in d:
				if len(a) == 3:
					if a[1] == '0' and a[2] == '0':
						keyList.append(d[i] + 'hundred')
						break
					else:
						keyList.append(d[i] + 'hundred' + 'and')
					a = a[1:]
					dictionumb(a)
				elif len(a) == 2:
					if a[0] == '0':
						keyList.append(d[a[1]])
					elif a[0] == '1':
						if a[1] == '0':
							keyList.append(tens[i])
						else:
							keyList.append(teens[a[1]])
							keyList = keyList[:2]
					else:
						keyList.append(tens[i])
						a = a[1:]
						dictionumb(a)
				else:
					keyList.append(d[i])

	new = []
	for i in keyList:
		if i not in new:
			new.append(i)

	return new



new = []
count = 0
for i in range(1,1001):
	new.append(dictionumb(i))
new.append('thousand')
print new
for i in new:
	for j in i:
		for k in j:
			count += 1
print count