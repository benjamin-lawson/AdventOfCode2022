class Solver:
	def solve_part_1(self, data): # data is the raw lines from the file
		elves_carrying = {}
		elf_count = 0
		
		for line in data:
			if line.strip() == '':
				elf_count += 1
				continue
			
			if elf_count not in elves_carrying:
				elves_carrying[elf_count] = 0
			
			elves_carrying[elf_count] += int(line.strip())
		
		sorted_elves = dict(sorted(elves_carrying.items(), key=lambda item: item[1], reverse=True))
		
		return elves_carrying[list(sorted_elves.keys())[0]]
	
	def solve_part_2(self, data):
		elves_carrying = {}
		elf_count = 0
		
		for line in data:
			if line.strip() == '':
				elf_count += 1
				continue
			
			if elf_count not in elves_carrying:
				elves_carrying[elf_count] = 0
			
			elves_carrying[elf_count] += int(line.strip())
		
		sorted_elves = dict(sorted(elves_carrying.items(), key=lambda item: item[1], reverse=True))
		
		return elves_carrying[list(sorted_elves.keys())[0]] + elves_carrying[list(sorted_elves.keys())[1]] + elves_carrying[list(sorted_elves.keys())[2]]