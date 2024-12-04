import csv
import numpy as np


def main():
	part_one()
	part_two()

def part_one():
	safe_count = 0
	for row in parse():
		levels = [int(i) for i in row]
		arr = np.array(levels)
		if is_safe(arr):
			safe_count += 1
	print("There are", safe_count, "safe reports.")

def part_two():
	safe_count = 0
	for row in parse():
		levels = [int(i) for i in row]
		for index in range(len(levels)):
			missing_one_level = levels[0:index] + levels[index+1:len(levels)]
			if is_safe(missing_one_level):
				safe_count += 1
				break
	print("There are", safe_count, "safe reports if we use the Problem Dampener.")

# 	# Ways to be unsafe:
# 		# increasing or decreasing too steeply (removing won't make less steep)
# 		# more than one inflection point
# 		# one no-change and one inflection point

# def part_two_faster():
# 	safe_count = 0
# 	with open('aoc_2.csv') as csvfile:
# 		reader = csv.reader(csvfile, delimiter = ' ')
# 		for row in reader:
# 			levels = [int(i) for i in row]
# 			pairwise_differences = np.diff(levels)
# 			if(not np.all(pairwise_differences >= -3) or not np.all(pairwise_differences <= 3)):
# 				continue
# 			products = []
# 			for x in range(len(pairwise_differences)-1):
# 				products.append(pairwise_differences[x]*pairwise_differences[x+1])
# 			inflections = np.array(products)
# 			num_inflections = np.count_nonzero(inflections < 0)
# 			num_no_changes = np.count_nonzero(pairwise_differences == 0)
# 			if num_inflections > 1:
# 				print(levels)
# 				continue
# 			if num_no_changes > 0 and num_inflections > 0:
# 				continue
# 			safe_count += 1

# 	print("There are", safe_count, "safe reports if we use the Problem Dampener.")

def parse():
	csvfile = open('aoc_2.csv')
	return csv.reader(csvfile, delimiter = ' ')

def is_safe(arr):
	if is_increasing_gradually(arr) or is_decreasing_gradually(arr):
		return True

def is_increasing_gradually(arr):
	pairwise_differences = np.diff(arr)
	return np.all(pairwise_differences <= 3) and np.all(pairwise_differences >= 1)

def is_decreasing_gradually(arr):
	pairwise_differences = np.diff(arr)
	return np.all(pairwise_differences >= -3) and np.all(pairwise_differences <= -1)


if __name__=="__main__":
    main()

