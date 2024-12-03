import re

def main():
	part_one()
	part_two()

def part_one():
	cleaned = re.findall(r"mul\(\d+,\d+\)", store_memory())
	pairs = [parse_mul(function) for function in cleaned]
	print(sum_of_products(pairs))

def part_two():
	cleaned = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", store_memory())
	enabled = True
	enabled_pairs = []
	for function in cleaned:
		if re.match("don't", function):
			enabled = False
		elif re.match("do", function):
			enabled = True
		else: #mul instruction
			if enabled:
				enabled_pairs.append(parse_mul(function))
	print(sum_of_products(enabled_pairs))

def sum_of_products(pairs):
	sum_of_products = 0
	for x,y in pairs:
		sum_of_products += x * y
	return sum_of_products

def parse_mul(funct):
	return tuple(map(int, tuple(funct[4:-1].split(","))))

def store_memory():
	return open("aoc_3.txt", "r").read()

if __name__=="__main__":
    main()
