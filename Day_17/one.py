# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 17

# ASCII
from functools import reduce
import sys
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

robot = Intcomputer(list(map(int, open("ascii.txt", "r").read().split(","))))

robot.run()

out = robot.output()[:-1]
view = []
row = []

for n in out:
	row.append(n)
	if n == 10:
		view.append(row)
		row = []

inter = []
for i in range(1, len(view) - 1):
	for j in range(1, len(view[0]) - 1):
		if view[i][j] == 35:
			if view[i + 1][j] == 35 and view[i - 1][j] == 35 and view[i][j + 1] == 35 and view[i][j - 1] == 35:
				inter.append((i, j))

print("Sum of the alignment parameters:", sum([x * y for x, y in inter]))
