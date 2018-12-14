from itertools import product

def find_combinations(numbers, answer):
    operators = ['+', '-', '']
    combinations = list(product(operators, repeat=len(numbers)-1))
    valid = 0
    for c in combinations:
        result = [None] * (2*len(numbers) - 1)
        result[::2], result[1::2] = numbers, c
        if eval(''.join(result)) == answer:
            valid += 1
    return valid

input = [str(n+1) for n in range(8)] + [str(n) for n in range(7,0,-1)]
print(find_combinations(input, 42))
'''
Hentet løsning fra LF, for å ikke ha en tom luke 5. Takk @danieman
'''