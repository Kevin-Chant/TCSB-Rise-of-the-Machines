import random
from pacman import Pacman
from searchproblem import *
from search import *

class AutoPacman(Pacman):
	'''
	An AI controlled pacman
	The AI interface has any entity with isAI = True call their AI() method once per loop
	'''
	def __init__(self,i,j,game):
		super(AutoPacman, self).__init__(i,j,game)
		self.isAI = True

	def AI(self, game):
		self.direction = None

class GoWestPacman(AutoPacman):
	'''
	The simplest AI which simply goes West
	'''
	def __init__(self,i,j,game):
		super(GoWestPacman, self).__init__(i,j,game)

	def AI(self, game):
		self.direction = "West"

class RandomPacman(AutoPacman):
	'''
	Another simple AI which chooses its moves randomly
	'''
	def __init__(self,i,j,game):
		super(RandomPacman, self).__init__(i,j,game)

	def AI(self, game):
		self.direction = random.choice(["North", "South", "East", "West", None])

class TinyMazePacman(AutoPacman):
	'''
	Contains the hardcoded solution to the tiny maze
	'''
	def __init__(self, i, j, game):
		super(TinyMazePacman, self).__init__(i,j,game)
		self.directionIndex = 0
		self.directions = ["South", "South", "South", "South", "West", "West", "South", "West", "West", "South"]
	
	def AI(self, game):
		self.direction = self.directions[self.directionIndex]
		self.directionIndex += 1

class BFSPacman(AutoPacman):
	'''
	Searches for the optimal path to the target (only works for mazes where the problem is a BoardSearchProblem)
	'''
	def __init__(self, i, j, game):
		super(BFSPacman, self).__init__(i,j,game)
	
	def AI(self, game):
		if not isinstance(game.problem, BoardSearchProblem):
			self.direction = None
		else:
			start = (self.i, self.j)
			target = game.problem.goal
			search_problem = BoardSearchProblem(start, target, game.board, self.passable_blocks)
			path_to_target = breadth_first_search(search_problem)
			if path_to_target:
				self.direction = path_to_target[0]
			else:
				self.direction = None

class UCSPacman(AutoPacman):
	'''
	Searches for the optimal path to the target (only works for mazes where the problem is a BoardSearchProblem)
	'''
	def __init__(self, i, j, game):
		super(UCSPacman, self).__init__(i,j,game)
	
	def AI(self, game):
		if not isinstance(game.problem, BoardSearchProblem):
			self.direction = None
		else:
			start = (self.i, self.j)
			target = game.problem.goal
			search_problem = BoardSearchProblem(start, target, game.board, self.passable_blocks)
			path_to_target = ucs(search_problem)
			if path_to_target:
				self.direction = path_to_target[0]
			else:
				self.direction = None

class AstarPacman(AutoPacman):
	'''
	Searches for the optimal path to the target (only works for mazes where the problem is a BoardSearchProblem)
	'''
	def __init__(self, i, j, game, heuristic=null_heuristic):
		super(AstarPacman, self).__init__(i,j,game)
		self.heuristic = null_heuristic
	
	def AI(self, game):
		if not isinstance(game.problem, BoardSearchProblem):
			self.direction = None
		else:
			start = (self.i, self.j)
			target = game.problem.goal
			search_problem = BoardSearchProblem(start, target, game.board, self.passable_blocks)
			path_to_target = Astar(search_problem, self.heuristic)
			if path_to_target:
				self.direction = path_to_target[0]
			else:
				self.direction = None