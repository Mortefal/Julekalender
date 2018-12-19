import sys
import time

def isPrime(n):
    if n < 2: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

sek = [1,3]
primes = [3]

def sekvens(k):
	start_time = time.time()
	sys.setrecursionlimit(5000)
	temp = []

	if len(primes) == 100:
		print("calculating")
		return sum(primes)


	for i in range(0, len(sek)-1):
		for j in range(i+1, len(sek)):
			if sek[i] == sek[j]:
				continue
			if sek[i] + sek[j] > sek[-1] + k or len(temp) > 1:
				break
			if sek[i] + sek[j] == sek[-1] + k:

				temp.append(sek[i] + sek[j])
	if len(temp) == 1:
		if isPrime(temp[0]):
			primes.append(temp[0])
		sek.append(temp[0])
		k = 1
		return sekvens(k)
	return sekvens(k+1)

print(sekvens(1))
print("Tok", time.time() - start_time)