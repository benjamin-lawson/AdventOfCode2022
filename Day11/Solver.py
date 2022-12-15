from enum import Enum
from math import floor
import copy

def add(param1, param2):
	return param1 + param2
	
def subtract(param1, param2):
	return param1 - param2
	
def multiply(param1, param2):
	return param1 * param2

def divide(param1, param2):
	return param1 / param2

class Monkey:
	def __init__(self, name):
		self.name = name
		self.items_interacted = 0
	
	def accept_item_from_monkey(self, item):
		self.items.append(item)
		
	def run_test(self, item):
		return item % self.test_div == 0
		
	def perform_worry_op(self, item):
		start_worry = item
		param2 = start_worry if self.worry_op_param_2 == 'OLD' else self.worry_op_param_2
		return self.worry_op(start_worry, param2)
		
	def run(self, part_1, monkey_mod=1):
		copy_items = copy.deepcopy(self.items)
		
		for i in range(len(copy_items)):
			self.items_interacted += 1
			worry_val = copy_items[i]
			
			worry_op_val = self.perform_worry_op(worry_val)
			if not part_1:
				worry_op_val = worry_op_val % monkey_mod
				
			if part_1:
				worry_op_val = worry_op_val // 3
				
			test_res = self.run_test(worry_op_val)
			is_val = 'is' if test_res else 'is not'
			monkey_to_throw_to = self.test_monkey_true if test_res else self.test_monkey_false
			monkey_to_throw_to.accept_item_from_monkey(worry_op_val)
			self.items.remove(worry_val)
			
			
	def __str__(self):
		items_str = ', '.join([str(x) for x in self.items])
		return f'{self.name}: {items_str}'

class Solver:
	worry_op_char_map = {
		'+': add,
		'-': subtract,
		'*': multiply,
		'/': divide,
	}
	
	def solve_part_1(self, data, *args, **kwargs): # data is the raw lines from the file
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		self.parse_data(data)
		
		for i in range(20):
			for m in self.monkeys:
				m.run(True)
		
		items_interact = []
		for m in self.monkeys:
			items_interact.append((m, m.items_interacted))
			
		items_interact.sort(key=lambda x: x[1], reverse=True)
		return items_interact[0][1] * items_interact[1][1]
	
	def solve_part_2(self, data, *args, **kwargs):
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		self.parse_data(data)
		
		for i in range(10000):
			for m in self.monkeys:
				m.run(False, self.monkey_mod)
		
		items_interact = []
		for m in self.monkeys:
			items_interact.append((m, m.items_interacted))
			
		items_interact.sort(key=lambda x: x[1], reverse=True)
		return items_interact[0][1] * items_interact[1][1]
		
	def parse_data(self, data):
		self.monkeys = []
		curr_monkey = None
		self.monkey_mod = 1
		
		monkey_pass_true = []
		monkey_pass_false = []
		
		
		for line in data:
			line = line.strip()
			line_name = line.split(':')[0]
			
			if 'Monkey' in line_name:
				name = line.split(':')[0]
				curr_monkey = Monkey(name)
				self.monkeys.append(curr_monkey)
				
			elif 'Starting items' in line_name:
				items = [int(x) for x in line.split('Starting items: ')[1].split(', ')]
				curr_monkey.items = items
				
			elif 'Operation' in line_name:
				line_split = line.split('Operation: new = ')[1].upper().split(' ')
				worry_op = Solver.worry_op_char_map[line_split[1]]
				param2 = line_split[2]
				
				curr_monkey.worry_op = worry_op
				curr_monkey.worry_op_param_2 = 'OLD' if param2 == 'OLD' else int(param2)
				
			elif 'Test' in line_name:
				test_div = int(line.split('Test: divisible by ')[1])
				self.monkey_mod *= test_div
				curr_monkey.test_div = test_div
				
			elif 'If true' in line_name:
				monkey_if_true_index = int(line.split('If true: throw to monkey ')[1])
				monkey_pass_true.append(monkey_if_true_index)
				
			elif 'If false' in line_name:
				monkey_if_false_index = int(line.split('If false: throw to monkey ')[1])
				monkey_pass_false.append(monkey_if_false_index)
				
		for i in range(len(self.monkeys)):
			self.monkeys[i].test_monkey_true = self.monkeys[monkey_pass_true[i]]
			self.monkeys[i].test_monkey_false = self.monkeys[monkey_pass_false[i]]
				