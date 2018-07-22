import pygame
from pygame.locals import *

pygame.font.init()
titlefont = pygame.font.SysFont('Arial', 60)
menufont = pygame.font.SysFont('Arial', 30)

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

def empty_grid():
	return [["","",""],["","",""],["","",""]]

class App:
	def __init__(self):
		self._running = True
		self.screen = None
		self.size = self.width, self.height = 600, 600
		self.grid = empty_grid()
		self.player = "x"
		self.difficulty = 1
		self.menu = True
		self.gameover = False
		self.waitcounter = 0
		self.clock = pygame.time.Clock()
		self.message = None

	def on_init(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running = True


	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			x,y = pygame.mouse.get_pos()
			if self.menu:
				if x > 225 and x < 375:
					if y > 100 and y < 175:
						self.menu = False
					if y > 400 and y < 475:
						self._running = False
				if x > 125 and x < 275:
					if y > 250 and y < 325:
						self.difficulty = 1
				if x > 325 and x < 475:
					if y > 250 and y < 325:
						self.difficulty = 4
			else:
				if not self.gameover:
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
							self.message = "You Win!"
							self.gameover=True
							self.grid = empty_grid()
							return
						if is_tie(self.grid):
							self.message = "Cat's game"
							self.gameover=True
							self.grid = empty_grid()
							return
						self.grid = minimax(self.grid, other(self.player), self.difficulty)
						if is_win(self.grid, other(self.player)):
							self.message = "You Lose!"
							self.gameover=True
							self.grid = empty_grid()
							return
						if is_tie(self.grid):
							self.message = "Cat's game"
							self.gameover=True
							self.grid = empty_grid()
							return


	def on_loop(self):
		self.clock.tick(60)
		if self.gameover:
			self.waitcounter += 1
			if self.waitcounter == 60 * 4:
				self.waitcounter = 0
				self.gameover = False
				self.menu = True
				self.message = None

	def on_render(self):
		self.screen.fill((255,255,255))
		if not self.menu:
			if self.message:
				messagesurface = titlefont.render(self.message, False, (0,0,0))
				self.screen.blit(messagesurface, (self.width//2 - messagesurface.get_width()//2, self.height//2 - messagesurface.get_height()//2))
			else:
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
		else:
			titlesurface = titlefont.render("Tic Tac Toe", False, (0,0,0))
			self.screen.blit(titlesurface, (180, 10))
			# Play button
			pygame.draw.rect(self.screen, (200,200,200), (225, 100, 150, 75))
			playsurface = menufont.render("Play", False, (0,0,0))
			self.screen.blit(playsurface, (280,120))
			# Regular difficulty
			pygame.draw.rect(self.screen, (100,200,100), (125, 250, 150, 75))
			playsurface = menufont.render("Regular", False, (0,0,0))
			self.screen.blit(playsurface, (150,270))
			# Impossible difficulty
			pygame.draw.rect(self.screen, (200,100,100), (325, 250, 150, 75))
			playsurface = menufont.render("Impossible", False, (0,0,0))
			self.screen.blit(playsurface, (350,270))
			# Quit button
			pygame.draw.rect(self.screen, (200,200,200), (225, 400, 150, 75))
			playsurface = menufont.render("Quit", False, (0,0,0))
			self.screen.blit(playsurface, (280,420))
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