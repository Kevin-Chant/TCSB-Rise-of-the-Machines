import heapq
class Stack:
	def __init__(self):
		self.list = []

	def push(self, item):
		self.list.append(item)

	def pop(self):
		return self.list.pop()

	def isEmpty(self):
		return len(self.list) == 0

class Queue:
	def __init__(self):
		self.list = []

	def push(self, item):
		self.list.insert(0, item)

	def pop(self):
		return self.list.pop()

	def isEmpty(self):
		return len(self.list) == 0

class PriorityQueue:
	def __init__(self, eval_fx):
		self.fx = eval_fx
		self.list = []
		self.count = 0

	def push(self, item):
		entry = (self.fx(item), self.count, item)
		heapq.heappush(self.list, entry)
		self.count += 1

	def pop(self):
		(_,_,item) = heapq.heappop(self.list)
		return item

	def isEmpty(self):
		return len(self.list) == 0

class Board:
	def __init__(self, width=20, height=15, filled=False, house=False, maze=None):
		if not maze:
			self.grid = [["wall"]*width]
			if width < 3 or height < 3:
				raise ValueError("Width and height must both be at least 3")
			for i in range(height-2):
				self.grid.append(["wall"] + ["spot"]*(width-2) + ["wall"])
			self.grid.append(["wall"]*width)
			self.width = width
			self.height = height
		else:
			self.grid = maze
			self.width = len(maze[0])
			self.height = len(maze)

		self.hasGhosts = house

		self.foodgrid = [row.copy() for row in self.grid]
		for row in self.foodgrid:
			for i in range(len(row)):
				row[i] = False

		if filled:
			self.fill()

		if house:
			self.create_house()


	def __getitem__(self, i):
		return self.grid[i]

	def fill(self):
		for j in range(1,self.width-1):
			for i in range(1, self.height-1):
				if self.grid[i][j] == "spot":
					self.foodgrid[i][j] = True

	def fillcorners(self):
		for i,j in [(1,1), (1,self.width-2), (self.height-2, 1), (self.height-2, self.width-2)]:
			self.foodgrid[i][j] = True

	def create_house(self):
		if self.width < 10:
			raise ValueError("Cannot create house in board with less than 10 width")
		start = self.width//2-3
		end = self.width//2+3
		top = self.height//2-1
		middle = self.height//2
		bottom = self.height//2+1
		for j in range(start,start+2):
			self.grid[top][j] = "house"
		for j in range(start+2,start+4):
			self.grid[top][j] = "house_door"
		for j in range(start+4,end):
			self.grid[top][j] = "house"
		self.grid[middle][start] = "house"
		self.grid[middle][end-1] = "house"
		for j in range(start, end):
			self.grid[bottom][j] = "house"
		self.house_row = middle
		self.house_start = start+1
		
		for i in range(top,bottom+1):
			for j in range(start,end):
				self.foodgrid[i][j] = False

	def isEmpty(self):
		for row in self.foodgrid:
			for item in row:
				if item:
					return False
		return True

	def copy(self):
		newboard = Board(maze=self.grid, house=self.hasGhosts)
		newboard.foodgrid = [row.copy() for row in self.foodgrid]
		return newboard

def manhattan_distance(xy1, xy2):
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])