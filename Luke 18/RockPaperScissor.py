import time

players = {
	1: 0,
	2: 0,
	3: 0,
}
dic = {
	'RRR': 'draw',
	'RRS': 'AB',
	'RRP': 'c',
	'RSR': 'AC',
	'RSS': 'a',
	'RSP': 'draw',
	'RPR': 'b',
	'RPS': 'draw',
	'RPP': 'BC',
	'SRR': 'BC',
	'SRS': 'b',
	'SRP': 'draw',
	'SSR': 'c',
	'SSS': 'draw',
	'SSP': 'AB',
	'SPR': 'draw',
	'SPS': 'AC',
	'SPP': 'a',
	'PRR': 'a',
	'PRS': 'draw',
	'PRP': 'AC',
	'PSR': 'draw',
	'PSS': 'BC',
	'PSP': 'b',
	'PPR': 'AB',
	'PPS': 'c',
	'PPP': 'draw'
}

def readFile():
	f = open('matchlog.txt', 'r').read()
	return f

def doubleDraw(string):
	a = string[0]
	b = string[1]
	if a == 'P' and b == 'R':
		return 1
	elif a == 'P' and b == 'S':
		return 0
	elif a == 'S' and b == 'P':
		return 1
	elif a == 'S' and b == 'R':
		return 0
	elif a == 'R' and b == 'S':
		return 1
	elif a == 'R' and b == 'P':
		return 0
	else:
		return -1

def main():
	start_time = time.time()
	f = readFile()
	j = 0

	while j < len(f):

		a = f[j]
		b = f[j+1]
		c = f[j+2]
		string = a+b+c
		if dic[string] == 'a':
			players[1] += 1
			j+=3
			continue
		elif dic[string] == 'b':
			players[2] += 1
			j+=3
			continue
		elif dic[string] == 'c':
			players[3] += 1
			j+=3
			continue
		elif dic[string] == 'draw':
			j+= 3
			continue
		elif dic[string] == 'AB':
			j += 3
			a = f[j]
			b = f[j+1]
			st = a+b
			if doubleDraw(st) == -1:
				j+=2
				a = f[j]
				b = f[j+1]
				st = a+b
				while doubleDraw(st) == -1:
					j += 2
					st = f[j] + f[j+1]
			if doubleDraw(st) == 1:
				players[1] += 1
				j+=2
				continue
			elif doubleDraw(st) == 0:
				players[2] += 1
				j+=2
				continue
		elif dic[string] == 'AC':
			
			
			j += 3
			a = f[j]
			b = f[j+1]
			st = a+b
			
			if doubleDraw(st) == -1:
				j+=2
				a = f[j]
				b = f[j+1]
				st = a+b
				
				while doubleDraw(st) == -1:
					j += 2
					st = f[j] + f[j+1]
			if doubleDraw(st) == 1:
				players[1] += 1
				j+=2
				continue
			elif doubleDraw(st) == 0:
				players[3] += 1
				j+=2
				continue
		elif dic[string] == 'BC':
			
			
			j += 3
			
			a = f[j]
			b = f[j+1]
			st = a+b
			
			if doubleDraw(st) == -1:
				j+=2
				a = f[j]
				b = f[j+1]
				st = a+b
				
				while doubleDraw(st) == -1:
					j += 2
					
					st = f[j] + f[j+1]
					
			if doubleDraw(st) == 1:
				players[2] += 1
				j+=2
				continue
			elif doubleDraw(st) == 0:
					players[3] += 1
					j+=2
					continue

	print("Tok:", time.time() - start_time)
main()