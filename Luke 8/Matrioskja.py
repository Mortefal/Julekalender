import urllib.request
from operator import itemgetter

response = urllib.request.urlopen('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-dolls.txt')
numbers = []
for line in response:
	line = line.decode('utf-8').rstrip('\n').split(',')
	line[1] = int(line[1])
	numbers.append(line)
	numbers.sort(key=lambda x:x[1])

def matrioskja(numbers):
	dukke = []
	current = numbers[0]
	for i in range(1, len(numbers)):
		if current[0] != numbers[i][0]:
			dukke.append(current)
			current = numbers[i]
	return len(dukke)

print(matrioskja(numbers))

