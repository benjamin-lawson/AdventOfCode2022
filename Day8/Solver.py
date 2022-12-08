class Solver:
	def solve_part_1(self, data, *args, **kwargs): # data is the raw lines from the file
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		self.parse_input(data)
		#self.print_forest()
		
		total = 0
		for y in range(len(self.forest)):
			for x in range(len(self.forest[0])):
				total += int(self.is_tree_visible(x, y))
		return total
		
	def parse_input(self, data):
		self.forest = []
		for line in data:
			line = line.strip()
			new_row = [int(x) for x in line]
			self.forest.append(new_row)
		
	def is_tree_visible(self, x, y):
		if x == len(self.forest[0])-1 or y == len(self.forest)-1 or x == 0 or y == 0:
			return True
			
		if self.is_tree_visible_left(x, y):
			return True
			
		if self.is_tree_visible_up(x, y):
			return True
			
		if self.is_tree_visible_right(x, y):
			return True
			
		if self.is_tree_visible_down(x, y):
			return True
		
		return False
		
	def is_tree_visible_left(self, x, y):
		tree_height = self.forest[y][x]
		for i in range(x-1, -1, -1):
			if self.forest[y][i] >= tree_height:
				return False
		return True
		
	def is_tree_visible_right(self, x, y):
		tree_height = self.forest[y][x]
		for i in range(x+1, len(self.forest[0])):
			if self.forest[y][i] >= tree_height:
				return False
		return True
		
	def is_tree_visible_up(self, x, y):
		tree_height = self.forest[y][x]
		for i in range(y-1, -1, -1):
			if self.forest[i][x] >= tree_height:
				return False
		return True
		
	def is_tree_visible_down(self, x, y):
		tree_height = self.forest[y][x]
		for i in range(y+1, len(self.forest)):
			if self.forest[i][x] >= tree_height:
				return False
		return True
	
	def print_forest(self):
		sb = ''
		for i in range(len(self.forest)):
			sb += f'{i} | '
			sb += ''.join([str(x) for x in self.forest[i]])
			sb += '\n'
		
		sb += '    -----\n'
		sb += '    '
		for i in range(len(self.forest[0])):
			sb += f'{i}'
		print(sb)
		
	def solve_part_2(self, data, *args, **kwargs):
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		self.parse_input(data)
		#self.print_forest()
		
		max_score = -1
		
		for y in range(len(self.forest)):
			for x in range(len(self.forest[0])):
				max_score = max(max_score, self.get_scenic_score(x,y))
			
		return max_score
		
		
	def get_scenic_score(self, x, y):
		if x == 0 or y == 0 or x == len(self.forest[0])-1 or y == len(self.forest)-1:
			return 0
			
		up_score = self.get_scenic_score_up(x,y)
		left_score = self.get_scenic_score_left(x,y)
		right_score = self.get_scenic_score_right(x,y)
		down_score = self.get_scenic_score_down(x,y)
		
		return left_score * right_score * up_score * down_score
		
	def get_scenic_score_left(self, x, y):
		tree_height = self.forest[y][x]
		score = 0
		
		for i in range(x-1, -1, -1):
			score += 1
			if self.forest[y][i] >= tree_height:
				break
			
		return score
	
	def get_scenic_score_right(self, x, y):
		tree_height = self.forest[y][x]
		score = 0
		
		for i in range(x+1, len(self.forest[0])):
			score += 1
			if self.forest[y][i] >= tree_height:
				break
			
		return score
	
	def get_scenic_score_up(self, x, y):
		tree_height = self.forest[y][x]
		score = 0
		
		for i in range(y-1, -1, -1):
			score += 1
			if self.forest[i][x] >= tree_height:
				break
			
		return score
	
	def get_scenic_score_down(self, x, y):
		tree_height = self.forest[y][x]
		score = 0
		
		for i in range(y+1, len(self.forest)):
			score += 1
			if self.forest[i][x] >= tree_height:
				break
			
		return score
	
		