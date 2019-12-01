# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 1.

# Fuel per module = floor(module_mass / 4) - 2
# Sum of fuel for all modules?
import math, functools

mass = map(int, open("modules.txt", "r").readlines())

fuel = map(lambda e: math.floor(e / 3) - 2, mass)
total_fuel = functools.reduce(lambda x, y : x + y, fuel)

print("Total fuel needed: ", total_fuel)
