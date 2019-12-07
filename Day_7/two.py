# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 7

# Amplifiers
import itertools

inputA = []
inputB = []
inputC = []
inputD = []
inputE = []

final = []
phases = [5, 6, 7, 8, 9]
sequences = []
# It's my first time using itertools :/
for s in list(itertools.product(phases, repeat = 5)):
	if 5 in s and 6 in s and 7 in s and 8 in s and 9 in s:
		sequences.append(list(s))

def reset():
	file = "software.txt"
	return [list(map(int, open(file, "r").read().split(","))), list(map(int, open(file, "r").read().split(","))), list(map(int, open(file, "r").read().split(","))), list(map(int, open(file, "r").read().split(","))), list(map(int, open(file, "r").read().split(",")))]

def intcomputer(input):
	amp = 0

	memory = reset()
	indexSrcA = 0
	indexSrcB = 0
	indexDst = 0

	i = [0] * 5
	while i[amp] < len(memory[amp]) - 2:
		e = memory[amp][i[amp]] % 100

		if e == 99:
			break

		if e == 3 or e == 4:
			param = (memory[amp][i[amp]] // 100)
			indexDst = i[amp] + 1 if param == 1 else memory[amp][i[amp] + 1]		

		else:
			param = (memory[amp][i[amp]] // 10000, memory[amp][i[amp]] // 1000 - (memory[amp][i[amp]] // 10000) * 10, memory[amp][i[amp]] // 100 - (memory[amp][i[amp]] // 1000) * 10 - (memory[amp][i[amp]] // 10000) * 100)[::-1]
			indexSrcA = i[amp] + 1 if param[0] == 1 else memory[amp][i[amp] + 1]
			indexSrcB = i[amp] + 2 if param[1] == 1 else memory[amp][i[amp] + 2]
			indexDst = i[amp] + 3 if param[2] == 1 else memory[amp][i[amp] + 3]

		if e == 1:
			memory[amp][indexDst] = memory[amp][indexSrcA] + memory[amp][indexSrcB]
			i[amp] -=- 4
		elif e == 2:
			memory[amp][indexDst] = memory[amp][indexSrcA] * memory[amp][indexSrcB]
			i[amp] -=- 4
		elif e == 3:
			memory[amp][indexDst] = input[amp].pop(0)
			i[amp] -=- 2
		elif e == 4:
			input[(amp + 1) % len(input)].append(memory[amp][indexDst])
			i[amp] -=- 2
			amp = (amp + 1) % len(input)
		elif e == 5:
			if memory[amp][indexSrcA]: i[amp] = memory[amp][indexSrcB]
			else: i[amp] -=- 3
		elif e == 6:
			if not memory[amp][indexSrcA]: i[amp] = memory[amp][indexSrcB]
			else: i[amp] -=- 3
		elif e == 7:
			memory[amp][indexDst] = int(memory[amp][indexSrcA] < memory[amp][indexSrcB])
			i[amp] -=- 4
		elif e == 8:
			memory[amp][indexDst] = int(memory[amp][indexSrcA] == memory[amp][indexSrcB])
			i[amp] -=- 4	



for ex in sequences:
	amps = []
	for i in range(len(ex)):
		amps.append([ex[i]])
	amps[0].append(0)
	intcomputer(amps)
	final.append(amps[0][0])

print("Max thruster signal: ", max(final))

# This is the ugliest thing I've coded in my entire life and I'm very ashamed of it
