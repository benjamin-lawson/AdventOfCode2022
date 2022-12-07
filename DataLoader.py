import os
import shutil


class DataLoader:
	@staticmethod
	def LoadTestData(day_dir):
		day_dir_path = os.path.join(os.getcwd(), day_dir)
		path = os.path.join(day_dir_path, 'testdata.txt')
		if not os.path.isfile(path):
			print(f'ERROR: No data file found at ({path})')
			return None
		
		with open(path, 'r') as data_file:
			return data_file.readlines()
	
	@staticmethod
	def LoadData(day_dir):
		day_dir_path = os.path.join(os.getcwd(), day_dir)
		path = os.path.join(day_dir_path, 'data.txt')
		if not os.path.isfile(path):
			print(f'ERROR: No data file found at ({path})')
			return None
		
		with open(path, 'r') as data_file:
			return data_file.readlines()
	
	@staticmethod
	def CreateNewDay(day_dir):
		day_dir_path = os.path.join(os.getcwd(), day_dir)
		
		if not os.path.exists(day_dir_path):
			os.mkdir(day_dir_path)
		else:
			print(f'ERROR: {day_dir} already exists!')
			return None
		
		shutil.copyfile(os.path.join('Template', '__init__.py'), os.path.join(day_dir_path, '__init__.py'))
		shutil.copyfile(os.path.join('Template', 'SolverTemplate.txt'), os.path.join(day_dir_path, 'Solver.py'))
		shutil.copyfile(os.path.join('Template', 'data.txt'), os.path.join(day_dir_path, 'data.txt'))
		shutil.copyfile(os.path.join('Template', 'testdata.txt'), os.path.join(day_dir_path, 'testdata.txt'))
		
		return day_dir_path