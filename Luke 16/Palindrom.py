

liste = open('input-palindrom.txt').read().split(',')

string = "".join(liste)

def isPalindrome(liste):
	return liste == liste[::-1]

def isPrime(n):
    if n < 2: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True
def produkt(num):
	summ = 0
	for c in num:
		summ += int(c)
	return summ
def findPal(liste):
	biggestPrime = 0
	length = len(liste)
	for i, num in enumerate(liste):
		start, end = i-1, i + 1
		while start <= end and end < length and liste[start] == liste[end]:
			x = produkt((liste[start: end+1]))
			if (isPrime(x) and x > biggestPrime):
				biggestPrime = x
				print("biggestPrime: " + str(biggestPrime))
			start -= 1
			end += 1
		start, end = i, i + 1
		while start >= 0 and end < length and liste[start] == liste[end]:
			x = produkt(liste[start: end+1])
			if (isPrime(x) and x > biggestPrime):
				biggestPrime = x

			start -= 1
			end += 1
	return biggestPrime

print(findPal(string))
#x = findPal("163832124")

#print(produkt((['1','3','4','2'])))
#1, 6, 3, 8, 3, 2, 1, 2, 4
#print(isPrime(52697))