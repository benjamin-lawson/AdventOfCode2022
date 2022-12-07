import string

class Solver:
	def intersection(self, lst1, lst2):
		return [value for value in lst1 if value in lst2]
		
	def intersection_three(self, lst1, lst2, lst3):
		return [value for value in lst1 if value in lst2 if value in lst3]
		
	def letter_value(self, letter):
		return string.ascii_letters.index(letter) + 1

	def solve_part_1(self, data): # data is the raw lines from the file
		total = 0
		for line in data:
			line = line.strip()
			half = int(len(line)/2)
			inter_letter = self.intersection(line[0:half], line[half:len(line)])[0]
			total += self.letter_value(inter_letter)
		return total
		
	
	def solve_part_2(self, data):
		total = 0
		
		for i in range(0, len(data), 3):
			inter_letter = self.intersection_three(data[i].strip(), data[i+1].strip(), data[i+2].strip())[0]
			total += self.letter_value(inter_letter)
		
		return total