stones = [int(x) for x in open("aoc_11.txt", "r").read().split(" ")]
count_cache_retrievals = 0
cache = dict()

def main():	
	part_one()
	part_two()

def part_one():
	blinks = 25
	global stones
	for i in range(blinks):
		new_stones = []
		for index, stone in enumerate(stones):
			if stone == 0:
				new_stones.append(1)
			elif len(str(stone)) % 2 == 0:
				stone_1 = int(str(stone)[:len(str(stone))//2])
				stone_2 = int(str(stone)[len(str(stone))//2:])
				new_stones += [stone_1,stone_2]
			else:
				new_stones.append(stone*2024)
		stones = new_stones
	print("There are", len(stones), "stones after", blinks, "blinks.")

def part_two():
	stones = [int(x) for x in open("aoc_11.txt", "r").read().split(" ")]
	global count_cache_retrievals
	blinks = 75
	num_stones = 0
	for i in stones:
		num_stones += blink(i, blinks)
	print("There are", num_stones, "stones after", blinks, "blinks.")
	print("This solution used", count_cache_retrievals, "cache retrievals!")

#given the value on a stone and the number of blinks, return the total number of stones after expansion
def blink(stone, num_blinks):
	num_stones = 1
	global cache
	global count_cache_retrievals
	if (stone,num_blinks) in cache:
		count_cache_retrievals += 1
		return cache[(stone,num_blinks)]
	if num_blinks == 0:
		return num_stones
	elif stone == 0:
		num_stones = blink(1, num_blinks-1)
	elif len(str(stone)) % 2 == 0:
		stone_1 = int(str(stone)[:len(str(stone))//2])
		stone_2 = int(str(stone)[len(str(stone))//2:])
		num_stones = blink(stone_1, num_blinks-1) + blink(stone_2, num_blinks-1)
	else:
		num_stones = blink(stone*2024, num_blinks-1)
	cache[(stone,num_blinks)] = num_stones
	return num_stones

if __name__=="__main__":
	main()
