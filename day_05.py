import csv

def main():	
	rules_dict = parse_rules()
	all_updates = parse_updates()
	correct_updates, corrected_updates = check_and_correct(rules_dict, all_updates)
	part_one(correct_updates)
	part_two(corrected_updates)

def check_and_correct(rules_dict, updates):
	correct_updates = []
	corrected_updates = []
	sorted_rule_keys = sorted(rules_dict, key=lambda key: len(rules_dict[key]), reverse=True)
	for update in updates:
		incorrect = False
		for rule_key in sorted_rule_keys:
			for comes_after in rules_dict[rule_key]:
				if (rule_key in update and comes_after in update 
					and update.index(comes_after) < update.index(rule_key)):
					incorrect = True
					del update[update.index(rule_key)]
					update.insert(update.index(comes_after),rule_key)
		if incorrect:
			corrected_updates.append(update)
		else:
			correct_updates.append(update)
	return correct_updates, corrected_updates

def sum_of_middles(updates):
	sum_of_middles = 0
	for update in updates:
		sum_of_middles += int(update[len(update)//2])
	return sum_of_middles

def part_one(correct_updates):
	print("Sum of middles of correct updates:", sum_of_middles(correct_updates))

def part_two(corrected_updates):
	print("Sum of middles of corrected updates:", sum_of_middles(corrected_updates))

def parse_rules():
	rules = [tuple(line.strip().split("|")) for line in open("aoc_5_rules.txt", "r").readlines()]
	rules.sort()
	rules_dict = dict()
	for rule in rules:
		if rule[0] not in rules_dict:
			rules_dict[rule[0]]={rule[1]}
		else:
			rules_dict[rule[0]].add(rule[1])
	return rules_dict

def parse_updates():
	csvfile = open('aoc_5_updates.csv')
	return [line for line in csv.reader(csvfile)]

if __name__=="__main__":
	main()
