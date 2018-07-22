class SearchProblem:
	'''
	A wrapper class for defining a generic search problem
	Includes start state, goal test, and successor functions
	'''

	# kwargs indicates that each type of problem will need to be initialized with different keyword arguments
	def __init__(self, **kwargs):
		self.expanded = 0
		self.expandedstates = []
		self.visualizeexpandedstates = False

	def getStartState(self):
		raise NotImplementedError()
	
	def getStartPos(self):
		return self.getPos(self.getStartState())

	def getPos(self, state):
		raise NotImplementedError()

	def getBoard(self):
		raise NotImplementedError()

	def isGoalState(self, state):
		raise NotImplementedError()

	def getSuccessors(self, state):
		self.expanded += 1
		self.expandedstates.append(state)

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
		super(BoardSearchProblem, self).__init__()
		self.start = start
		self.goal = goal
		self.board = board
		self.passable_blocks = passable_blocks

	def getStartState(self):
		return self.start

	def getPos(self, state):
		return state
	
	def getBoard(self):
		return self.board

	def isGoalState(self, state):
		return state == self.goal

	def getSuccessors(self, state):
		super(BoardSearchProblem, self).getSuccessors(state)
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

class NearestFoodProblem(SearchProblem):
	'''
	A helper class for problems about finding the nearest food
	State = (i,j) coordinate pair
	Goal = N/A
	Child = (state, action, cost) triple
	'''

	def __init__(self, start, board):
		super(NearestFoodProblem, self).__init__()
		self.start = start
		self.board = board
		self.passable_blocks = ["spot"]

	def getStartState(self):
		return self.start
	
	def getPos(self, state):
		return state

	def getBoard(self):
		return self.board

	def isGoalState(self, state):
		i,j = state
		return self.board.foodgrid[i][j]

	def getSuccessors(self, state):
		super(NearestFoodProblem, self).getSuccessors(state)
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
		super(EatAllFoodProblem, self).__init__()
		self.start = start
		self.board = board
		self.passable_blocks = ["spot"]

	def getStartState(self):
		return self.start
	
	def getPos(self, state):
		return state[0]

	def getBoard(self):
		return self.board

	def isGoalState(self, state):
		return state[1].isEmpty()

	def getSuccessors(self, state):
		super(EatAllFoodProblem, self).getSuccessors(state)
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

class CornersProblem(EatAllFoodProblem):
	'''
	A problem where Pacman must eat all the food pellets on the board
	State = (i,j) coordinate pair, boolean list of 4 corners visited [TopLeft, TopRight, BottomLeft, BottomRight]
	Goal = N/A
	Child = (state, action, cost) triple
	'''

	def __init__(self, start, board):
		super(EatAllFoodProblem, self).__init__()
		self.start = start
		self.board = board
		self.passable_blocks = ["spot"]
		self.corners = [(1,1), (1,board.width-2), (board.height-2,1), (board.height-2,board.width-2)]

	def getStartState(self):
		return self.start
	
	def getPos(self, state):
		return state[0]

	def getBoard(self):
		return self.board

	def isGoalState(self, state):
		return sum(state[1]) == 4

	def getSuccessors(self, state):
		super(EatAllFoodProblem, self).getSuccessors(state)
		i,j = state[0]
		children = []
		oldcorners = state[1]
		if i > 0:
			if self.board[i-1][j] in self.passable_blocks:
				newcorners = oldcorners
				if (i-1,j) == (1,1):
					newcorners = (True, oldcorners[1], oldcorners[2], oldcorners[3])
				elif (i-1,j) == (1,self.board.width-2):
					newcorners = (oldcorners[0], True, oldcorners[2], oldcorners[3])
				children.append((((i-1,j),newcorners),"North",1))
		if i < self.board.height-1:
			if self.board[i+1][j] in self.passable_blocks:
				newcorners = oldcorners
				if (i+1,j) == (self.board.height-2,1):
					newcorners = (oldcorners[0], oldcorners[1], True, oldcorners[3])
				elif (i+1,j) == (self.board.height-2,self.board.width-2):
					newcorners = (oldcorners[0], oldcorners[1], oldcorners[2], True)
				children.append((((i+1,j),newcorners),"South",1))
		if j > 0:
			if self.board[i][j-1] in self.passable_blocks:
				newcorners = oldcorners
				if (i,j-1) == (1,1):
					newcorners = (True, oldcorners[1], oldcorners[2], oldcorners[3])
				elif (i,j-1) == (self.board.height-2,1):
					newcorners = (oldcorners[0], oldcorners[1], True, oldcorners[3])
				children.append((((i,j-1),newcorners),"West",1))
		if j < self.board.width-1:
			if self.board[i][j+1] in self.passable_blocks:
				newcorners = oldcorners
				if (i,j+1) == (1,self.board.width-2):
					newcorners = (oldcorners[0], True, oldcorners[2], oldcorners[3])
				elif (i,j+1) == (self.board.height-2,self.board.width-2):
					newcorners = (oldcorners[0], oldcorners[1], oldcorners[2], True)
				children.append((((i,j+1),newcorners),"East",1))
		return children

	def hasWon(self, game):
		return game.board.isEmpty()