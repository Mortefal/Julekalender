
f = open('input-birthnumber.txt', 'r')
persons = []
for line in f:
	persons.append(line.rstrip())


def gender(number):
	if int(number[8]) % 2 == 0:
		return 1
	if int(number[8]) % 2 == 1:
		return 2
	else:
		print("wrong gender")
		return False

#print(gender(persons[1]))

def controllSiffer1(number):
	rekken = [3,7,6,1,8,9,4,5,2]
	
	sumRekke = 0
	for i in range(0, len(rekken)):
		sumRekke += int(number[i]) * rekken[i]
	restTall = sumRekke % 11
	if restTall == 0:
		return True
	kontrollTall = 11 - restTall
	if kontrollTall == 10:
		return False
	if kontrollTall == int(number[9]):

		return True
	else:
		return False

def controllSiffer2(number):
	rekke2 = [5,4,3,2,7,6,5,4,3,2]
	summen = 0
	for i in range(0, len(rekke2)):
		summen += int(number[i]) * rekke2[i]
	y = summen % 11
	if y == 1:
		return False
	if y == 0:
		return True
	kontroll  = 11 - y

	if kontroll == 10:
		return False
	if kontroll == int(number[10]):
		return True
	else:
		return False

def checkDate(number):
	if int(number[0]) > 3:
		return False
	if int(number[0]) == 3 and int(number[1]) > 1:
		return False
	else:
		return True

def bornInAugust(number):
	if int(number[3]) == 8 and int(number[2]) == 0:
		return True
	else:
		return False
counter = 0

for person in persons:
	if bornInAugust(person):
		if checkDate(person):
			if gender(person) == 1:
				if controllSiffer1(person):
					if controllSiffer2(person):
						counter += 1

print(counter)