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

while True:
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
		if pos not in visited:visited.append(pos)
		pos = cur[:]
		prev = d
	if status == 2: break

	

	# system("clear")
	# for i in range(-26, 26)[::-1]:
	# 	s = ""
	# 	for j in range(-25, 26):
	# 		if (i, j) == pos: s += D		
	# 		elif (i, j) in walls: s += "#"
	# 		elif (i, j) in visited: s += "."
	# 		else: s += " "
	# 	print(s)



print("Fewest number of movement commands:", steps)
print(f"(Position: {pos})")
