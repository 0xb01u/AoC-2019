# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 5

# TEST
import math, functools

def reset():
	return list(map(int, open("test.txt", "r").read().split(",")))

memory = reset()
indexSrcA = 0
indexSrcB = 0
indexDst = 0

i = 0
while i < len(memory) - 2:
	e = memory[i] % 100

	if e == 99:
		break

	if e == 3 or e == 4:
		param = (memory[i] // 100)
		indexDst = i + 1 if param == 1 else memory[i + 1]

	else:
		param = (memory[i] // 10000, memory[i] // 1000 - (memory[i] // 10000) * 10, memory[i] // 100 - (memory[i] // 1000) * 10 - (memory[i] // 10000) * 100)[::-1]
		indexSrcA = i + 1 if param[0] == 1 else memory[i + 1]
		indexSrcB = i + 2 if param[1] == 1 else memory[i + 2]
		indexDst = i + 3 if param[2] == 1 else memory[i + 3]

	if e == 1:
		memory[indexDst] = memory[indexSrcA] + memory[indexSrcB]
		i -=- 4
	elif e == 2:
		memory[indexDst] = memory[indexSrcA] * memory[indexSrcB]
		i -=- 4
	elif e == 3:
		memory[indexDst] = int(input("Request: "))
		i -=- 2
	elif e == 4:
		print(memory[indexDst])
		i -=- 2

print("The last input was the diagnosis code.")
