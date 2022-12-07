class Solver:
	def solve_part_1(self, data): # data is the raw lines from the file
		total = 0
		for line in data:
			line = line.strip()
			split_line = line.split(',')
			first_pair = split_line[0]
			second_pair = split_line[1]
			
			first_range = int(first_pair.split('-')[0]), int(first_pair.split('-')[1])
			second_range = int(second_pair.split('-')[0]), int(second_pair.split('-')[1])
			
			if first_range[0] <= second_range[0] and first_range[1] >= second_range[1]:
				total += 1
				continue
				
			if second_range[0] <= first_range[0] and second_range[1] >= first_range[1]:
				total += 1
				continue
				
		return total
	
	def solve_part_2(self, data):
		total = 0
		for line in data:
			split_line = line.strip().split(',')
			
			first_pair = split_line[0]
			second_pair = split_line[1]
			
			first_range = range(int(first_pair.split('-')[0]), int(first_pair.split('-')[1]) + 1)
			second_range = range(int(second_pair.split('-')[0]), int(second_pair.split('-')[1]) + 1)
			
			if list(set(first_range) & set(second_range)):
				total += 1
			
		return total