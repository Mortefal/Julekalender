import numpy as np
def readFile():
	f = open('input-rain.txt', 'r')
	lines = f.read().split('\n')
	lines = [i.split(';') for i in lines]
	vectors = []
	for i in range(len(lines)):
		vectors.append([int(lines[i][1].strip('()').split(',')[0])-
        	int(lines[i][0].strip('()').split(',')[0]),
        	int(lines[i][1].strip('()').split(',')[1])-
        	int(lines[i][0].strip('()').split(',')[1])])
	return vectors

def oneElem(vectors):
	unique = []
	for elem in vectors:
		if elem not in unique:
			unique.append(elem)
	return unique

def crossproduct(unique):
	diffent_par = []
	for i in range(0, len(unique) -1):
		for j in range(i+1, len(unique)):
			if np.cross(np.array([unique[i][0], unique[i][1]]),
                       np.array([unique[j][0], unique[j][1]])) == 0:
				diffent_par.append(unique[i])
				diffent_par.append(unique[j])
	return diffent_par

def allVectors(vectors, diffent_par):
	all = [[], []]
	for i in range(len(vectors)):
		if vectors[i] == diffent_par[0] or vectors[i] == diffent_par[1]:
			all[0].append(vectors[i])
		elif vectors[i] == diffent_par[2] or vectors[i] == diffent_par[3]:
			all[1].append(vectors[i])
	return max(len(all[0]), len(all[1]))

def main():
	vectors = readFile()
	unique = oneElem(vectors)
	cross = crossproduct(unique)
	result = allVectors(vectors, cross)
	print(result)
main()