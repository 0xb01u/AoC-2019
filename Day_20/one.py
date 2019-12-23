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


for i in range(len(donut)):
	for j in range(len(donut[0])):
		if donut[i][j] == '.': path.append((i, j))

		elif donut[i][j] >= 'A' and donut[i][j] <= 'Z':
			if donut[i - 1][j] == '.':
				portal = donut[i][j] + donut[i + 1][j]
				donut[i + 1][j] = ' '
			elif donut[i][j - 1] == '.':
				portal = donut[i][j] + donut[i][j + 1]
				donut[i][j + 1] = ' '
			elif donut[i][j + 1] == '.':
				portal = donut[i][j - 1] + donut[i][j]
			elif donut[i + 1][j] == '.':
				portal = donut[i - 1][j] + donut[i][j]
			else:
				continue

			if portal == "AA": entrance = (i, j)
			elif portal == "ZZ": goal = (i, j)
			else:
				if portal not in tmp_portals:
					tmp_portals[portal] = (i, j)
				else:
					portals[(i, j)] = tmp_portals[portal]
					portals[tmp_portals[portal]] = (i, j)

			path.append((i, j))

steps = { entrance: -1 }
explore = [entrance]
explored = set()

while len(explore) > 0:
	cur = explore.pop(0)
	explored.add(cur)

	if (cur[0] - 1, cur[1]) in portals and portals[(cur[0] - 1, cur[1])] not in explored:
		explore.append(portals[(cur[0] - 1, cur[1])])
		steps[portals[(cur[0] - 1, cur[1])]] = steps[cur]
	elif (cur[0] - 1, cur[1]) in path and (cur[0] - 1, cur[1]) not in explored:
		explore.append((cur[0] - 1, cur[1]))
		steps[(cur[0] - 1, cur[1])] = steps[cur] + 1
	if (cur[0], cur[1] + 1) in portals and portals[(cur[0], cur[1] + 1)] not in explored:
		explore.append(portals[(cur[0], cur[1] + 1)])
		steps[portals[(cur[0], cur[1] + 1)]] = steps[cur]
	elif (cur[0], cur[1] + 1) in path and (cur[0], cur[1] + 1) not in explored:
		explore.append((cur[0], cur[1] + 1))
		steps[(cur[0], cur[1] + 1)] = steps[cur] + 1
	if (cur[0] + 1, cur[1]) in portals and portals[(cur[0] + 1, cur[1])] not in explored:
		explore.append(portals[(cur[0] + 1, cur[1])])
		steps[portals[(cur[0] + 1, cur[1])]] = steps[cur]
	elif (cur[0] + 1, cur[1]) in path and (cur[0] + 1, cur[1]) not in explored:
		explore.append((cur[0] + 1, cur[1]))
		steps[(cur[0] + 1, cur[1])] = steps[cur] + 1
	if (cur[0], cur[1] - 1) in portals and portals[(cur[0], cur[1] - 1)] not in explored:
		explore.append(portals[(cur[0], cur[1] - 1)])
		steps[portals[(cur[0], cur[1] - 1)]] = steps[cur]
	elif (cur[0], cur[1] - 1) in path and (cur[0], cur[1] - 1) not in explored:
		explore.append((cur[0], cur[1] - 1))
		steps[(cur[0], cur[1] - 1)] = steps[cur] + 1

print("Min number of steps to get to the end:", steps[goal] - 1)
