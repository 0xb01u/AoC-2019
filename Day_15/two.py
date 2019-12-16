# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 15

# Repair droid
import random
import sys
from os import system
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

droid = Intcomputer(list(map(int, open("control.txt", "r").read().split(","))))
pos = (0, 0)
directions = ['N', 'W', 'S', 'E']
D = 'N'
walls = []
visited = []
steps = 0

minutes = 0
spreading = False

# Arbitrarily high number of iterations, just to make sure we traverse all the maze.
# It seems 10**4 is enough. (10**3 is not.)
# This was first solved with an infinite loop.
# I printed the var minutes on every iteration and I stopped the program when it stopped increasing.
for _ in range(10**4):
	if D == 'N':
		if (pos[0], pos[1] + 1) not in walls: D = 'E'
	elif D == 'S':
		if (pos[0], pos[1] - 1) not in walls: D = 'W'
	elif D == 'W':
		if (pos[0] + 1, pos[1]) not in walls: D = 'N'
	elif D == 'E':
		if (pos[0] - 1, pos[1]) not in walls: D = 'S'

	if D == 'N': d = 1
	if D == 'S': d = 2
	if D == 'W': d = 3
	if D == 'E': d = 4

	if d == 1: cur = (pos[0] + 1, pos[1])
	elif d == 2: cur = (pos[0] - 1, pos[1])
	elif d == 3: cur = (pos[0], pos[1] - 1)
	else: cur = (pos[0], pos[1] + 1)

	droid.input([d])
	droid.run()

	status = droid.output()[-1]
	if status == 0:
		D = directions[(directions.index(D) + 1) % len(directions)]
		if cur not in walls: walls.append(cur)
	else:
		steps += -1 if cur in visited else 1
		if pos not in visited: visited.append(pos)
		pos = cur[:]
	if status == 2:
		steps = 0
		spreading = True
		visited = []

	if spreading and steps > minutes: minutes = steps



	# system("clear")
	# for i in range(-26, 26)[::-1]:
	# 	s = ""
	# 	for j in range(-25, 26):
	# 		if (i, j) == pos: s += D		
	# 		elif (i, j) in walls: s += "#"
	# 		elif (i, j) in visited: s += "."
	# 		else: s += " "
	# 	print(s)



print("Number of minutes it takes to fill the whole area with oxygen:", minutes)
