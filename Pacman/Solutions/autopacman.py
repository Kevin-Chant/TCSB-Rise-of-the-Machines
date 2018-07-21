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
		self.directions = []
		self.directionIndex = 0

	def AI(self, game):
		if self.directionIndex >= len(self.directions):
			self.direction=None
		else:
			self.direction = self.directions[self.directionIndex]
			self.directionIndex += 1

class GoWestPacman(AutoPacman):
	'''
	The simplest AI which simply goes West
	'''
	def __init__(self,i,j,game):
		super(GoWestPacman, self).__init__(i,j,game)
		self.directions = ["West"] * 100


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
		self.directions = ["South", "South", "South", "South", "West", "West", "South", "West", "West", "South"]
	

class BFSPacman(AutoPacman):
	'''
	Searches for the optimal path to the target (only works for mazes where the problem is a BoardSearchProblem)
	'''
	def __init__(self, i, j, game):
		super(BFSPacman, self).__init__(i,j,game)
		if not isinstance(game.problem, BoardSearchProblem):
			self.directions = []
		else:
			path_to_target = breadth_first_search(game.problem)
			if path_to_target:
				self.directions = path_to_target
			else:
				self.directions = []
	

class UCSPacman(AutoPacman):
	'''
	Searches for the optimal path to the target (only works for mazes where the problem is a BoardSearchProblem)
	'''
	def __init__(self, i, j, game):
		super(UCSPacman, self).__init__(i,j,game)
		if not isinstance(game.problem, BoardSearchProblem):
			self.directions = []
		else:
			path_to_target = ucs(game.problem)
			if path_to_target:
				self.directions = path_to_target
			else:
				self.directions = []
	

class AStarPacman(AutoPacman):
	'''
	Searches for the optimal path to the target (only works for mazes where the problem is a BoardSearchProblem)
	'''
	def __init__(self, i, j, game, heuristic=null_heuristic):
		super(AStarPacman, self).__init__(i,j,game)
		startnode = Node((1,1),[])
		if not isinstance(game.problem, BoardSearchProblem) and not isinstance(game.problem, EatAllFoodProblem):
			self.directions = []
		else:
			path_to_target = Astar(game.problem, heuristic)
			if path_to_target:
				self.directions = path_to_target
			else:
				self.directions = []

class GreedyFoodPacman(AutoPacman):
	'''
	Greedily searches for the nearest food
	'''
	def __init__(self, i, j, game, heuristic=null_heuristic):
		super(GreedyFoodPacman, self).__init__(i,j,game)
		self.directionIndex = 0
		if not isinstance(game.problem, EatAllFoodProblem):
			self.directions = []
		else:
			path_to_target = greedySearch(game.problem, heuristic)
			if path_to_target:
				self.directions = path_to_target
			else:
				self.directions = []




