# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 14

# ORE
# You must manually append one final "\n" to the input file!
change = { (int(e.split(" ")[0]), e.split(" ")[1]): list(zip((int(n) for n in s.split(" ")[0::2]), s.split(" ")[1::2])) for s, e in list(map(lambda x: tuple(x[:-1].replace(", ", " ").split(" => ")), open("transformations.txt").readlines())) }

quantity = { k[1]: 0 for k in change }
quantity["ORE"] = 0
quantity["FUEL"] = 1



# while True:
# 	exit = True
# 	for q, e in change:
# 		if quantity[e] >= q:
# 			exit = False
# 			quantity[e] -= q
# 			for n, v in change[(q, e)]:
# 				quantity[v] += n

# 	if exit: break

while any(quantity[e] > 0 for e in quantity if e != "ORE"):
	for q, e in change:
		if quantity[e] > 0:
			quantity[e] -= q
			for n, v in change[(q, e)]:
				quantity[v] += n



print("Minimun ORE needed:", quantity["ORE"])
