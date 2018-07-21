import pygame
from pygame.locals import *
import random
import sys
from search import *
from searchproblem import *
from mazes import *
from util import *
from autopacman import *


class Entity:
	# Entity interface:
	# i,j coordinates on the grid
	# img image to render at i,j

	def draw(self, screen, x, y):
		screen.blit(self.img, (x, y))

class Pacman(Entity):
	def __init__(self,i,j,game):
		self.i = i
		self.j = j
		self.img = pygame.image.load("imgs/pacman.png")
		self.direction = None
		self.passable_blocks = ["spot", "ghost"]
		self.blocktype = "pacman"
		self.isAI = False
		self.current_block = "spot"

	def draw(self, screen, x, y):
		img = self.img
		if self.direction == "North":
			img = pygame.transform.rotate(img, 90)
		elif self.direction == "West":
			img = pygame.transform.rotate(img, 180)
		elif self.direction == "South":
			img = pygame.transform.rotate(img, 270)
		screen.blit(img, (x,y))

class Ghost(Entity):
	def __init__(self,i,j,name):
		self.i = i
		self.j = j
		self.img = pygame.image.load("imgs/" + name + ".png")
		self.name = name
		self.direction = None
		self.passable_blocks = ["spot", "house_door", "pacman"]
		self.blocktype = "ghost"
		self.isAI = True
		self.current_block = "spot"

	def draw(self, screen, x, y):
		img = self.img
		if self.direction == "West":
			img = pygame.transform.flip(img, True, False)
		screen.blit(img, (x,y))

	def AI(self, game):
		start = (self.i, self.j)
		target = (game.player.i, game.player.j)
		search_problem = BoardSearchProblem(start, target, game.board, self.passable_blocks)
		path_to_target = breadth_first_search(search_problem)
		if path_to_target:
			self.direction = path_to_target[0]
		else:
			self.direction = None
		# self.direction = random.choice(["North", "South", "East", "West", None])


board_colors = {"wall": (64, 96, 191),
				"spot": (0, 0, 0),
				"house": (77, 51, 153),
				"house_door": (159, 140, 217),
				"food": (255, 255, 255)
			}
bg_color = (0,0,0)

class App:
	def __init__(self, food=True, problem=None, agent=None, heuristic=None):
		self._running = True
		self.screen = None
		if not problem:
			self.problem = regularmazeproblem
		else:
			self.problem = problem
		self.board = self.problem.getBoard()
		
		self.board_offset = (0,100)
		self.spot_size = 40
		self.size = self.width, self.height = self.spot_size * self.board.width + self.board_offset[0], self.spot_size * self.board.height + self.board_offset[1]

		if not agent:
			agent = Pacman

		if heuristic and agent != Pacman:
			self.player = agent(*self.problem.getStartPos(), self, heuristic=heuristic)
		else:
			self.player = agent(*self.problem.getStartPos(), self)

		self.score = 0
		self.tickcounter = 0
		self.entities = [self.player]
		self.ghosts = []

		self.clock = pygame.time.Clock()

		if self.board.hasGhosts:
			for j,ghost in enumerate(["inky", "blinky", "pinky", "clyde"]):
				g = Ghost(self.board.house_row,self.board.house_start + j,ghost)
				self.entities.append(g)
				self.ghosts.append(g)

	def on_init(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running = True
 
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_F4 and (pygame.key.get_pressed()[K_LALT] or pygame.key.get_pressed()[K_RALT]):
				self._running = False
			elif event.key == pygame.K_LEFT and not self.player.isAI:
				self.player.direction = "West"
			elif event.key == pygame.K_RIGHT and not self.player.isAI:
				self.player.direction = "East"
			elif event.key == pygame.K_UP and not self.player.isAI:
				self.player.direction = "North"
			elif event.key == pygame.K_DOWN and not self.player.isAI:
				self.player.direction = "South"

	def on_loop(self):
		self.clock.tick(60)
		self.tickcounter += 1
		self.tickcounter %= 60
		if self.tickcounter%10 == 0:
			for entity in self.entities:
				if entity.isAI:
					entity.AI(self)
				if entity.direction:
					next_spot = [entity.i, entity.j]
					if entity.direction == "North":
						next_spot[0] -= 1
					elif entity.direction == "South":
						next_spot[0] += 1
					elif entity.direction == "East":
						next_spot[1] += 1
					elif entity.direction == "West":
						next_spot[1] -= 1
					if self.board[next_spot[0]][next_spot[1]] in entity.passable_blocks:
						self.board[entity.i][entity.j] = entity.current_block
						entity.i, entity.j = next_spot
						entity.current_block = self.board[next_spot[0]][next_spot[1]]
						self.board[next_spot[0]][next_spot[1]] = entity.blocktype
			if self.board.foodgrid[self.player.i][self.player.j]:
				self.score += 1
				self.board.foodgrid[self.player.i][self.player.j] = False
			for ghost in self.ghosts:
				if self.player.i == ghost.i and self.player.j == ghost.j:
					print("You lose!")
					self.score -= 100
					print("Final score: " + str(self.score))
					exit(0)
			if self.problem.hasWon(self):
				print("You win!")
				print("Final score: " + str(self.score))
				exit(0)


	def render_board(self):
		for i in range(self.board.height):
			for j in range(self.board.width):
				item = self.board[i][j]
				x,y = self.convert_ij_to_xy(i,j)
				if item in board_colors and not self.board.foodgrid[i][j]:
					rect = pygame.Rect(x, y, self.spot_size, self.spot_size)
					pygame.draw.rect(self.screen, board_colors[item], rect)
				elif self.board.foodgrid[i][j]:
					rect = pygame.Rect(x+3*self.spot_size//8, y+3*self.spot_size//8, self.spot_size//4, self.spot_size//4)
					pygame.draw.rect(self.screen, board_colors["food"], rect)

	def convert_ij_to_xy(self, i ,j):
		x,y = self.board_offset
		return (x+j*self.spot_size, y+i*self.spot_size)

	def on_render(self):
		self.screen.fill(bg_color)
		self.render_board()
		for entity in self.entities:
			entity.draw(self.screen, *self.convert_ij_to_xy(entity.i,entity.j))
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
 
def main(**kwargs):
	theApp = App(problem=kwargs.get("problem",None),agent=kwargs.get("agent",None),heuristic=kwargs.get("heuristic",None))
	theApp.on_execute()

if __name__ == "__main__" :
	# Keyword arguments expected:
	# -maze=mazename
	# -agent=agentname
	# -heuristic=heuristicname
	kwargs = {}
	if len(sys.argv) > 1:
		for arg in sys.argv[1:]:
			if "-maze=" in arg:
				kwargs["problem"] = eval(arg.split("=")[1] + "problem")
			elif "-agent=" in arg:
				kwargs["agent"] = eval(arg.split("=")[1])
			elif "-heuristic=" in arg:
				kwargs["heuristic"] = eval(arg.split("=")[1] + "_heuristic")
	main(**kwargs)