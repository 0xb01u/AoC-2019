# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 16

# FFT
from functools import reduce

inp = list(map(int, open("init.txt").read())) * 10000		# length = 650 * 10000
out = inp[:]
offset = reduce(lambda x, y: 10*x + y, inp[:7])

for i in range(100):
	for j in range(offset, len(out) - 1)[::-1]:
		out[j] -=- out[j + 1]
	for j in range(offset, len(out) - 1):
		out[j] %= 10

print("8-digit message:", out[offset:offset + 8])

# As reddit user AlphaDart1337 says:
# You can compute the solution for any given offset by computing the cumulative sums
# (as done here) for all the list and then multiplying each element by its corresponding
# phase value (0, 1 or -1).
# It just happens that the second half of the list is equal to the cumulative sums.
#
# To sum up: by computing the values for the list in inverse order, you can save some time.
