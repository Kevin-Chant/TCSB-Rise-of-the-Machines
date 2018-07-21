import pygame
from pygame.locals import *
 
def is_win(grid, player):
	for row in range(3):
		if grid[row] == [player,player,player]:
			return True
	for column in range(3):
		threeinarow = True
		for row in range(3):
			if grid[row][column] != player:
				threeinarow = False
		if threeinarow:
			return True
	if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
		return True
	if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
		return True
	return False

def is_tie(grid):
	for row in range(3):
		for column in range(3):
			if grid[row][column] == "":
				return False
	return True

def get_successors(grid, player):
	successors = []
	for row in range(3):
		for column in range(3):
			if grid[row][column] == "":
				copy = [row.copy() for row in grid]
				copy[row][column] = player
				successors.append(copy)
	return successors

def evaluation_function(grid):
	if is_win(grid, "x"):
		return 1
	if is_win(grid, "o"):
		return 0
	return 0.5

def other(player):
	if player == "x":
		return "o"
	else:
		return "x"

player_functions = {'x': max, 'o': min}

def value(grid, player, depth, maxdepth):
	if is_win(grid, player) or is_win(grid, other(player)) or is_tie(grid) or depth >= maxdepth:
		return evaluation_function(grid)
	comparison = player_functions[player]
	children = get_successors(grid, player)
	child_values = []
	for i in range(len(children)):
		child_values.append(value(children[i], other(player), depth+1, maxdepth))
	return comparison(child_values)

def minimax(grid, player, maxdepth):
	if is_win(grid, player) or is_win(grid, other(player)) or is_tie(grid):
		raise ValueError("Cannot choose next best move when game has terminated")
	comparison = player_functions[player]
	children = get_successors(grid, player)
	child_values = []
	for i in range(len(children)):
		child_values.append(value(children[i], other(player), 0, maxdepth))
	bestvalue = comparison(child_values)
	return children[child_values.index(bestvalue)]	

class App:
	def __init__(self):
		self._running = True
		self.screen = None
		self.size = self.weight, self.height = 600, 600
		self.grid = [["","",""],["","",""],["","",""]]
		self.player = "x"
		self.difficulty = 4
 
	def on_init(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running = True


	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			x,y = pygame.mouse.get_pos()
			i,j = 0,0
			if x < 200:
				j = 0
			elif x > 400:
				j = 2
			else:
				j = 1
			if y < 200:
				i = 0
			elif y > 400:
				i = 2
			else:
				i = 1
			if self.grid[i][j] == "":
				self.grid[i][j] = self.player
				if is_win(self.grid, self.player):
					print("You win!")
					exit(0)
				if is_tie(self.grid):
					print("Cat's game!")
					exit(0)
				self.grid = minimax(self.grid, other(self.player), self.difficulty)
				if is_win(self.grid, other(self.player)):
					print("You lose!")
					exit(0)
				if is_tie(self.grid):
					print("Cat's game!")
					exit(0)


	def on_loop(self):
		pass
	def on_render(self):
		self.screen.fill((255,255,255))
		pygame.draw.line(self.screen, (0,0,0), (200,0), (200,600))
		pygame.draw.line(self.screen, (0,0,0), (400,0), (400,600))
		pygame.draw.line(self.screen, (0,0,0), (0,200), (600,200))
		pygame.draw.line(self.screen, (0,0,0), (0,400), (600,400))
		for row in range(3):
			for col in range(3):
				if self.grid[row][col] == "o":
					pygame.draw.circle(self.screen, (0,0,0), (col*200+100, row*200+100), 75, 1)
				if self.grid[row][col] == "x":
					pygame.draw.line(self.screen, (0,0,0), (col*200-53+100, row*200-53+100), (col*200+53+100,row*200+53+100))
					pygame.draw.line(self.screen, (0,0,0), (col*200+53+100, row*200-53+100), (col*200-53+100,row*200+53+100))
		pygame.display.update()
	
	def on_cleanup(self):
		pygame.quit()
 
	def on_execute(self):
		if self.on_init() == False:
			self._running = False
 
		while( self._running ):
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()
 
if __name__ == "__main__" :
	theApp = App()
	theApp.on_execute()