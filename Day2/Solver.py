from enum import Enum

class GameState(Enum):
	PLAYER_WIN = 6
	TIE = 3
	PLAYER_LOSE = 0
	
class GameMove(Enum):
	ROCK = 1
	PAPER = 2
	SCISSORS = 3

class Solver:
	def __init__(self):
		self.victories = {
			GameMove.ROCK: [GameMove.SCISSORS],
			GameMove.PAPER: [GameMove.ROCK],
			GameMove.SCISSORS: [GameMove.PAPER],
		}
		
		self.defeats = {
			GameMove.ROCK: [GameMove.PAPER],
			GameMove.PAPER: [GameMove.SCISSORS],
			GameMove.SCISSORS: [GameMove.ROCK],
		}
		
		self.moves = {
			'A': GameMove.ROCK,
			'B': GameMove.PAPER,
			'C': GameMove.SCISSORS,
			'X': GameMove.ROCK,
			'Y': GameMove.PAPER,
			'Z': GameMove.SCISSORS,
		}
		
		self.end_state = {
			'X': GameState.PLAYER_LOSE,
			'Y': GameState.TIE,
			'Z': GameState.PLAYER_WIN
		}
	
	def solve_part_1(self, data): # data is the raw lines from the file
		total_score = 0
		
		for line in data:
			game_split = line.strip().split(' ')
			
			computer_input = self.moves[game_split[0]]
			player_input = self.moves[game_split[1]]
			
			game_state = self.play_rps(computer_input, player_input)
			
			score = self.score_game(game_state, player_input)
			total_score += score
			
		return total_score
	
	def solve_part_2(self, data):
		total_score = 0
		
		for line in data:
			game_split = line.strip().split(' ')
			
			computer_input = self.moves[game_split[0]]
			desired_result = self.end_state[game_split[1]]
			
			player_input = self.determine_rps_play(computer_input, desired_result)
			
			score = self.score_game(desired_result, player_input)
			total_score += score
		
		return total_score
	
	def play_rps(self, computer_input, player_input):
		if player_input == computer_input:
			return GameState.TIE
		
		defeats = self.victories[player_input]
		
		if computer_input in defeats:
			return GameState.PLAYER_WIN
		else:
			return GameState.PLAYER_LOSE
			
	def determine_rps_play(self, computer_input, desired_result):
		if desired_result == GameState.TIE:
			return computer_input
		elif desired_result == GameState.PLAYER_WIN:
			return self.defeats[computer_input][0]
		else:
			return self.victories[computer_input][0]
		
	
	def score_game(self, game_state, player_input):
		return int(game_state.value) + int(player_input.value)
		
		