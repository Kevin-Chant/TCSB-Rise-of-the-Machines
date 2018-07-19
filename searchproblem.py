class SearchProblem:
	'''
	A wrapper class for defining a generic search problem
	Includes start state, goal test, and successor functions
	'''

	# kwargs indicates that each type of problem will need to be initialized with different keyword arguments
	def __init__(self, **kwargs):
		raise NotImplementedError()

	def getStartState(self):
		raise NotImplementedError()
	
	def getStartPos(self):
		raise NotImplementedError()

	def getBoard(self):
		raise NotImplementedError()

	def isGoalState(self, state):
		raise NotImplementedError()

	def getSuccessors(self, state):
		raise NotImplementedError()

	def hasWon(self, game):
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
	
	def getStartPos(self):
		return self.start
	
	def getBoard(self):
		return self.board

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

	def hasWon(self, game):
		state = (game.player.i, game.player.j)
		return self.isGoalState(state)

class EatAllFoodProblem(SearchProblem):
	'''
	A problem where Pacman must eat all the food pellets on the board
	State = (i,j) coordinate pair, current board
	Goal = N/A
	Child = (state, action, cost) triple
	'''

	def __init__(self, start, board):
		self.start = start
		self.board = board
		self.passable_blocks = ["spot"]

	def getStartState(self):
		return self.start
	
	def getStartPos(self):
		return self.start[0]

	def getBoard(self):
		return self.board

	def isGoalState(self, state):
		return state[1].isEmpty()

	def getSuccessors(self, state):
		i,j = state[0]
		children = []
		if i > 0:
			if self.board[i-1][j] in self.passable_blocks:
				newboard = state[1].copy()
				newboard[i-1][j] = False
				children.append((((i-1,j),newboard),"North",1))
		if i < self.board.height-1:
			if self.board[i+1][j] in self.passable_blocks:
				newboard = state[1].copy()
				newboard[i+1][j] = False
				children.append((((i+1,j),newboard),"South",1))
		if j > 0:
			if self.board[i][j-1] in self.passable_blocks:
				newboard = state[1].copy()
				newboard[i][j-1] = False
				children.append((((i,j-1),newboard),"West",1))
		if j < self.board.width-1:
			if self.board[i][j+1] in self.passable_blocks:
				newboard = state[1].copy()
				newboard[i][j+1] = False
				children.append((((i,j+1),newboard),"East",1))
		return children

	def hasWon(self, game):
		return game.board.isEmpty()

class AdversarialEatAllFoodProblem(EatAllFoodProblem):
	'''
	A modified form of the EatAllFoodProblem where Pacman must deal with ghosts
	State = (i,j) coordinate pair, current board, and list of ghost positions
	Goal = N/A
	Child = (state, action, cost) triple
	'''

	def __init__(self, start, board, ghost_starts):
		self.start = start
		self.board = board
		self.passable_blocks = ["spot", "ghost"]

	def getStartState(self):
		return self.start
	
	def getStartPos(self):
		return self.start[0]

	def getBoard(self):
		return self.board

	def isGoalState(self, state):
		return state[1].isEmpty()

	def getSuccessors(self, state):
		i,j = state[0]
		children = []
		if i > 0:
			if self.board[i-1][j] in self.passable_blocks:
				newboard = state[1].copy()
				newboard[i-1][j] = False
				children.append((((i-1,j),newboard, state[2]),"North",1))
		if i < self.board.height-1:
			if self.board[i+1][j] in self.passable_blocks:
				newboard = state[1].copy()
				newboard[i+1][j] = False
				children.append((((i+1,j),newboard, state[2]),"South",1))
		if j > 0:
			if self.board[i][j-1] in self.passable_blocks:
				newboard = state[1].copy()
				newboard[i][j-1] = False
				children.append((((i,j-1),newboard, state[2]),"West",1))
		if j < self.board.width-1:
			if self.board[i][j+1] in self.passable_blocks:
				newboard = state[1].copy()
				newboard[i][j+1] = False
				children.append((((i,j+1),newboard, state[2]),"East",1))
		return children

	def hasWon(self, game):
		return game.board.isEmpty()