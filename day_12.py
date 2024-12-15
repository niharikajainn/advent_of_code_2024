import queue

garden = [list(line.strip()) for line in open("aoc_12.txt", "r").readlines()]
num_rows = len(garden)
num_cols = len(garden[0])

def main():	
	# print_garden()
	part_one()
	part_two()

def part_one():
	perimeter = 0
	count_area = 1
	price = 0
	visited = set()
	frontier = queue.LifoQueue()
	next_plot = next_plot_in_frontier(frontier, visited)
	while(next_plot):
		frontier.put(next_plot)
		while(not frontier.empty()):
			node = frontier.get()
			visited.add(node)
			adjacents = children(node)
			for child in adjacents:
				if(child not in visited and child not in frontier.queue):
					count_area += 1
					frontier.put(child)
			perimeter += 4-len(adjacents)	
		price += perimeter*count_area
		# print(plant(*next_plot), perimeter)
		perimeter=0
		count_area=1
		next_plot = next_plot_in_frontier(frontier, visited)
	print("The price to put put fences in the garden when counting plot perimeter is", price)

def part_two():
	vertices = 0
	count_area = 1
	price = 0
	visited = set()
	frontier = queue.LifoQueue()
	next_plot = next_plot_in_frontier(frontier, visited)
	while(next_plot):
		frontier.put(next_plot)
		while(not frontier.empty()):
			node = frontier.get()
			visited.add(node)
			adjacents = children(node)
			for child in adjacents:
				if(child not in visited and child not in frontier.queue):
					count_area += 1
					frontier.put(child)
			vertices += count_vertices(*node)	
		price += vertices*count_area
		# print(plant(*next_plot), vertices)
		vertices=0
		count_area=1
		next_plot = next_plot_in_frontier(frontier, visited)
	print("The total price to put fences in the garden when counting plot sides is", price)


def print_garden():
	for line in garden:
		print(line)

def children(node):
	row,col = node
	adjacent_plots = []
	if row > 0:
		adjacent_plots.append((up(row,col)))
	if row < num_rows-1:
		adjacent_plots.append((down(row,col)))
	if col > 0:
		adjacent_plots.append((left(row,col)))
	if col < num_cols-1:
		adjacent_plots.append((right(row,col)))
	
	children = []
	for plot in adjacent_plots:
		if plant(*plot) == plant(*node):
			children.append(plot)
	return children

def next_plot_in_frontier(frontier, visited):
	for row in range(num_rows):
		for col in range(num_cols):
			if (row,col) not in visited:
				return row,col
	return None

def count_outer_vertices(row,col,current_plant):
	# outer vertex at B
	# ?A  A?  BA  AB
	# AB  BA  A?  ?A

	# outer vertex at B, valid edge cases
	# -- |A -- A| BA B| AB |B
	# AB |B BA B| -- A| -- |A

	vertices = 0
	left_different = False
	right_different = False
	down_different = False
	up_different = False

	if row == 0 or plant(*up(row,col)) != current_plant:
		up_different = True
	if row == num_rows-1 or plant(*down(row,col)) != current_plant:
		down_different = True
	if col == 0 or plant(*left(row,col)) != current_plant:
		left_different = True
	if col == num_cols-1 or plant(*right(row,col)) != current_plant:
		right_different = True

	if up_different and left_different:
		vertices += 1
	if up_different and right_different:
		vertices += 1
	if down_different and right_different:
		vertices += 1
	if down_different and left_different:
		vertices += 1

	return vertices

def count_inner_vertices(row,col,current_plant):
	# inner vertex at A
	# AA  AA  BA  AB
	# AB  BA  AA  AA
	
	# inner vertex at A, impossible to occur at edge
	# A|  AA  |A  --  
	# A|  --  |A  AA

	vertices = 0
	left_same = False
	right_same = False
	down_same = False
	up_same = False

	up_left_different = False
	up_right_different = False
	down_left_different = False
	down_right_different = False

	up_same = row > 0 and plant(*up(row,col)) == current_plant
	down_same = row < num_rows-1 and plant(*down(row,col)) == current_plant
	left_same = col > 0 and plant(*left(row,col)) == current_plant
	right_same = col < num_cols-1 and plant(*right(row,col)) == current_plant

	up_left_different = row > 0 and col > 0 and plant(*up_left(row,col)) != current_plant
	up_right_different = row > 0 and col < num_cols-1 and plant(*up_right(row,col)) != current_plant
	down_left_different = row < num_rows-1 and col > 0 and plant(*down_left(row,col)) != current_plant
	down_right_different = row < num_rows-1 and col < num_cols-1 and plant(*down_right(row,col)) != current_plant

	if up_same and left_same and up_left_different:
		vertices += 1
	if up_same and right_same and up_right_different:
		vertices += 1
	if down_same and left_same and down_left_different:
		vertices += 1
	if down_same and right_same and down_right_different:
		vertices += 1

	return vertices

def count_vertices(row,col):
	current_plant = plant(row,col)
	outer_vertices = count_outer_vertices(row,col,current_plant)
	inner_vertices = count_inner_vertices(row,col,current_plant)
	return outer_vertices + inner_vertices

def plant(row,col):
	return garden[row][col]

def up(row,col):
	return row-1,col

def down(row,col):
	return row+1,col

def left(row, col):
	return row,col-1

def right(row,col):
	return row,col+1

def up_left(row,col):
	return row-1,col-1

def up_right(row,col):
	return row-1, col+1

def down_left(row,col):
	return row+1,col-1

def down_right(row,col):
	return row+1,col+1

if __name__=="__main__":
	main()
