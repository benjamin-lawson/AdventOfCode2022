class Solver:
	def solve_part_1(self, data, *args, **kwargs): # data is the raw lines from the file
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		return self.parse_data_for_start_packet(data, 4)
	
	def solve_part_2(self, data, *args, **kwargs):
		self.test = kwargs['test_data'] if 'test_data' in kwargs else False
		return self.parse_data_for_start_packet(data, 14)
		
	def parse_data_for_start_packet(self, data, packet_size):
		for i in range(len(data[0]) - (packet_size-1)):
			if len(set(data[0][i:i+packet_size])) == packet_size:
				return i+packet_size