import itertools
import queue
import sys
from enum import Enum

word_search = [list(line.strip()) for line in open("aoc_4.txt", "r").readlines()]
num_rows = len(word_search)
num_cols = len(word_search[0])

class Direction(Enum):
	UP_LEFT = 1
	UP = 2
	UP_RIGHT = 3
	LEFT = 4
	RIGHT = 5
	DOWN_LEFT = 6
	DOWN = 7
	DOWN_RIGHT = 8
	ANY = 9

def main():		
	part_one()
	part_two()

def part_one():
	count_xmas = 0
	frontier = queue.SimpleQueue()
	for col in range(num_cols):
		for row in range(num_rows):
			if(letter(row,col)=='X'):
				frontier.put((row,col,Direction.ANY.name))
	while(not frontier.empty()):
		node = frontier.get()
		node_row, node_col, search_direction = node
		if(letter(node_row,node_col) == 'S'):
			count_xmas += 1
		adjacents = children(*node)
		for child in adjacents:
			if(continues_word(letter(child[0], child[1]),letter(node_row, node_col))):
				frontier.put(child)
	print(count_xmas)

def part_two():
	count_x_mas = 0
	for col in range(1, num_cols-1):
		for row in range(1, num_rows-1):
			left_diagonal_mas, right_diagonal_mas = False, False
			if(letter(row,col)=='A'):
				if((letter(*up_left_indices(row,col))=='M' and letter(*down_right_indices(row,col))=='S') 
					or (letter(*up_left_indices(row,col))=='S') and (letter(*down_right_indices(row,col))=='M')):
					left_diagonal_mas = True
				if((letter(*down_left_indices(row,col))=='M' and letter(*up_right_indices(row,col))=='S') 
					or (letter(*down_left_indices(row,col))=='S') and (letter(*up_right_indices(row,col))=='M')):
					right_diagonal_mas = True
				if(right_diagonal_mas and left_diagonal_mas):
					count_x_mas += 1
	print(count_x_mas)

def children(row,col,direction):
		if direction == Direction.UP_LEFT.name and row > 0 and col > 0:
			return [(*up_left_indices(row,col), Direction.UP_LEFT.name)]
		elif direction == Direction.UP.name and row > 0:
			return [(*up_indices(row,col), Direction.UP.name)]
		elif direction == Direction.UP_RIGHT.name and row > 0 and col < num_cols-1:
			return [(*up_right_indices(row,col), Direction.UP_RIGHT.name)]
		elif direction == Direction.LEFT.name and col > 0:
			return [(*left_indices(row,col), Direction.LEFT.name)]
		elif direction == Direction.RIGHT.name and col < num_cols-1:
			return [(*right_indices(row,col), Direction.RIGHT.name)]
		elif direction == Direction.DOWN_LEFT.name and row < num_rows-1 and col > 0:
			return [(*down_left_indices(row,col), Direction.DOWN_LEFT.name)]
		elif direction == Direction.DOWN.name and row < num_rows-1:
			return [(*down_indices(row,col), Direction.DOWN.name)]
		elif direction == Direction.DOWN_RIGHT.name and row < num_rows-1 and col < num_cols-1:
			return [(*down_right_indices(row,col), Direction.DOWN_RIGHT.name)]
		elif direction == Direction.ANY.name:
			children_rows = [row]
			children_cols = [col]
			if(row > 0):
				children_rows.append(up(row))
			if(row < num_rows-1):
				children_rows.append(down(row))
			if(col > 0):
				children_cols.append(left(col))
			if(col < num_cols-1):
				children_cols.append(right(col))
			indices = list(itertools.product(children_rows, children_cols))[1:]
			children = []
			for adj_row, adj_col in indices:
				horizontal = ""
				vertical = ""
				if(adj_col == left(col)):
					horizontal = "LEFT"
				elif(adj_col == right(col)):
					horizontal = "RIGHT"
				if(adj_row == down(row)):
					vertical = "DOWN"
				elif(adj_row == up(row)):
					vertical = "UP"
				if horizontal != "" and vertical != "":
					direction = vertical+"_"+horizontal
				else:
					direction = vertical+horizontal
				children.append((adj_row, adj_col, direction))
			return children
		else:
			return []

def letter(row,col):
	return word_search[row][col]

def continues_word(current_letter, previous_letter):
		if current_letter == 'M':
			return previous_letter == 'X'
		elif current_letter == 'A':
			return previous_letter == 'M'
		elif current_letter == 'S':
			return previous_letter == 'A'
		else:
			return False

def up_left_indices(row,col):
	return (up(row),left(col))

def up_indices(row,col):
	return(up(row),col)

def up_right_indices(row,col):
	return(up(row),right(col))

def left_indices(row,col):
	return(row,left(col))

def right_indices(row,col):
	return(row,right(col))

def down_left_indices(row,col):
	return (down(row),left(col))

def down_indices(row,col):
	return(down(row),col)

def down_right_indices(row,col):
	return(down(row),right(col))

def up(row):
	return(row-1)

def down(row):
	return(row+1)

def left(col):
	return(col-1)

def right(col):
	return(col+1)

if __name__=="__main__":
    main()
