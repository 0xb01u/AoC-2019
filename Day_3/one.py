# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 3

# Wires
central_port = [1, 1]

f = open("wires.txt", "r")
path1 = f.readline().split(",")
path2 = f.readline().split(",")

wire1 = []
wire2 = []

intersections = [[-2570, -3111], [-1754, -2365], [-1619, -3122], [-1575, -3122], [-2273, -3170], [-1941, -3159], [-1940, -3170], [-1575, -3374], [-1575, -3033], [-1619, -3033], [-1603, -2697], [-691, -2266], [-1162, -1323], [-1180, -1878], [15, -2266], [928, -1884], [928, -1835], [811, -1765], [616, -1765], [598, -1765], [481, -1765], [416, -1619], [316, -1613], [167, -1613], [167, -1354], [175, -1354], [316, -1354], [616, -1354], [738, -1344], [738, -1216], [811, -1065], [1370, -1216], [1370, -1835], [1180, -1884], [1180, -1835], [811, -1500], [616, -1500], [316, -1500], [175, -1058], [167, -1058]]

def cross(p1, p2, q1, q2):
	return ((p1[0] < q1[0] and p1[1] < q1[1]) and (p2[0] > q2[0] or p2[1] > q2[1])) or ((q1[0] < p1[0] and q1[1] < p1[1]) and (q2[0] > p2[0] or q2[1] > p2[1]))

def intersection(p1, p2, q1, q2):
	if p1[0] == p2[0]: return [p1[0], q1[1]]
	else: return [q1[0], p1[1]]


# last = central_port[:]
# for d in path1:
# 	if d[0] == "R":
# 		for i in range(int(d[1:])):
# 			wire1.append([last[0], last[1] + 1])
# 			last = wire1[-1]
# 	elif d[0] == "U":
# 		for i in range(int(d[1:])):
# 			wire1.append([last[0] + 1, last[1]])
# 			last = wire1[-1]
# 	elif d[0] == "L":
# 		for i in range(int(d[1:])):
# 			wire1.append([last[0], last[1] - 1])
# 			last = wire1[-1]
# 	elif d[0] == "D":
# 		for i in range(int(d[1:])):
# 			wire1.append([last[0] - 1, last[1]])
# 			last = wire1[-1]

# last = central_port[:]
# for d in path2:
# 	if d[0] == "R":
# 		for i in range(int(d[1:])):
# 			wire2.append([last[0], last[1] + 1])
# 			last = wire2[-1]
# 	elif d[0] == "U":
# 		for i in range(int(d[1:])):
# 			wire2.append([last[0] + 1, last[1]])
# 			last = wire2[-1]
# 	elif d[0] == "L":
# 		for i in range(int(d[1:])):
# 			wire2.append([last[0], last[1] - 1])
# 			last = wire2[-1]
# 	elif d[0] == "D":
# 		for i in range(int(d[1:])):
# 			wire2.append([last[0] - 1, last[1]])
# 			last = wire2[-1]

# intersections = [p for p in wire1 if p in wire2]
# print(intersections)

distances = [abs(p[0] - central_port[0]) + abs(p[1] - central_port[1]) for p in intersections]
print("Closest distance: ", min(distances))
