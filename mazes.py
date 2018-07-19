from util import Board
from searchproblem import *
tinymazegrid = [
			["wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "spot", "spot", "spot", "spot", "spot", "wall"],
			["wall", "spot", "wall", "wall", "wall", "spot", "wall"],
			["wall", "spot", "spot", "spot", "spot", "spot", "wall"],
			["wall", "wall", "wall", "wall", "wall", "spot", "wall"],
			["wall", "wall", "wall", "spot", "spot", "spot", "wall"],
			["wall", "spot", "spot", "spot", "wall", "wall", "wall"],
			["wall", "spot", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall"]
			]
tinymaze = Board(maze=tinymazegrid, house=False)
tinymazeproblem = BoardSearchProblem((1,5), (7,1), tinymaze, ["spot"])


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
regularmazeproblem = AdversarialEatAllFoodProblem(((1,1), regularmaze), regularmaze, [(regularmaze.house_row, regularmaze.house_start + i + 1) for i in range(0,4)])




hugemazegrid = [
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "spot", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "wall", "spot", "spot", "spot", "spot", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "spot", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "wall"],
			["wall", "spot", "wall", "wall", "wall", "wall", "wall", "wall", "spot", "spot", "wall", "wall", "wall", "wall", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "wall", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "spot", "wall", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "wall", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "spot", "spot", "wall", "spot", "wall", "wall"],
			["wall", "spot", "wall", "wall", "wall", "spot", "wall", "wall", "spot", "spot", "wall", "spot", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "spot", "wall", "wall", "wall", "wall", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "wall"],
			["wall", "spot", "spot", "spot", "wall", "spot", "wall", "spot", "spot", "spot", "wall", "spot", "wall", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "spot", "spot", "spot", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "spot", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			["wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall"],
			]
hugemaze = Board(maze=hugemazegrid, house=False)
hugemazeproblem = BoardSearchProblem((1,1), (7,1), hugemaze, ["spot"])
