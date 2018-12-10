

file = open('input.txt', 'r')
file = file.readlines()
lst = []
for line in file:
	lst.append(line.rstrip('\n'))

class Stack:

	def __init__(self):
		self.stack = []

	def push(self, values):
		return self.stack.append(values)

	def peek(self):
		return self.stack[-1]

	def remove(self):
		if len(self.stack) <=0:
			return False
		else:
			return self.stack.pop()
	def x(self):
		return len(self.stack)


def kolon(stack):
	pre = stack.x()
	value = 0
	temp = True
	while stack.x() != 0:
		x = stack.remove()
		value += x
	stack.push(value)
	after = stack.x()
	return stack

def mellomrom(stack):
	stack.push(31)
	return stack

def punktum(stack):
	A = stack.remove()
	B = stack.remove()
	stack.push(A-B)
	stack.push(B-A)
	return stack

def strek(stack):
	stack.push(3)
	return stack

def apostrof(stack):
	A = stack.remove()
	B = stack.remove()
	stack.push(A+B)
	return stack

def underscore(stack):

	A = stack.remove()
	B = stack.remove()
	stack.push(A*B)
	stack.push(A)
	return stack
def rightstrek(stack):
	stack.remove()
	return stack

def bokstavenI(stack):
	A = stack.peek()
	stack.push(A)
	return stack

def leftstrek(stack):
	x = stack.remove()
	stack.push(x + 1)
	return stack
def star(stack):
	A = stack.remove()
	B = stack.remove()
	C = int(float(A/B))
	stack.push(C)
	return stack

def leftbracket(stack):
	x = stack.remove()
	if x % 2 == 0:
		stack.push(1)
		return stack
	else:
		return stack

def rightbracket(stack):
	x = stack.remove()
	if x % 2 == 0:
		return stack
	else:
		stack.push(x)
		return stack
def swirlyline(stack):
	a = stack.remove()
	b = stack.remove()
	c = stack.remove()
	stack.push(max_3(a,b,c))

	return stack

def max_2(a,b):
	if a > b:
		return a
	return b

def max_3(a,b,c):
	return max_2(a,max_2(b,c))
def findBiggest(stack):
	lst = []
	temp = True
	while temp:
		x = stack.remove()
		if x == False:
			temp = False
		else:
			lst.append(x)
	return lst
def main():
	x = Stack()
	for i in range(0, len(lst)):
		for j in range(0, len(lst[i])):
			if lst[i][j] == "K":
				break
			if lst[i][j] == " ":
				x = mellomrom(x)
			elif lst[i][j] == ":":
				x = kolon(x)
			elif lst[i][j] == ".":
				x = punktum(x)
			elif lst[i][j] == "|":
				x = strek(x)
			elif lst[i][j] == "'":
				x = apostrof(x)
			elif lst[i][j] == "_":
				x = underscore(x)
			elif lst[i][j] == "/":
				x = rightstrek(x)
			elif lst[i][j] == '\\':
				x = leftstrek(x)
			elif lst[i][j] == "*":
				x = star(x)
			elif lst[i][j] == "]":
				x = leftbracket(x)
			elif lst[i][j] == "[":
				x = rightbracket(x)
			elif lst[i][j] == "~":
				x = swirlyline(x)
			elif lst[i][j] == "i":
				x = bokstavenI(x)
	print(x.peek())
main()