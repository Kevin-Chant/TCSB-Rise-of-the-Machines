from util import *
from searchproblem import *

class Node:
	def __init__(self, state, path):
		self.state = state
		self.path = path

	def __getitem__(self, item):
		if item == "state":
			return self.state
		if item == "path":
			return self.path
		else:
			raise KeyError("Invalid key given, Nodes only have a state and a path")

def general_search(problem, fringe):
	fringe.push(Node(problem.getStartState(), []))
	closed = set()
	while True:
		if fringe.isEmpty():
			return None
		node = fringe.pop()
		if problem.isGoalState(node["state"]):
			return node["path"]
		if node["state"] not in closed:
			closed.add(node["state"])
			children = problem.getSuccessors(node["state"])
			for child,action,cost in children:
				fringe.push(Node(child,node["path"] + [action]))

def depth_first_search(problem):
	fringe = Stack()
	return general_search(problem, fringe)

def breadth_first_search(problem):
	fringe = Queue()
	return general_search(problem, fringe)

def ucs(problem):
	fringe = PriorityQueue(lambda node: len(node["path"]))
	return general_search(problem, fringe)

def Astar(problem, heuristic):
	fringe = PriorityQueue(lambda node: len(node["path"]) + heuristic(node, problem))
	return general_search(problem, fringe)

def null_heuristic(node, problem):
	return 0

def euclidean_heuristic(node, problem):
	if isinstance(problem, BoardSearchProblem):
		return abs(node["state"][0]-problem.goal[0]) + abs(node["state"][1]-problem.goal[1])
	else:
		return 0