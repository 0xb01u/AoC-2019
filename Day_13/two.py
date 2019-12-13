# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 13

# Care package
import sys
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

arcade = Intcomputer(list(map(int, open("game_free.txt", "r").read().split(","))))

sprites = { 0: ' ', 1: '|', 2: '█', 3: '_', 4: 'O'}

empty = []
wall = []
block = []
paddle = []
ball = []
score = 0

blocks = { 0: empty, 1: wall, 2: block, 3: paddle, 4: ball }

next_cycle = False
while arcade.run() != 'F' or not next_cycle:
	next_cycle = arcade.state() == 'F'

	out = arcade.output()
	screen = list(zip(out[0::3], out[1::3], out[2::3]))
	#print(out)

	for x, y, b in screen:
		if x == -1 and y == 0:
			score = b
		else:
			for k in range(5):
				if k != b:
					if (x, y) in blocks[k]:
						blocks[k].remove((x, y))
			blocks[b].append((x, y))

	#print(ball)
	#print(paddle)

	# max_x = max([max(empty), max(wall), max(block), max(paddle), max(ball)])[0]
	# max_y = max([max([e[::-1] for e in empty]), max([e[::-1] for e in wall]), max([e[::-1] for e in block]), max([e[::-1] for e in paddle]), max([e[::-1] for e in ball]), ])[0]

	# for j in range(max_y):
	# 	line = ""
	# 	for i in range(max_x):
	# 		for k in range(5):
	# 			if (i, j) in blocks[k]:
	# 				line += sprites[k]
	# 	print(line)
	# print()
	# print("Score:", score)

	arcade.input([ball[0][0] - paddle[0][0]])

		

print("Final score:", score)
