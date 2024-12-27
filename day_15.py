from enum import Enum

warehouse = [list(line.strip()) for line in open("aoc_15_map.txt", "r").readlines()]
boxes = set()
boxes_second = set()
second_warehouse = []
for row in range(len(warehouse)):
	warehouse_row = []
	for col in range(len(warehouse[0])):
		obj = warehouse[row][col]
		if obj == "#":
			new_obj = ["#", "#"]
		elif obj == "O":
			new_obj = ["[", "]"]
		elif obj == ".":
			new_obj = [".", "."]
		else:
			new_obj = ["@", "."]
		warehouse_row += new_obj
	second_warehouse.append(warehouse_row)

moves = [item for row in [list(line.strip()) for line in open("aoc_15_moves.txt", "r").readlines()] for item in row]

class Direction(Enum):
	UP = 1
	LEFT = 2
	RIGHT = 3
	DOWN = 4

def main():	
	part_one()
	part_two()

def part_one():
	for row in range(len(warehouse)):
		for col in range(len(warehouse[0])):
			obj = warehouse[row][col]
			if obj == '@':
				start = (row,col)
			elif obj == "O":
				boxes.add((row,col))

	row, col = start
	for move in moves:
		if move == "^":
			direction = Direction.UP
		elif move == "<":
			direction = Direction.LEFT
		elif move == ">":
			direction = Direction.RIGHT
		else:
			direction = Direction.DOWN

		peek_next_position = peek_direction(row, col, direction)
		if should_shift(*peek_next_position, direction):
			warehouse[row][col] = "."
			row, col = peek_next_position

	# print_warehouse()
	gps = 0
	for row,col in boxes:
		gps += 100*row + col
	print("The total GPS value is", gps, "in the first warehouse.")

def part_two():
	for row in range(len(second_warehouse)):
		for col in range(len(second_warehouse[0])):
			obj = second_warehouse[row][col]
			if obj == '@':
				start = (row,col)
			elif obj == "[":
				boxes_second.add((row,col))

	row, col = start
	for move in moves:
		if move == "^":
			direction = Direction.UP
		elif move == "<":
			direction = Direction.LEFT
		elif move == ">":
			direction = Direction.RIGHT
		else:
			direction = Direction.DOWN

		peek_next_position = peek_direction(row, col, direction)
		if should_shift_wide_box(*peek_next_position, direction):
			next_row, next_col = peek_next_position
			next_obj = second_warehouse[peek_next_position[0]][peek_next_position[1]]
			if next_obj != ".": # robot is adjacent to a box
				shift_wide_box(next_row, next_col, direction)
			second_warehouse[row][col] = "."

			row,col = next_row, next_col
			second_warehouse[row][col] = "@"

	gps = 0
	for row,col in boxes_second:
		gps += 100*row + col
	print("The total GPS value is", gps, "in the second warehouse.")

def should_shift(row, col, direction):
	global warehouse
	obj = warehouse[row][col]
	if obj == "#":
		return False
	elif obj == ".":
		return True
	else:
		peek_new_position = peek_direction(row, col, direction)
		if should_shift(*peek_new_position, direction):
			global boxes

			warehouse[row][col] = "."
			new_row, new_col = peek_new_position
			warehouse[new_row][new_col] = "O"

			boxes.remove((row,col))
			boxes.add((new_row,new_col))
			return True
		else:
			return False

def should_shift_wide_box(row, col, direction):
	global second_warehouse
	obj = second_warehouse[row][col]
	if obj == "#":
		return False
	elif obj == ".":
		return True
	else:
		if obj == "[":
				left_end = row,col
				right_end = right(row,col)
		else: # ]
				left_end = left(row,col)
				right_end = row,col
		if direction == Direction.UP or direction == Direction.DOWN:
			peek_new_position_left = peek_direction(*left_end, direction)
			peek_new_position_right = peek_direction(*right_end, direction)
			if (should_shift_wide_box(*peek_new_position_left, direction) and 
				should_shift_wide_box(*peek_new_position_right, direction)):
				return True
			return False
		elif direction == Direction.LEFT:
			peek_new_position_left = left(*left_end)
			peek_new_position_right = left_end
			if should_shift_wide_box(*peek_new_position_left, direction):
				return True
		else: # RIGHT
			peek_new_position_left = right_end
			peek_new_position_right = right(*right_end)
			if should_shift_wide_box(*peek_new_position_right, direction):
				return True
		return False

def shift_wide_box(row, col, direction):
	global second_warehouse
	obj = second_warehouse[row][col]
	if obj == ".":
		return
	else:
		if obj == "[":
			left_end = row,col
			right_end = right(row,col)
		else: # ]
			left_end = left(row,col)
			right_end = row,col

		if direction == Direction.UP or direction == Direction.DOWN:
			peek_new_position_left = peek_direction(*left_end, direction)
			peek_new_position_right = peek_direction(*right_end, direction)
		elif direction == Direction.LEFT:
			peek_new_position_left = left(*left_end)
			peek_new_position_right = left_end
		else: #RIGHT
			peek_new_position_left = right_end
			peek_new_position_right = right(*right_end)

		if direction == Direction.LEFT:
			shift_wide_box(peek_new_position_left[0], peek_new_position_left[1], direction)
		elif direction == Direction.RIGHT:
			shift_wide_box(peek_new_position_right[0], peek_new_position_right[1], direction)
		else:
			shift_wide_box(peek_new_position_left[0], peek_new_position_left[1], direction)
			shift_wide_box(peek_new_position_right[0], peek_new_position_right[1], direction)

		second_warehouse[left_end[0]][left_end[1]] = "."
		second_warehouse[right_end[0]][right_end[1]] = "."
		second_warehouse[peek_new_position_left[0]][peek_new_position_left[1]] = "["
		second_warehouse[peek_new_position_right[0]][peek_new_position_right[1]] = "]"
		boxes_second.remove(left_end)
		boxes_second.add(peek_new_position_left)
		return

def print_warehouse():
	for line in warehouse:
		print("".join(line))

def print_second_warehouse():
	for line in second_warehouse:
		print("".join(line))

def peek_direction(row, col, direction):
	if direction == Direction.UP:
		return up(row,col)
	elif direction == Direction.LEFT:
		return left(row,col)
	elif direction == Direction.RIGHT:
		return right(row,col)
	else:
		return down(row,col)

def up(row,col):
	return row-1,col, 

def down(row,col):
	return row+1,col

def left(row,col):
	return row,col-1

def right(row,col):
	return row,col+1

if __name__=="__main__":
	main()
