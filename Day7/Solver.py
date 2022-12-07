class Directory:
	def __init__(self, name, parent_dir=None):
		self.name = name
		self.items = []
		if parent_dir is not None:
			self.parent_dir = parent_dir
			
	def get_dir_by_name(self, dir_name):
		for item in self.items:
			if type(item) is not Directory:
				continue
			
			if item.name == dir_name:
				return item
		
		return None
		
	def get_dirs(self):
		result_arr = []
		for item in self.items:
			if type(item) is Directory:
				result_arr.append(item)
		return result_arr
		
	def identify_candidate_dirs(self, max_size):
		result = []
		all_dirs = self.get_dirs()
		
		for dir in all_dirs:
			if dir.get_size() < max_size:
				result.append(dir)
			result.extend(dir.identify_candidate_dirs(max_size))
			
		return result
		
	def generate_dir_structure_str(self, level=0):
		space_prefix = '  ' * (level)
		result_str = f'{space_prefix}- {str(self)}\n'
		
		for item in self.items:
			if type(item) is File:
				result_str += f'{space_prefix} - {str(item)}\n'
			else:
				result_str += item.generate_dir_structure_str(level+1)
				
		return result_str
		
	def get_all_dirs(self):
		result = [self]
		for dir in self.get_dirs():
			result.extend(dir.get_all_dirs())
		return result
		
	def get_size(self):
		total_size = 0
		
		for item in self.items:
			if type(item) is File:
				total_size += item.size
			else:
				total_size += item.get_size()
				
		return total_size
		
	def __str__(self):
		return f'{self.name} (dir , size={self.get_size()})'
		
	def __eq__(self, other):
		return self.name == other.name

class File:
	def __init__(self, name, size):
		self.name = name
		self.size = size
	
	def __str__(self):
		return f'{self.name} (file, size={self.size})'
	

class Solver:
	def solve_part_1(self, data, *args, **kwargs): # data is the raw lines from the file
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		
		self.root_dir = Directory('/')
		self.current_dir = self.root_dir
		
		self.parse_input(data[1:])
		
		result = 0
		for dir in self.root_dir.identify_candidate_dirs(100000):
			result += dir.get_size()
		return result
	
	def solve_part_2(self, data, *args, **kwargs):
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		
		self.root_dir = Directory('/')
		self.current_dir = self.root_dir
		
		self.parse_input(data[1:])
		
		total_disk_space = 70000000
		current_unused_disk_space = total_disk_space - self.root_dir.get_size()
		space_to_free = 30000000 - current_unused_disk_space
		
		all_dirs = self.root_dir.get_all_dirs()
		filtered_dirs = list(filter(lambda d: d.get_size() > space_to_free, all_dirs))
		filtered_dirs.sort(key=lambda d: d.get_size())
		
		return filtered_dirs[0].get_size()
		
	def parse_input(self, data):
		curr_index = 0
		
		while True:
			if curr_index >= len(data):
				break
			
			line = data[curr_index].strip()
			
			if 'cd' in line:
				self.parse_cd_command(line)
				curr_index += 1
			elif 'ls' in line:
				curr_index = self.parse_ls_command(data, curr_index)
				
	def parse_cd_command(self, command_line):
		command_param = command_line.split('$ cd ')[1]
			
		if command_param == '..':
			self.current_dir = self.current_dir.parent_dir
		else:
			self.current_dir = self.current_dir.get_dir_by_name(command_param)
			
	def parse_ls_command(self, data, command_index):
		i = command_index + 1
		
		while True:
			if i >= len(data):
				return i
		
			curr_line = data[i].strip()
			
			if curr_line[0] == '$':
				break
			
			if curr_line.split(' ')[0] != 'dir':
				file_size = int(curr_line.split(' ')[0])
				file_name = curr_line.split(' ')[1]
				self.current_dir.items.append(File(file_name, file_size))
			else:
				dir_name = curr_line.split('dir ')[1]
				self.current_dir.items.append(Directory(dir_name, self.current_dir))
			i += 1
		
		return i
			
			
			
			
			
			
			
			
				