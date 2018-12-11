import urllib.request


response = urllib.request.urlopen('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-crisscross.txt')
coordinates = []
for line in response:
	coordinates.append(line)

def getCood(coordinates):
	x = 0
	y = 0

	for i in range(0, len(coordinates)):
		for j in range(0, len(coordinates[i]), 2):
			if coordinates[i][j] == "V":
				x -= int(coordinates[i][j-1])
			elif coordinates[i][j] == "H":
				x += int(coordinates[i][j-1])
			elif coordinates[i][j] == "B":
				y -= int(coordinates[i][j-1])
			elif coordinates[i][j] == "F":
				y += int(coordinates[i][j-1])
	return [x,y]

print(getCood(coordinates))