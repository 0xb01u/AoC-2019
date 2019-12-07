# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 7

# Amplifiers
import itertools, sys
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

final = []
phases = range(5, 10)
sequences = list(itertools.permutations(phases))

file = list(map(int, open("software.txt", "r").read().split(",")))

def reset():
	A = Intcomputer(file)
	B = Intcomputer(file)
	C = Intcomputer(file)
	D = Intcomputer(file)
	E = Intcomputer(file)

	amps = [A, B, C, D, E]
	return amps

for ex in sequences:
	amps = reset()
	for i in range(len(ex)):
		amps[i].input([ex[i]])
	amps[0].input([0])
	i = 0
	while amps[-1].state() != 'F':
		amps[(i + 1) % len(amps)].input(amps[i].output())
		amps[i].run()
		i = (i + 1) % len(amps)
	final.append(amps[-1].output()[0])

print("Max thruster signal: ", max(final))

# This is slightly better than the first program I used to solve this puzzle, but still ugly.
