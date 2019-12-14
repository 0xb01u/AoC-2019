# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 14

# ORE
import math

# You must manually append one final "\n" to the input file!
change = { (int(e.split(" ")[0]), e.split(" ")[1]): list(zip((int(n) for n in s.split(" ")[0::2]), s.split(" ")[1::2])) for s, e in list(map(lambda x: tuple(x[:-1].replace(", ", " ").split(" => ")), open("transformations.txt").readlines())) }

quantity = { k[1]: 0 for k in change }
quantity["ORE"] = 0
quantity["FUEL"] = 1



while any(quantity[e] > 0 for e in quantity if e != "ORE"):
	for q, e in change:
		if quantity[e] > 0:
			m = math.ceil(quantity[e] / q)
			quantity[e] -= q*m
			for n, v in change[(q, e)]:
				quantity[v] += n*m



print("Minimun ORE needed:", quantity["ORE"])
