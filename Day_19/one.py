# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 19

# Tractor beam
import sys
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

file = list(map(int, open("tractor.txt", "r").read().split(",")))
tractor = Intcomputer(file)

affected = 0

for i in range(50):
	s = ""
	for j in range(50):
		tractor.input([i, j])
		tractor.run()

		if tractor.output()[0]:
			affected -=- 1
			s += "#"
		else:
			s += "."

		tractor = Intcomputer(file)

	print(s)

print("Number of points affected:", affected)
