from enum import Enum

class InstructionType(Enum):
	ADDX = 1
	NOOP = 2

class CPU:
	def __init__(self, instructs):
		self.x = 1
		self.cycle_num = 0
		self.x_history = []
		self.instructions = instructs
		self.crt_rows = ['']
		self.curr_crt_row = 0
				
	def run_all_instructions(self):
		for instruct, val in self.instructions:
			if instruct == InstructionType.NOOP:
				self.noop()
			else:
				self.addx(val)
	
	def addx(self, val):
		self.cycle_num += 1
		self.x_history.append(self.x)
		self.add_to_crt_row()
		
		self.cycle_num += 1
		self.x_history.append(self.x)
		self.add_to_crt_row()

		self.x += val
	
	def noop(self):
		self.cycle_num += 1
		self.x_history.append(self.x)
		self.add_to_crt_row()
		
	def add_to_crt_row(self):
		if self.cycle_num % 40 in (self.x % 40, (self.x + 1) % 40, (self.x + 2) % 40):
			self.crt_rows[self.curr_crt_row] += '#'
		else:
			self.crt_rows[self.curr_crt_row] += '.'
			
		if self.cycle_num % 40 == 0:
				self.crt_rows.append('')
				self.curr_crt_row  += 1

class Solver:
	def __init__(self):
		self.instruction_map = {
			'addx': InstructionType.ADDX,
			'noop': InstructionType.NOOP,
		}
	
	def solve_part_1(self, data, *args, **kwargs): # data is the raw lines from the file
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		self.parse_instructions(data)
		cpu_sim = CPU(self.instructions)
		cpu_sim.run_all_instructions()
		
		result = 0
		
		for i in range(19, len(cpu_sim.x_history), 40):
			cycle = i + 1
			result += cycle * cpu_sim.x_history[i]
		
		return result
	
	def solve_part_2(self, data, *args, **kwargs):
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		self.parse_instructions(data)
		cpu_sim = CPU(self.instructions)
		cpu_sim.run_all_instructions()
		
		for line in cpu_sim.crt_rows:
			print('')
			print(' '.join(line))
			
		return ''
		
	def parse_instructions(self, data):
		self.instructions = []
		
		for line in data:
			line = line.strip()
			if line.split(' ')[0] == 'noop':
				self.instructions.append((InstructionType.NOOP, 0))
			elif line.split(' ')[0] == 'addx':
				self.instructions.append((InstructionType.ADDX, int(line.split(' ')[1])))
			else:
				print(f'ERROR: Found incompatible line! {line}')