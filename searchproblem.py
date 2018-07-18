class SearchProblem:
	'''
	A wrapper class for defining a generic search problem
	Includes start state, goal test, and successor functions
	'''

	def __init__(self, start, goal, board):
		raise NotImplementedError()

	def getStartState(self):
		raise NotImplementedError()

	def isGoalState(self, state):
		raise NotImplementedError()

	def getSuccessors(self, state):
		raise NotImplementedError()

class BoardSearchProblem(SearchProblem):
	'''
	Any problem involving moving from point A to point B on the board
	State = (i,j) coordinate pair
	Goal = (i,j) coordinate pair
	Child = ((i,j), action, cost) triple
	'''

	def __init__(self, start, goal, board, passable_blocks):
		self.start = start
		self.goal = goal
		self.board = board
		self.passable_blocks = passable_blocks

	def getStartState(self):
		return self.start

	def isGoalState(self, state):
		return state == self.goal

	def getSuccessors(self, state):
		i,j = state
		children = []
		if i > 0:
			if self.board[i-1][j] in self.passable_blocks:
				children.append(((i-1,j),"North",1))
		if i < self.board.height-1:
			if self.board[i+1][j] in self.passable_blocks:
				children.append(((i+1,j),"South",1))
		if j > 0:
			if self.board[i][j-1] in self.passable_blocks:
				children.append(((i,j-1),"West",1))
		if j < self.board.width-1:
			if self.board[i][j+1] in self.passable_blocks:
				children.append(((i,j+1),"East",1))
		return children
