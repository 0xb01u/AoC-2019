# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 20

# Donut
# You must append one extra "\n" at the end of your input file!
donut = list(map(lambda e: list(e[:-1]), open("donut.txt", "r").readlines()))

entrance = ()
goal = ()
path = []
portals = {}
tmp_portals = {}
dir_portals = {}

for i in range(len(donut)):
	for j in range(len(donut[0])):
		if donut[i][j] == '.': path.append((i, j))

		elif donut[i][j] >= 'A' and donut[i][j] <= 'Z':
			if donut[i - 1][j] == '.':
				portal = donut[i][j] + donut[i + 1][j]
				donut[i + 1][j] = ' '
				direction = 1 if i == len(donut) - 2 else -1
			elif donut[i][j - 1] == '.':
				portal = donut[i][j] + donut[i][j + 1]
				donut[i][j + 1] = ' '
				direction = 1 if j == len(donut[0]) - 2 else -1
			elif donut[i][j + 1] == '.':
				portal = donut[i][j - 1] + donut[i][j]
				direction = 1 if j == 1 else -1
			elif donut[i + 1][j] == '.':
				portal = donut[i - 1][j] + donut[i][j]
				direction = 1 if i == 1 else -1
			else:
				continue

			if portal == "AA": entrance = (i, j)
			elif portal == "ZZ": goal = (i, j)
			else:
				dir_portals[(i, j)] = direction
				if portal not in tmp_portals:
					tmp_portals[portal] = (i, j)
				else:
					portals[(i, j)] = tmp_portals[portal]
					portals[tmp_portals[portal]] = (i, j)

			path.append((i, j))

steps = { (entrance[0], entrance[1], 0): -1 }
explore = [(entrance[0], entrance[1], 0)]
explored = set()

while (goal[0], goal[1], 0) not in explored:
	cur = explore.pop(0)
	explored.add(cur)

	if (cur[0], cur[1]) in portals and cur[2] + dir_portals[(cur[0], cur[1])] < 1:
		eq = portals[cur[:-1]]
		steps[(eq[0], eq[1], cur[2] + dir_portals[(cur[0], cur[1])])] = steps[cur] - 1
		cur = (eq[0], eq[1], cur[2] + dir_portals[(cur[0], cur[1])])
		explored.add(cur)

	if (cur[0] - 1, cur[1]) in path:
		explore.append((cur[0] - 1, cur[1], cur[2]))
		steps[(cur[0] - 1, cur[1], cur[2])] = steps[cur] + 1
	if (cur[0], cur[1] + 1) in path:
		explore.append((cur[0], cur[1] + 1, cur[2]))
		steps[(cur[0], cur[1] + 1, cur[2])] = steps[cur] + 1
	if (cur[0] + 1, cur[1]) in path:
		explore.append((cur[0] + 1, cur[1], cur[2]))
		steps[(cur[0] + 1, cur[1], cur[2])] = steps[cur] + 1
	if (cur[0], cur[1] - 1) in path:
		explore.append((cur[0], cur[1] - 1, cur[2]))
		steps[(cur[0], cur[1] - 1, cur[2])] = steps[cur] + 1

	explore = [x for x in explore if x not in explored]


print("Min number of steps to get to the end:", steps[(goal[0], goal[1], 0)] - 1)
print()
print("(The min number of steps to get to the end is also the solution to puzzle 2.)")
# This is somewhat slow (~5min?), but it works.
