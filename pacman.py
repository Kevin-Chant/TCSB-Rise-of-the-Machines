import pygame
from pygame.locals import *
from search import *
from searchproblem import *

class Board:
    def __init__(self, width=20, height=15, filled=False, house=False):
        self.grid = [["wall"]*width]
        if width < 3 or height < 3:
            raise ValueError("Width and height must both be at least 3")
        for i in range(height-2):
            self.grid.append(["wall"] + ["spot"]*(width-2) + ["wall"])
        self.grid.append(["wall"]*width)
        self.width = width
        self.height = height

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

class Entity:
    # Entity interface:
    # i,j coordinates on the grid
    # img image to render at i,j

    def draw(self, screen, x, y):
        screen.blit(self.img, (x, y))

class Pacman(Entity):
    def __init__(self,i,j):
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


board_colors = {"wall": (64, 96, 191),
                "spot": (0, 0, 0),
                "house": (77, 51, 153),
                "house_door": (159, 140, 217),
                "food": (255, 255, 255)
                }
bg_color = (0,0,0)

class App:
    def __init__(self, ghosts=True):
        self._running = True
        self.screen = None
        self.board = Board(filled=True, house=ghosts)
        self.board_offset = (0,100)
        self.spot_size = 40
        self.size = self.width, self.height = self.spot_size * self.board.width + self.board_offset[0], self.spot_size * self.board.height + self.board_offset[1]
        self.player = Pacman(1,1)
        self.score = 0
        self.tickcounter = 0
        self.entities = [self.player]
        self.ghosts = []
        if ghosts:
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
            if event.key == pygame.K_LEFT:
                self.player.direction = "West"
            elif event.key == pygame.K_RIGHT:
                self.player.direction = "East"
            elif event.key == pygame.K_UP:
                self.player.direction = "North"
            elif event.key == pygame.K_DOWN:
                self.player.direction = "South"

    def on_loop(self):
        self.tickcounter += 1
        self.tickcounter %= 60
        if self.tickcounter%30 == 0:
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
            if self.board.isEmpty():
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
 
if __name__ == "__main__" :
    clock = pygame.time.Clock()
    clock.tick(60)
    theApp = App()
    theApp.on_execute()