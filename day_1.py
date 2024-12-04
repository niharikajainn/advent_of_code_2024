import csv

def main():		
	part_one()
	part_two()

def parse():
	csvfile = open('aoc_1.csv')
	return csv.reader(csvfile, delimiter = ' ')

def part_one():
	list_1 = []
	list_2 = []

	for row in parse():
		list_1.append(row[0])
		list_2.append(row[1])

	list_1.sort()
	list_2.sort()

	distance = 0

	for x in range(len(list_1)):
		distance += abs(int(list_2[x]) - int(list_1[x])) 

	print("The total distance between the two lists is", str(distance)+".")

def part_two():
	list_1 = []
	dict_2 = dict()

	for row in parse():
		list_1.append(row[0])
		if(row[1] in dict_2):
			dict_2[row[1]]+= 1
		else:
			dict_2[row[1]] = 1

	sim_score = 0

	for x in list_1:
		if x in dict_2:
			sim_score += int(x) * dict_2[x] 

	print("The similarity score between the two lists is", str(sim_score)+".")

if __name__=="__main__":
    main()
