
def juletall():
	counter = 0
	for i in range(16777216, 4294967296, 2**11):
		if primeFactor(i) == 24:
			counter += 1
	return counter

def primeFactor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return len(factors)

print(juletall())