disk_map = [int(x) for x in list(open("aoc_9.txt", "r").read())]

def main():	
	part_one()
	part_two()

def part_one():
	i = 2
	j = len(disk_map)-1
	id_left = 1
	id_right = len(disk_map)//2

	free_space = disk_map[1]
	file_size_right = disk_map[j]

	final_position = disk_map[0]
	checksum = 0
	checksum_str = ""

	while i < j:
		while free_space > 0:
			checksum += final_position * id_right
			checksum_str += str(final_position) + "*" + str(id_right) + " + "
			final_position += 1
			free_space -= 1
			file_size_right -= 1
			if file_size_right == 0:
				id_right -= 1
				j -= 2
				file_size_right = disk_map[j]

		if id_left < id_right:
			file_size_left = disk_map[i]
			free_space = disk_map[i+1]
			while file_size_left > 0:
				checksum += final_position * id_left
				checksum_str += str(final_position) + "*" + str(id_left) + " + "
				final_position += 1
				file_size_left -= 1

			id_left += 1
			i += 2

	while file_size_right > 0:
		checksum += final_position * id_right
		checksum_str += str(final_position) + "*" + str(id_right) + " + "
		final_position += 1
		file_size_right -= 1

	# print(checksum_str[:-2])
	print("The checksum of the compacted file is", checksum)


def part_two():
	
	free_dict = {}
	file_dict = {}
	id = 0
	i = 0
	disk_position = 0

	while i < len(disk_map):
		file_space = disk_map[i]
		file_dict[disk_position] = (file_space, id)
		disk_position += file_space
		i += 1
		id += 1
		if i < len(disk_map):
			free_space = disk_map[i]
			free_dict[disk_position] = free_space
			disk_position += free_space
			i += 1

	# print("Original disk:", visualize_part_two(file_dict, free_dict))

	file_dict_iterator = file_dict.copy()
	for file_position in reversed(file_dict_iterator):
		file_space_end = file_dict[file_position][0]
		file_id_end = file_dict[file_position][1]

		free_keys = list(sorted(free_dict))
		for free_position in free_keys:
			free_space = free_dict[free_position]
			if free_space >= file_space_end and free_position < file_position:
				del file_dict[file_position]
				file_dict[free_position] = (file_space_end, file_id_end)
				free_dict[file_position] = file_space_end
				del free_dict[free_position]
				free_space -= file_space_end
				free_position += file_space_end
				free_dict[free_position] = free_space
				break

	free_dict_keys = sorted(free_dict)
	file_dict_keys = sorted(file_dict)

	# print("Compacted disk:", visualize_part_two(file_dict, free_dict))
	print("The checksum of the compacted file with the new method is", checksum_part_two(file_dict))

def visualize_part_two(file_dict, free_dict):
	result_viz = ""
	for i in range(sum(disk_map)):
		if i in file_dict:
			result_viz += str(file_dict[i][1])*file_dict[i][0]
		elif i in free_dict:
			result_viz += "."*free_dict[i]
	return result_viz

def checksum_part_two(file_dict):
	checksum = 0
	i = 0
	while i < sum(disk_map):
		if i in file_dict:
			id = file_dict[i][1]
			size = file_dict[i][0]
			for j in range(size):
				checksum += i*id
				i+= 1
		else:
			i+=1
	return checksum


if __name__=="__main__":
	main()
