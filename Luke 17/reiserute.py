import math
import itertools
import time

rute = [(7.1,10.5),(18.8,9.2),(2.1,62.1),(74.2,1.5),(58.4,5.6),(15.9,6.2),(44.5,15.6),(88.1,53.4),(36.2,84.2),
(26.9,8.5)]
start_time = time.time()
x = itertools.permutations(rute, 10)

def euklidDistance(point1, point2):
	return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

min_dist = 500
dist = 0

for elem in x:
	for i in range(len(elem) - 1):
		dist += euklidDistance(elem[i], elem[i+1])
	if dist < min_dist:
		min_dist = dist
	dist = 0
print("My program took:", time.time() - start_time)
print(min_dist)