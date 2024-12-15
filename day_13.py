import sympy
import re

def main():	
	nums = parse_equations()
	part_one(nums)
	part_two(nums)

def part_one(nums):
	i = 0
	tokens = 0
	while i <len(nums):
		matrix_input = nums[i:i+3]
		i +=4 
		tokens += tokens_for_slot(matrix_input)
	print("It would take", tokens, "tokens to win all possible prizes.")

def part_two(nums):
	i = 0
	tokens = 0
	while i < len(nums):
		for index, num in enumerate(nums[i+2]):
			nums[i+2][index] += 10000000000000
		matrix_input = nums[i:i+3]
		i +=4 
		tokens += tokens_for_slot(matrix_input)
	print("It would take", tokens, "tokens to win all possible prizes, using corrected coordinates.")

def parse_equations():
	equations = [line.strip() for line in open("aoc_13.txt", "r").readlines()]
	nums=[]
	for equation in equations:
		nums.append([int(x) for x in re.findall(r'\d+',equation)])
	return nums

def tokens_for_slot(matrix_input):
	matrix = sympy.Matrix(matrix_input).T
	rref = matrix.rref()[0]
	a_presses = rref[2]
	b_presses = rref[5]
	if a_presses % 1 == 0 and b_presses % 1 == 0:
		return 3*a_presses + b_presses
	else:
		return 0

if __name__=="__main__":
	main()
