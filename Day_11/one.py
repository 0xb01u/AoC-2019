# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 11

# Space police
import sys
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

com = Intcomputer(list(map(int, open("paint.txt", "r").read().split(","))))

pos = (2, 2)
direction = 'U'
panels = {}
black = []
white = []


def update(mov):
	global pos, direction, panels, black, white

	if pos not in black and pos not in white:
		black.append(pos)

	color = mov[0]

	if pos in black and color:
		if pos in panels: panels[pos] += 1
		else: panels[pos] = 1
		black.remove(pos)
		white.append(pos)
	elif pos in white and not color:
		if pos in panels: panels[pos] += 1
		else: panels[pos] = 1
		white.remove(pos)
		black.append(pos)

	rot = mov[1] if mov[1] else - 1
	directions = ['U', 'R', 'D', 'L']
	direction = directions[(4 + directions.index(direction) + rot) % 4]

	if direction == 'U': pos = (pos[0] + 1, pos[1])
	if direction == 'R': pos = (pos[0], pos[1] + 1)
	if direction == 'D': pos = (pos[0] - 1, pos[1])
	if direction == 'L': pos = (pos[0], pos[1] - 1)

chain = []
com.input([0])
while com.run() != 'F':
	chain.extend(com.output())
	update([chain[-2], chain[-1]])
	color = 1 if pos in white else 0
	com.input([color])

print("# panels painted:", len(panels))
