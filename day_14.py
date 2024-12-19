import re

tiles_width = 101
tiles_height = 103


def main():	
	positions = part_one()
	part_two(positions)

def part_one():
	
	bathroom = [[0 for tile in range(tiles_width)] for tile in range(tiles_height)]
	positions = parse_positions()
	iterations = 100
	for position in positions:
		col, row, col_speed, row_speed = position
		bathroom[(row+(row_speed*iterations))%tiles_height][(col+(col_speed*iterations))%tiles_width] += 1
	# print_bathroom()
	quadrants = [[x[:(tiles_width//2)] for x in bathroom[:(tiles_height//2)]], [x[(tiles_width//2)+1:] for x in bathroom[:(tiles_height//2)]],
				 [x[:(tiles_width//2)] for x in bathroom[(tiles_height//2)+1:]], [x[(tiles_width//2)+1:] for x in bathroom[(tiles_height//2)+1:]]]
	safety_factor = 1
	for quadrant in quadrants:
		count_robots = 0
		for row in quadrant:
			for col in row:
				count_robots += col
		safety_factor *= count_robots

	print(safety_factor)
	return positions

def part_two(positions):
	bathroom = [[0 for tile in range(tiles_width)] for tile in range(tiles_height)]
	christmas_tree = False
	iterations = 0
	num_rows = len(bathroom)
	num_cols = len(bathroom[0])
	while not christmas_tree:
		for index in range(len(positions)):
			col, row, col_speed, row_speed = positions[index]
			positions[index] = ((col+col_speed)%tiles_width, (row+row_speed)%tiles_height, col_speed, row_speed)
			if bathroom[row][col] > 0:
				bathroom[row][col] -= 1
			bathroom[(row+row_speed)%tiles_height][(col+col_speed)%tiles_width] += 1
		max_robots_in_a_row = 0
		for row in range(num_rows):
			count_robots_in_a_row = 0
			for col in range(num_cols):
				if bathroom[row][col] == 1:
					count_robots_in_a_row += 1
					max_robots_in_a_row = max(max_robots_in_a_row, count_robots_in_a_row)
				else:
					count_robots_in_a_row = 0
		if max_robots_in_a_row > 10:
			print_bathroom(bathroom)
			christmas_tree = True
			print(iterations)
		iterations += 1


def print_bathroom(bathroom):
	for line in bathroom:
		print(line)

def parse_positions():
	positions = [line.strip() for line in open("aoc_14.txt", "r").readlines()]
	nums=[]
	for position in positions:
		nums.append(tuple([int(x) for x in re.findall(r'-*\d+',position)]))
	return nums

if __name__=="__main__":
	main()
