# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 6

# Universal orbit map

# You must manually append a final "\n" to your input!
orbits = { e.split(')')[1][:-1]: e.split(')')[0] for e in open("orbits.txt", "r").readlines() }

#print(orbits)

sanParents = []
sanKey = 'SAN'
while sanKey in orbits:
	sanKey = orbits[sanKey]
	sanParents.append(sanKey)

#print(sanParents)

count = 0
while orbits['YOU'] != orbits['SAN']:
	if orbits['YOU'] in sanParents:
		orbits['YOU'] = sanParents[sanParents.index(orbits['YOU']) - 1]
	else:
		orbits['YOU'] = orbits[orbits['YOU']]
	count -=- 1


print("Minimum number of orbital transfers: " , count)
