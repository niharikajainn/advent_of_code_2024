import itertools
import queue
import sys
from enum import Enum

trail_map = [list(line.strip()) for line in open("aoc_10.txt", "r").readlines()]
num_rows = len(trail_map)
num_cols = len(trail_map[0])

def main():	
	part_one()

def part_one():
	count_trail = 0
	frontier = queue.LifoQueue()
	trailheads = []
	goals = []
	for col in range(num_cols):
		for row in range(num_rows):
			if(number(row,col) == '0'):
				trailheads.append((row,col))
				trail_map[row][col] = '.'
	
	for trailhead in trailheads:
		trail_map[trailhead[0]][trailhead[1]] = 0
		frontier.put(trailhead)
		while(not frontier.empty()):
			node = frontier.get()
			adjacents = children(*node)
			for child in adjacents:
				if(continues_trail(number(*child),number(*node))):
					if(number(*child) == '9'):
						trail_map[child[0]][child[1]] = '.'
						goals.append(child)
						count_trail += 1
					else:
						frontier.put(child)
		trail_map[trailhead[0]][trailhead[1]] = '.'
		for goal in goals:
			trail_map[goal[0]][goal[1]] = '9'

	print("The total score of the map is", count_trail)
	

def part_two():
	count_trail = 0
	frontier = queue.LifoQueue()
	for col in range(num_cols):
		for row in range(num_rows):
			if(number(row,col) == '0'):
				frontier.put((row,col))	
		while(not frontier.empty()):
			node = frontier.get()
			adjacents = children(*node)
			for child in adjacents:
				if(continues_trail(number(*child),number(*node))):
					if(number(*child) == '9'):
						count_trail += 1
					else:
						frontier.put(child)

	print("There are", count_trail, "unique trails in the map.")


def children(row,col):
	children = []
	if row > 0:
		children.append(up(row,col))
	if row < num_rows-1:
		children.append(down(row,col))
	if col > 0:
		children.append(left(row,col))
	if col < num_cols-1:
		children.append(right(row,col))
	return children

def number(row,col):
	return trail_map[row][col]

def continues_trail(current_number, previous_number):
	if current_number == '.':
		return False
	else:
		return int(current_number) == int(previous_number) + 1

def reset_trail_map():
	trail_map = [list(line.strip()) for line in open("aoc_10.txt", "r").readlines()]

def print_trail_map():
	for line in trail_map:
		print(line)

def up(row,col):
	return row-1,col

def down(row,col):
	return row+1,col

def left(row, col):
	return row,col-1

def right(row,col):
	return row,col+1

if __name__=="__main__":
	main()
