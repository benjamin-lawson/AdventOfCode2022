from DataLoader import DataLoader
import sys
import importlib


class DayRunner:
	def __init__(self, day_dir, solver):
		self.day_dir = day_dir
		self.solver = solver
	
	def RunTestData(self):
		print('===== Test Data =====')
		test_data = DataLoader.LoadTestData(self.day_dir)
		print('Part 1')
		print(self.solver.solve_part_1(test_data, test_data=True))
		
		print('Part 2')
		print(self.solver.solve_part_2(test_data, test_data=True))
		print('')
		
	def RunData(self):
		print('===== Real Data =====')
		data = DataLoader.LoadData(self.day_dir)
		print('Part 1')
		print(self.solver.solve_part_1(data, test_data=False))
		
		print('Part 2')
		print(self.solver.solve_part_2(data, test_data=False))
		
		print('')
		
def main():
	if '--day' not in sys.argv:
		print('ERROR: --day argument must be specified!')
		return

	day_arg_index = sys.argv.index('--day') + 1
	day_dir = 'Day' + sys.argv[day_arg_index]
	
	if '--new-day' in sys.argv:
		new_day_path = DataLoader.CreateNewDay(day_dir)
		if new_day_path is not None:
			print(f'New day started at ({new_day_path})')
		return
		
	
	solver = importlib.import_module(f'{day_dir}.Solver')
	
	runner = DayRunner(day_dir, solver.Solver())
	runner.RunTestData()
	runner.RunData()

if __name__ == '__main__':
	main()
	