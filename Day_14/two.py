# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 14

# ORE
import math

# You must manually append one final "\n" to the input file!
change = { (int(e.split(" ")[0]), e.split(" ")[1]): list(zip((int(n) for n in s.split(" ")[0::2]), s.split(" ")[1::2])) for s, e in list(map(lambda x: tuple(x[:-1].replace(", ", " ").split(" => ")), open("transformations.txt").readlines())) }



low = 1
high = 10**12	# Arbitrarily high number. We have a n-to-1 ORE to FUEL conversion (n > 1), so the fuel isn't going to be as high as 10**12.
while low <= high:
	fuel = (high + low) // 2

	quantity = { k[1]: 0 for k in change }
	quantity["ORE"] = 0
	quantity["FUEL"] = fuel
	#quantity["FUEL"] = 11788286	# At first, I solved puzzle 2 by trial and error changing this value.

	while any(quantity[e] > 0 for e in quantity if e != "ORE"):
		for q, e in change:
			if quantity[e] > 0:
				m = math.ceil(quantity[e] / q)
				quantity[e] -= q*m
				for n, v in change[(q, e)]:
					quantity[v] += n*m

	if quantity["ORE"] > 10**12:
		high = fuel - 1
	elif quantity["ORE"] < 10**12:
		low = fuel + 1



print("Maximun fuel with 1 trillion ORE:", fuel)
