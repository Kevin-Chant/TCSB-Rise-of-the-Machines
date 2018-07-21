from util import *
from searchproblem import *

class Node:
	def __init__(self, state, info):
		self.state = state
		self.info = info

	def __getitem__(self, item):
		if item == 0 or item == "state":
			return self.state
		if item == 1 or item == "info":
			return self.info
		else:
			raise KeyError("Invalid key. Key can choose from (0,1), (state,info), or more specific keys for types of nodes")

class BoardSearchNode(Node):

	def __getitem__(self, item):
		if item == "state":
			return self.state
		if item == "path":
			return self.path
		else:
			return super(BoardSearchNode,Node).__getitem__(item)

def general_search(problem, fringe):
	fringe.push(Node(problem.getStartState(), []))
	closed = set()
	expanded = 0
	while True:
		if fringe.isEmpty():
			return None
		node = fringe.pop()
		if problem.isGoalState(node["state"]):
			return node["info"]
		if node["state"] not in closed:
			closed.add(node["state"])
			expanded += 1
			children = problem.getSuccessors(node["state"])
			for child,action,cost in children:
				fringe.push(Node(child,node["info"] + [action]))

def depth_first_search(problem):
	fringe = Stack()
	return general_search(problem, fringe)

def breadth_first_search(problem):
	fringe = Queue()
	return general_search(problem, fringe)

def ucs(problem):
	fringe = PriorityQueue(lambda node: len(node["info"]))
	return general_search(problem, fringe)

def Astar(problem, heuristic):
	fringe = PriorityQueue(lambda node: len(node["info"]) + heuristic(node, problem))
	return general_search(problem, fringe)

def greedySearch(problem, heuristic):
	fringe = PriorityQueue(lambda node: heuristic(node, problem))
	return general_search(problem, fringe)

def null_heuristic(node, problem):
	return 0

def euclidean_heuristic(node, problem):
	if isinstance(problem, BoardSearchProblem):
		return abs(node["state"][0]-problem.goal[0]) + abs(node["state"][1]-problem.goal[1])
	else:
		return 0

def euclideancorner_heuristic(node, problem):
	if isinstance(problem, CornersProblem):
		i,j = node["state"][0]
		dist = 0
		if i < problem.board.height//2:
			dist += i-1
		else:
			dist += problem.board.height-2-i
		if j < problem.board.width//2:
			dist += j-1
		else:
			dist += problem.board.width-2-j
		return dist
	else:
		return 0

def euclideanfood_heuristic(node, problem):
	if isinstance(problem, NearestFoodProblem):
		i,j = node["state"]
		for r1 in range(problem.board.height):
			if i-r1 > 0:
				for r2 in range(problem.board.width):
					if j-r2 > 0:
						if problem.board.foodgrid[i-r1][j-r2]:
							return r1+r2
					if j+r2 < problem.board.width-1:
						if problem.board.foodgrid[i-r1][j+r2]:
							return r1+r2

			if i+r1 < problem.board.height-1:
				for r2 in range(problem.board.width):
					if j-r2 > 0:
						if problem.board.foodgrid[i+r1][j-r2]:
							return r1+r2
					if j+r2 < problem.board.width-1:
						if problem.board.foodgrid[i+r1][j+r2]:
							return r1+r2

	return 0

def bfsfood_heuristic(node, problem):
	if isinstance(problem, NearestFoodProblem):
		problem = NearestFoodProblem(node["state"], problem.board)
		return len(breadth_first_search(problem))
	else:
		return 0