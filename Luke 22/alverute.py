import math
import time

start_time = time.time()
file = open('input-luke-22.txt', 'r')


coords = []
for line in file:
	x = line.rstrip().split(',')
	numLine = [float(x[0]), float(x[1])]
	coords.append(numLine)


# Find max x value.
maxX = max(coords, key=lambda x:x[0])
minX = min(coords, key=lambda x:x[0])

def euklidDistance(point1, point2):
	return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
print(math.pi*euklidDistance(minX, maxX))
print("Programmet tok: ", time.time() - start_time)