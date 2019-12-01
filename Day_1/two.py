# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 1.

# Fuel per module = floor(module_mass / 4) - 2
# Sum of fuel for all modules?
import math, functools

mass = map(int, open("modules.txt", "r").readlines())

f = lambda e: math.floor(e / 3) - 2
fuel = list(map(f, mass))
fuelOfFuel = list(map(f, fuel))

while max(fuelOfFuel) > 0:
	fuel = [fuel[i] + fuelOfFuel[i] for i in range(len(fuel))]
	fuelOfFuel = list(map(lambda x : f(x) if f(x) > 0 else 0, fuelOfFuel))

total_fuel = functools.reduce(lambda x, y : x + y, fuel)

print("Total fuel needed: ", total_fuel)
