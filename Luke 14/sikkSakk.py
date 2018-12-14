import decimal

file = open('tekstInput.txt', 'r').read()

def Coordinates(file):
	positions = [(1,1)]
	x = 1
	y = 1
	positionLength = 0
	for i in range(1, len(file), 2):
		if file[i] == 'H':
			positionLength += int(file[i-1])
			for j in range(1,int(file[i-1]) + 1):
				x += 1
				positions.append((x,y))

		elif file[i] == 'V':
			positionLength += int(file[i-1])
			for j in range(1,int(file[i-1]) +1):
				x -= 1
				positions.append((x,y))

		elif file[i] == 'F':
			positionLength += int(file[i-1])
			for j in range(1,int(file[i-1]) + 1):
				y += 1
				positions.append((x,y))

		elif file[i] == 'B':
			positionLength += int(file[i-1])
			for j in range(1,int(file[i-1])+ 1):
				y -= 1
				positions.append((x,y))

	return positions, positionLength


def findAreal(positions):
	maxX = max(positions, key=lambda x: x[0])
	maxY = max(positions, key=lambda x: x[1])
	minX = min(positions, key=lambda x: x[0])
	minY = min(positions, key=lambda x: x[1])

	areal = (float(maxX[0]+ 1) - float(minX[0])) * (float(maxY[1] + 1) - float(minY[1]))
	
	return areal

def getEmptySpots(unique, area):
	empty = area - unique
	return empty

def main():
	lst = Coordinates(file)
	count = lst[1]
	unique = len(set(lst[0]))
	areal = findAreal(lst[0])
	empty = getEmptySpots(len(set(lst[0])), areal)
	print(decimal.Decimal(unique) / decimal.Decimal(empty))

main()
