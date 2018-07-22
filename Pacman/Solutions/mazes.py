from util import Board
from searchproblem import *
from search import *

def maze_generator(pattern):
	def other(spot):
		if spot == "spot":
			return "wall"
		return "spot"

	grid = []
	for row in pattern:
		grid.append([])
		current = row[0]
		for i in range(1,len(row)):
			grid[-1]+=[current]*row[i]
			current = other(current)
		if len(grid[-1]) != len(grid[0]):
			print("Pattern was set with len " + str(len(grid[0])) + ". Generated row " + str(len(grid)) + " with length " + str(len(grid[-1])))
	return grid

tinymazepattern = [
					["wall", 7],
					["wall", 1, 5, 1],
					["wall", 1, 1, 3, 1, 1],
					["wall", 1, 5, 1],
					["wall", 5, 1, 1],
					["wall", 3, 3, 1],
					["wall", 1, 3, 3],
					["wall", 1, 1, 5],
					["wall", 7]
					]


tinymazegrid = maze_generator(tinymazepattern)
tinymaze = Board(maze=tinymazegrid, house=False)
tinymazeproblem = BoardSearchProblem((1,5), (7,1), tinymaze, ["spot"])

tinycornersgrid = 	[
					["wall", "wall", "wall", "wall", "wall", "wall", "wall"],
					["wall", "spot", "spot", "spot", "spot", "spot", "wall"],
					["wall", "spot", "wall", "spot", "wall", "spot", "wall"],
					["wall", "spot", "spot", "spot", "spot", "spot", "wall"],
					["wall", "spot", "wall", "spot", "wall", "spot", "wall"],
					["wall", "spot", "spot", "spot", "spot", "spot", "wall"],
					["wall", "wall", "wall", "wall", "wall", "wall", "wall"],
					]
tinycorners = Board(maze=tinycornersgrid, house=False)
tinycorners.fillcorners()
tinycornerstart = ((3,3),(False, False, False, False))
tinycornersproblem = CornersProblem(tinycornerstart,tinycorners)


smallfoodgrid = [
				["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
				["wall", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "wall"],
				["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
				]
smallfood = Board(maze=smallfoodgrid, house=False)
smallfoodstart = ((1,4),smallfood)
smallfood.foodgrid[1][1] = True
smallfoodproblem = EatAllFoodProblem(smallfoodstart, smallfood)



smallmazegrid = [
				["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
				["wall", "spot", "spot", "spot", "spot", "spot", "wall", "spot", "spot", "spot", "spot", "spot", "wall", "spot", "spot", "spot", "spot", "spot", "wall"],
				["wall", "spot", "wall", "wall", "wall", "spot", "wall", "spot", "wall", "wall", "wall", "spot", "wall", "spot", "wall", "wall", "wall", "spot", "wall"],
				["wall", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "wall"],
				["wall", "spot", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "spot", "wall"],
				["wall", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "wall"],
				["wall", "spot", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "spot", "wall"],
				["wall", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "wall"],
				["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
				]
smallmaze = Board(maze=smallmazegrid, house=False, filled=True)
smallmazeproblem = EatAllFoodProblem(((7,1), smallmaze), smallmaze)

regularmaze = Board(filled=True, house=True)
regularmazeproblem = EatAllFoodProblem(((1,1), regularmaze), regularmaze)

heuristictestpattern = [
						["wall", 10],
						["wall", 1,8,1],
						["wall", 10],
						]
heuristictestgrid = maze_generator(heuristictestpattern)
heuristictest = Board(maze=heuristictestgrid, house=False)
heuristictestproblem = BoardSearchProblem((1,4), (1,8), heuristictest, ["spot"])


hugemazepattern = [
			["wall", 19, 1, 21],
			["wall", 1, 23, 1, 7, 1, 3, 1, 3, 1],
			["wall", 1,1,10,1,10,1,1,1,5,1,3,1,1,1,3],
			["wall", 1,1,1,7,1,5,1,5,1,3,1,3,1,5,1,3,1],
			["wall", 1,1,1,1,5,1,3,1,3,1,3,1,3,1,1,1,1,1,9,1,1],
			["wall", 1,1,1,5,1,5,1,3,1,1,1,5,1,1,1,9,1,1,1],
			["wall", 1,1,13,1,3,1,3,1,3,1,5,1,3,1,1,1,1],
			["wall", 1,3,1,11,1,5,1,1,1,3,1,5,1,1,1,3,1],
			["wall", 3,1,1,1,13,1,3,1,1,1,3,1,5,1,5],
			["wall", 1,3,1,7,1,3,1,3,1,3,1,3,1,7,1,3,1],
			["wall", 1,1,9,1,1,1,3,1,3,1,5,1,5,1,3,1,1,1,1],
			["wall", 1,1,1,5,1,1,1,1,1,9,1,5,1,3,1,3,1,1,1,1,1],
			["wall", 1,1,1,1,3,1,1,1,1,1,9,1,1,1,3,1,3,1,5,1,3],
			["wall", 1,1,1,3,1,5,1,7,1,3,1,3,1,3,1,7,1],
			["wall", 1,1,3,1,9,1,9,1,3,1,5,1,3,1,1],
			["wall", 1,1,1,1,1,9,1,13,1,7,1,1,1,1,1],
			["wall", 1,1,1,1,9,1,1,1,11,1,3,1,5,1,1,1,1],
			["wall", 1,1,1,5,1,1,1,3,1,1,1,5,1,3,1,5,1,5,1,1,1],
			["wall", 1,1,3,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,7,1,1,1,3,1,1,1,1],
			["wall", 1,5,1,3,1,7,1,1,1,1,1,9,1,3,1,3,1],
			["wall", 19,1,21]
			]
hugemazegrid = maze_generator(hugemazepattern)
hugemaze = Board(maze=hugemazegrid, house=False)
hugemazeproblem = BoardSearchProblem((0,19), (20,19), hugemaze, ["spot"])
