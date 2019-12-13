# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 13

# Care package
import sys
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

arcade = Intcomputer(list(map(int, open("game.txt", "r").read().split(","))))

tiles = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

arcade.run()
for e in arcade.output()[2::3]:
	tiles[e] += 1

print("Number of block tiles:", tiles[2])
