import numpy as np
import itertools

area = [list(line.strip()) for line in open("aoc_8.txt", "r").readlines()]
num_rows = len(area)
num_cols = len(area[0])

antennas = dict()
antinodes = set()

def main():	
	read_map()
	part_one()
	part_two()

def part_one():
	for frequency in antennas:
		positions = antennas[frequency]
		pairs = list(itertools.combinations(positions, 2))
		for pair in pairs:
			(row_1, col_1), (row_2, col_2) = pair
			rise = row_2 - row_1
			run = col_2 - col_1
			new_point_1 = row_2 + rise, col_2 + run
			new_point_2 = row_1 - rise, col_1 - run
			if within_map(*new_point_1):
				antinodes.add(new_point_1)
			if within_map(*new_point_2):
				antinodes.add(new_point_2)
	print(len(antinodes))

def part_two():
	for frequency in antennas:
		positions = antennas[frequency]
		pairs = list(itertools.combinations(positions, 2))
		for pair in pairs:
			(row_1, col_1), (row_2, col_2) = pair
			rise = row_2 - row_1
			run = col_2 - col_1
			new_point = row_2, col_2
			while(within_map(*new_point)):
				antinodes.add(new_point)
				new_point = new_point[0] + rise, new_point[1] + run
			new_point = row_2 - rise, col_2 - run
			while(within_map(*new_point)):
				antinodes.add(new_point)
				new_point = new_point[0] - rise, new_point[1] - run
	print(len(antinodes))

def print_map():
	for line in map:
		print(line)

def read_map():
	for row in range(num_rows):
		for col in range(num_cols):
			if area[row][col] != '.':
				upsert(area[row][col], (row,col))

def upsert(frequency, position):
	if frequency in antennas:
		antennas[frequency].append(position)
	else:
		antennas[frequency] = [position]

def within_map(row,col):
	return row >= 0 and row < num_rows and col >= 0 and col < num_cols
  
# def print_antinodes_map(antinodes):
# 	antinodes_map = []
# 	for row in range(num_rows):
# 		antinodes_row = []
# 		for col in range(num_cols):
# 			if (row,col) in antinodes:
# 				antinodes_row.append("#")
# 			else:
# 				antinodes_row.append(".")
# 		antinodes_map.append(antinodes_row)

# 	for line in antinodes_map:
# 		print(line)

if __name__=="__main__":
	main()
