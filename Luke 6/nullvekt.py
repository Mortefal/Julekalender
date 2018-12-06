def nullvekt():
	return sum([i for i in range(0, 18163106) if str(i).count('0') > len(str(i))/2])
print(nullvekt())

