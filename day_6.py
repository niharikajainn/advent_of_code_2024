from enum import Enum

map = [list(line.strip()) for line in open("aoc_6.txt", "r").readlines()]
num_rows = len(map)
num_cols = len(map[0])

class Direction(Enum):
	UP = 1
	LEFT = 2
	RIGHT = 3
	DOWN = 4

def main():	
	obstacles, start = read_map()
	visited = part_one(obstacles, start)

	visited.remove(start)
	part_two(visited, obstacles, start)

def part_one(obstacles, start):
	visited = move(obstacles, start)
	print("The guard patrols in", len(visited), "different locations before leaving the area.")
	return visited


def part_two(visited, obstacles, start):
	
	count_loop = 0
	count_no_loop = 0

	for visit in visited:
		temp_obstacle = visit
		obstacles.add(temp_obstacle)

		row,col = start
		obstacles_direction = dict()
		direction = Direction.UP.name

		while within_map(row,col):
			if go_direction(direction,row,col) in obstacles:
				obstacles_direction, already_exists = upsert(obstacles_direction, (go_direction(direction, row, col)), direction)
				if already_exists:
					count_loop += 1
					obstacles.remove(temp_obstacle)
					break
				direction = turn(direction)
			else:
				row,col = go_direction(direction,row,col)

		if temp_obstacle in obstacles:
			count_no_loop += 1
			obstacles.remove(temp_obstacle)


	print("There are", count_loop, "ways to place an obstacle to cause the guard to loop.")

def read_map():
	obstacles = set()
	visited = set()
	for row in range(num_rows):
		for col in range(num_cols):
			if map[row][col] == '^':
				start = row,col
			if map[row][col] == '#':
				obstacles.add((row,col))
	return obstacles, start

def move(obstacles, start):
	row, col = start
	direction = Direction.UP.name
	visited = set()

	while within_map(row,col):
		visited.add((row,col))
		row,col = go_direction(direction, row,col)
		if go_direction(direction,row,col) in obstacles:
			direction = turn(direction)
	return visited


def within_map(row,col):
	return row >= 0 and row < num_rows and col >= 0 and col < num_cols


def turn(direction):
	if direction == Direction.UP.name:
		return Direction.RIGHT.name
	elif direction == Direction.RIGHT.name:
		return Direction.DOWN.name
	elif direction == Direction.DOWN.name:
		return Direction.LEFT.name
	else:
		return Direction.UP.name

def go_direction(direction, row,col):
	if direction == Direction.UP.name:
		return up(row,col)
	elif direction == Direction.RIGHT.name:
		return right(row,col)
	elif direction == Direction.DOWN.name:
		return down(row,col)
	else:
		return left(row,col)

def upsert(dictionary, obstacle, direction):
	already_exists = False
	if obstacle not in dictionary:
			dictionary[obstacle] = {direction}
	else:
		if direction not in dictionary[obstacle]:
			dictionary[obstacle].add(direction)
		else:
			already_exists = True
	return dictionary, already_exists

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
