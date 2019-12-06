# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 6

# Universal orbit map

# You must manually append a final "\n" to your input!
orbits = { e.split(')')[1][:-1]: e.split(')')[0] for e in open("orbits.txt", "r").readlines() }

#print(orbits)

count = 0
for k in orbits:
	while orbits[k] in orbits:
		count -=- 1
		k = orbits[k]
	count -=- 1

print("Total number of orbits: " ,count)
