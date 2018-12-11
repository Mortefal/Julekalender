import urllib.request

response = urllib.request.urlopen('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-crisscross.txt').read()

tekstinput = response.decode("utf-8")

def getCood(coordinates):
	x = 0
	y = 0
	for i in range(1, len(coordinates), 2):
		if coordinates[i] == "H":
			x += int(coordinates[i-1])
		elif coordinates[i] == "V":
			x -= int(coordinates[i-1])
		elif coordinates[i] == "F":
			y += int(coordinates[i-1])
		elif coordinates[i] == "B":
			y -= int(coordinates[i-1])
	return [x,y]
print(getCood(tekstinput))