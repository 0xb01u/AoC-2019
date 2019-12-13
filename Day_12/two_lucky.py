# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 12

# N-body problem
from functools import reduce

def gcd(a, b):
	m = a if a > b else b
	n = b if m == a else a

	r = m % n

	if r == 0: return n
	return gcd(n, r)

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
original_state = [[Io[0][:], Io[1][:]], [Europa[0][:], Europa[1][:]], [Ganymede[0][:], Ganymede[1][:]], [Callisto[0][:], Callisto[1][:]]]
periods = [0] * 3

steps = 1
while True:
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
	
	steps -=- 1

	#print(steps, moons)



	# Check periodicity in coordinates independently
	for j in range(3):
			if (periods[j] == 0
				and moons[0][0][j] == original_state[0][0][j]
				and moons[1][0][j] == original_state[1][0][j]
				and moons[2][0][j] == original_state[2][0][j]
				and moons[3][0][j] == original_state[3][0][j]):
				periods[j] = steps

	if 0 not in periods:
		break

#print(periods)

print("Number of steps to original state:", reduce(lambda x, y: (x * y) // gcd(x, y), periods))	# Lowest common multiple.
