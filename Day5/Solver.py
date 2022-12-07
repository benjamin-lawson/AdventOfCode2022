class Solver:
	def solve_part_1(self, data, *args, **kwargs): # data is the raw lines from the file
		self.test = kwargs['test_data'] if 'test_data' in kwargs else True
		self.generate_box_stacks()
		self.parse_instruction_input(data)
		self.run_sim_part_1()
		result = ''
		for box in self.box_stacks:
			result += box[-1]
		return result
		
	def generate_box_stacks(self):
		if self.test:
			box_strings = [
				'Z N',
				'M C D',
				'P'
			]
		else:
			box_strings = [
				'H B V W N M L P',
				'M Q H',
				'N D B G F Q M L',
				'Z T F Q M W G',
				'M T H P',
				'C B M J D H G T',
				'M N B F V R',
				'P L H M R G S',
				'P D B C N'
			]
			
		self.box_stacks = [s.split(' ') for s in box_strings]
		
	def visualize_box_stacks(self):
		sb_arr = []
		max_count = 0
		for box_stack in self.box_stacks:
			max_count = max(len(box_stack), max_count)
		
		for i in range(max_count):
			stack_row = ''
			for box in self.box_stacks:
				try:
					stack_row += f' [{box[i]}] '
				except IndexError:
					stack_row += '     '
					continue
			sb_arr.append(stack_row)
		
		sb_arr.reverse()
		sb_arr.append('')
		
		stack_count = 3 if self.test else 9
		num_row = ''
		for i in range(stack_count):
			num_row += f'  {i+1}  '
		sb_arr.append(num_row)
			
		print('\n'.join(sb_arr))
			
	def parse_instruction_input(self, data):
		instruction_start = 0
		for i in range(len(data)):
			if data[i].strip() == '':
				instruction_start = i+1
				break
		
		instruction_strs = [s.strip() for s in data[instruction_start:]]
		instructions = []
		for instruct_str in instruction_strs:
			num_to_move = int(instruct_str.split('move ')[1].split(' from')[0])
			stack_to_move_from = int(instruct_str.split('from ')[1].split(' to')[0]) - 1
			stack_to_move_to = int(instruct_str.split('to ')[1]) - 1
			instructions.append((num_to_move, stack_to_move_from, stack_to_move_to))
		self.instructions = instructions
	
	def run_sim_part_1(self):
		for instruct in self.instructions:
			for i in range(instruct[0]):
				self.box_stacks[instruct[2]].append(self.box_stacks[instruct[1]].pop())
			
	
	def solve_part_2(self, data, *args, **kwargs):
		self.test = kwargs['test_data'] if 'test_data' in kwargs else True
		self.generate_box_stacks()
		self.parse_instruction_input(data)
		self.run_sim_part_2()
		result = ''
		for box in self.box_stacks:
			result += box[-1]
		return result
		
	def run_sim_part_2(self):
		for instruct in self.instructions:
			num_to_move = instruct[0]
			stack_to_move_from = self.box_stacks[instruct[1]]
			stack_to_move_to = self.box_stacks[instruct[2]]
			
			boxes_to_move = stack_to_move_from[len(stack_to_move_from) - num_to_move:len(stack_to_move_from)]
			
			for box in boxes_to_move:
				stack_to_move_to.append(box)
				
			self.box_stacks[instruct[1]] = stack_to_move_from[:len(stack_to_move_from) - num_to_move]






