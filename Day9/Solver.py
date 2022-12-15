from enum import Enum

class Directions(Enum):
	LEFT = (-1, 0)
	RIGHT = (1, 0)
	UP = (0, 1)
	DOWN = (0, -1)
	LEFT_UP = (-1, 1)
	RIGHT_UP = (1, 1)
	LEFT_DOWN = (-1, -1)
	RIGHT_DOWN = (1, -1)
	
class Knot:
	def __init__(self, name, parent=None, child=None):
		self.name = name
		self.x = 0
		self.y = 0
		
		self.child = child
		self.parent = parent
		
		if parent is not None:
			self.parent.child = self
		
		self.last_touching_direction = None
	
	def is_touching_parent(self):
		if self.x == self.parent.x and self.y == self.parent.y: # Knots are overlapping
			return True
		
		for dir in list(Directions):
			x_off, y_off = dir.value
			if self.parent.x == self.x + x_off and self.parent.y == self.y + y_off:
				self.last_touching_direction = dir
				return True
		
		return False
		
	def follow_parent(self):
		if self.is_touching_parent():
			return
			
		elif self.x == self.parent.x:
			self.y += -1 if self.parent.y - self.y < 0 else 1
		
		elif self.y == self.parent.y:
			self.x += -1 if self.parent.x - self.x < 0 else 1
			
		else:
			best_move = None
			best_distance = 5
			
			for dir in list(Directions):
				x_off, y_off = dir.value
				distance = abs(self.parent.x - (self.x + x_off)) + abs(self.parent.y - (self.y + y_off))
				
				if distance < best_distance:
					best_distance = distance
					best_move = dir
				
			self.x += best_move.value[0]
			self.y += best_move.value[1]
			
		if self.child is not None:
			self.child.follow_parent()
	
	def move_knot(self, direction):
		x_off, y_off = direction.value
		
		self.x += x_off
		self.y += y_off
		
		self.child.follow_parent()
		
	def move_instruct(self, direction, amount):
		for i in range(amount):
			self.move_knot(direction)

class Solver:
	def solve_part_1(self, data, *args, **kwargs): # data is the raw lines from the file
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		
		self.direction_map = {
			'R': Directions.RIGHT,
			'U': Directions.UP,
			'L': Directions.LEFT,
			'D': Directions.DOWN,
		}
		
		self.parse_instructions(data)
		
		head = Knot('root')
		tail = Knot('tail', parent=head)
		tail_visits = [(0,0)]
		
		for direction, amount in self.move_instructs:
			for i in range(amount):
				head.move_knot(direction)
				tail_pos = (tail.x, tail.y)
			
				if tail_pos not in tail_visits:
					tail_visits.append(tail_pos)
		
		return len(tail_visits)
	
	def parse_instructions(self, data):
		self.move_instructs = []
		
		for line in data:
			line = line.strip()
			letter, amount = line.split(' ')
			self.move_instructs.append((self.direction_map[letter], int(amount)))
	
	def solve_part_2(self, data, *args, **kwargs):
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		
		self.direction_map = {
			'R': Directions.RIGHT,
			'U': Directions.UP,
			'L': Directions.LEFT,
			'D': Directions.DOWN,
		}
		
		self.parse_instructions(data)
		
		head = Knot('root')
		
		current_knot = head
		
		for i in range(9):
			new_knot = Knot(str(i+1), parent=current_knot)
			current_knot.child = new_knot
			
			current_knot = new_knot
		
		tail = current_knot
		tail_visits = [(0,0)]
		
		for direction, amount in self.move_instructs:
			for i in range(amount):
				head.move_knot(direction)
				tail_pos = (tail.x, tail.y)
			
				if tail_pos not in tail_visits:
					tail_visits.append(tail_pos)
		
		return len(tail_visits)
		
		
		