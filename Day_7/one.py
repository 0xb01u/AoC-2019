# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 7

# Amplifiers
import itertools

inputs = []

final = []
phases = [0, 1, 2, 3, 4]
sequences = []
# It's my first time using itertools :/
for s in list(itertools.product(phases, repeat = 5)):
	if 0 in s and 1 in s and 2 in s and 3 in s and 4 in s:
		sequences.append(list(s))

def reset():
	return list(map(int, open("software.txt", "r").read().split(",")))

def intcomputer(input):
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
			memory[indexDst] = input.pop(0)
			i -=- 2
		elif e == 4:
			input.insert(1, memory[indexDst])
			i -=- 2
		elif e == 5:
			if memory[indexSrcA]: i = memory[indexSrcB]
			else: i -=- 3
		elif e == 6:
			if not memory[indexSrcA]: i = memory[indexSrcB]
			else: i -=- 3
		elif e == 7:
			memory[indexDst] = int(memory[indexSrcA] < memory[indexSrcB])
			i -=- 4
		elif e == 8:
			memory[indexDst] = int(memory[indexSrcA] == memory[indexSrcB])
			i -=- 4



for ex in sequences:
	ex.insert(1, 0)
	for i in range(5):
		intcomputer(ex)
	final.append(ex)

print("Max thruster signal: ", max(final))
