# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 10

# Asteroids (monitoring station)
import math

def viewed(p, l):
	x = p[0]
	y = p[1]

	r = l[:]
	r.remove(p)

	viewable = []

	for e in r:
		slope = [e[0] - x, e[1] - y]
		lead = slope[0] if slope[0] else slope[1] if slope[1] else 1
		slope = list(map(lambda x: (x / lead) * math.copysign(1, lead), slope))
		if slope not in viewable:
			viewable.append(slope)

	return len(viewable)

# Append a '\n' at the end of your input file!
asteroid_map = list(map(lambda x : x[:-1], open("asteroids.txt", "r").readlines()))
height = len(asteroid_map)
width = len(asteroid_map[0])

asteroids = [(j, i) for i in range(len(asteroid_map)) for j in range(len(asteroid_map[0])) if asteroid_map[i][j] == '#']
#print(asteroids)

views = [viewed(e, asteroids) for e in asteroids]
#print(views)

print("Most views:", max(views))
print("( That's asteroid:", asteroids[views.index(max(views))], ")")
