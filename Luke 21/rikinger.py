
primes = []
f = open('primes10m.txt', 'r')
line = f.readline()
x = line.strip().split(',')
for i in x:
	if i == '':
		continue
	primes.append(int(i))


rikinger = []
def is_abundant(n):
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctr_sum > n
#	print(len(primes))

for elem in primes:
	if (elem + 2) in primes and is_abundant(elem + 1):
		if len(rikinger) % 100 == 0:
			print(len(rikinger))
		rikinger.append(elem+1)

print(sum(rikinger))