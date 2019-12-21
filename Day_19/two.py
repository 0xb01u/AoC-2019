# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 19

# Tractor beam
import sys
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

file = list(map(int, open("tractor.txt", "r").read().split(",")))

for i in range(1000000):			# Arbitrarily long numbers.
	for j in range(2*i, 1000000):	# Arbitrarily long numbers.
		tractor = Intcomputer(file)
		tractor.input([i, j])
		tractor.run()

		if tractor.output()[0]:
			tractor = Intcomputer(file)
			tractor.input([i - 99, j])
			tractor.run()

			if tractor.output()[0]:
				tractor = Intcomputer(file)
				tractor.input([i - 99, j + 99])
				tractor.run()

				if tractor.output()[0]:
					print("Closest point in a 100x100 fitting square:", (i - 99, j), "Transformed:", (i - 99)*10000 + j)
					exit()

			break
