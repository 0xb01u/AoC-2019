# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 10

# Asteroids (monitoring station)
import math

def angle(A, O):
	A = (A[0] - O[0], A[1] - O[1])
	return (360 + 90 + (math.atan2(A[1], A[0]) * 180 / math.pi)) % 360

def viewed(p, l):
	x = p[0]
	y = p[1]

	r = l[:]
	r.remove(p)

	viewable = []

	for e in r:
		slope = [e[0] - x, e[1] - y]
		lead = slope[0] if slope[0] else slope[1] if slope[1] else 0
		slope = list(map(lambda x: (x / lead) * math.copysign(1, lead), slope))
		if slope not in viewable:
			viewable.append(slope)

	return len(viewable)

def insight(p, q, l):
	r = l[l.index(q) + 1:] if l.index(p) > l.index(q) else l[:l.index(q)]	
	if p in r:
		r.remove(p)

	x1 = p[0]
	y1 = p[1]
	x2 = q[0]
	y2 = q[1]

	this_slope = [x2 - x1, y2 - y1]	
	lead = this_slope[0] if this_slope[0] else this_slope[1] if this_slope[1] else 1
	this_slope = list(map(lambda x: (x / lead) * math.copysign(1, lead), this_slope))

	for e in r:
		slope = [e[0] - x1, e[1] - y1]
		lead = slope[0] if slope[0] else slope[1] if slope[1] else 0
		slope = list(map(lambda x: (x / lead) * math.copysign(1, lead), slope))
		if slope == this_slope:
			return False

	return True


# Append a '\n' at the end of your input file!
asteroid_map = list(map(lambda x : x[:-1], open("asteroids.txt", "r").readlines()))
height = len(asteroid_map)
width = len(asteroid_map[0])

asteroids = [(j, i) for i in range(len(asteroid_map)) for j in range(len(asteroid_map[0])) if asteroid_map[i][j] == '#']
#print(asteroids)

views = [viewed(e, asteroids) for e in asteroids]
#print(views)

# _______________________________________________

station = asteroids[views.index(max(views))]
print("Station in", station)

n = 0
while n < 200:
	clockwise = asteroids[:]
	clockwise.remove(station)
	angles = list(map(lambda x : angle(x, station), clockwise))
	ordered = [x for _, x in sorted(zip(angles, clockwise)) if insight(station, x, asteroids)]

	for p in ordered:
		if p in asteroids and insight(station, p, asteroids):
			asteroids.remove(p)
			n += 1
			if n == 200:
				print("200th removed:", p[0] * 100 + p[1])
				break
