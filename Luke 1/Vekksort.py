import urllib.request

def vekksort(liste):
	
	response = urllib.request.urlopen('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-vekksort.txt')
	#print(copies)
	numbers = []
	for line in response:
		numbers.append(int(line))

	current = numbers[0]
	for i in range(1, len(numbers)):
		if current <= numbers[i]:
			current = numbers[i]
			
		if current > numbers[i]:
			numbers[i] = 0

	
	#print(numbers)
	return sum(numbers)
	
print(vekksort("vekksort.txt"))
