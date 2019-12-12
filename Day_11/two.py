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
white = [pos]


def update(mov):
	global pos, direction, panels, black, white

	if pos not in black and pos not in white:
		black.append(pos)

	color = mov[0]

	if pos in black and color:
		if pos in panels: panels[pos] += 1	# I thought I would need to know how many times a panel has been painted.
		else: panels[pos] = 1
		black.remove(pos)
		white.append(pos)
	elif pos in white and not color:
		if pos in panels: panels[pos] += 1	# I thought I would need to know how many times a panel has been painted.
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
com.input([1])
while com.run() != 'F':
	chain.extend(com.output())
	update([chain[-2], chain[-1]])
	color = 1 if pos in white else 0
	com.input([color])

all_panels = []
all_panels.extend(black)
all_panels.extend(white)

max_y = max(all_panels)[0]
min_y = min(all_panels)[0]
max_x = max([e[::-1] for e in all_panels])[0]
min_x = min([e[::-1] for e in all_panels])[0]

print(max_x, min_x, max_y, min_y)

paint = []
for i in range(min_y, max_y + 1):
	paint.append("")
	for j in range(min_x, max_x + 1):
		if (i, j) in white:	# Don't print unstepped panels as white ones!
			paint[-1] += "#"
		else:
			paint[-1] += " "
for s in paint[::-1]: print(s)
