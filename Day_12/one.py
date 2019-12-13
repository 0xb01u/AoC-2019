# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 12

# N-body problem
from functools import reduce

abs_sum = lambda e1, e2: abs(e1) + abs(e2)

Io = [[-7, -1, 6], [0, 0, 0]]
Europa = [[6, -9, -9], [0, 0, 0]]
Ganymede = [[-12, 2, -7], [0, 0, 0]]
Callisto = [[4, -17, -12], [0, 0, 0]]

# Example:
# Io = [[-1, 0, 2], [0, 0, 0]]
# Europa = [[2, -10, -7], [0, 0, 0]]
# Ganymede = [[4, -8, 8], [0, 0, 0]]
# Callisto = [[3, 5, -1], [0, 0, 0]]

moons = [Io, Europa, Ganymede, Callisto]

for i in range(1000):
	system_energy = 0
	potential = 0
	kinetic = 0

	# Gravity
	for m1 in moons:
		for m2 in moons:
			if m1 == m2:
				continue
			for i in range(3):
				m1[1][i] += 1 if m2[0][i] > m1[0][i] else -1 if m2[0][i] < m1[0][i] else 0
	# Velocity
	for m in moons:
		for i in range(3):
			m[0][i] += m[1][i]
		potential = reduce(abs_sum, m[0])
		kinetic = reduce(abs_sum, m[1])
		system_energy += potential * kinetic

print("Total system energy after 1000 steps:", system_energy)
