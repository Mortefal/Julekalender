import urllib.request

response = urllib.request.urlopen('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-gullbursdag.txt')
people = []
for line in response:
	people.append(int(line.rstrip().decode('utf-8').split('f.')[-1]))

def findPossibleGoldAges():
	ages = []
	for i in range(1, 100):
		ages.append([i,i**2])
	return ages

def checkIfPossible(ages, people):

	possible = 0

	for elem in people:
		for i in range(0, len(ages)):
			if elem + ages[i][0] == ages[i][1]:
				possible += 1
	return possible
def main():
	ages = findPossibleGoldAges()
	print(checkIfPossible(ages, people))
main()