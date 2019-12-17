# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 16

# FFT
from functools import reduce
import math

inp = list(map(int, open("init.txt").read()))
out = inp[:]

for i in range(100):
	inp = out[:]
	for j in range(len(inp)):
		phase = [0] * (j + 1) + [1] * (j + 1) + [0] * (j + 1) + [-1] * (j + 1)

		z = [0]
		z.extend(list(zip((phase * (math.ceil(len(out) / len(phase)) + 1))[1:], inp)))
		value = reduce(lambda x, y: x + y[0] * y[1], z)
		out[j] = abs(value) % 10

print("First 8 digits after 100 phases:", out[:8])
