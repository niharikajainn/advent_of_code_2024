import itertools

input = [line.strip().split(":") for line in open("aoc_7.txt", "r").readlines()]
equations = dict()
for line in input:
	equations[int(line[0])] = [int(x) for x in line[1][1:].split(" ")]

def main():	
	part_one_operators = ['*', '+']
	part_two_operators = part_one_operators.append('||')

	compute_valid_total(part_one_operators)
	compute_valid_total(part_two_operators)

def compute_valid_total(operators):
	valid_total = 0
	for equation in equations:
		operands = equations[equation]
		num_operators = len(operands) - 1
		operator_combinations = list(map(list, itertools.product(operators, repeat=num_operators)))
		for combination in operator_combinations:
			result = operands[0]
			for x, y in enumerate(combination):
				if y == '*':
					result *= operands[x+1]
				elif y == '+':
					result += operands[x+1]
				else:
					result = int(str(result)+str(operands[x+1]))
			if result == equation:
				valid_total += equation
				break
	print(valid_total)


if __name__=="__main__":
	main()
