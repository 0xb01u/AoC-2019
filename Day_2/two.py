# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 2

# Intcomputer
import math, functools

def reset():
	global memory
	return list(map(int, open("intcomputer.txt", "r").read().split(",")))

def update():
	global memory, instructions, src, dst
	instructions = memory[::4]
	src = list(zip(memory[1::4], memory[2::4]))
	dst = memory[3::4]

noun = 0
verb = 0
output = 1

while output != 19690720 and noun < 100:
	while output != 19690720 and verb < 100:
		memory = reset()
		instructions = []
		src = []
		dst = []

		memory[1] = noun
		memory[2] = verb

		update()

		for i in range(len(instructions)):
			if instructions[i] == 99:
				break
			if instructions[i] == 1:
				memory[dst[i]] = memory[src[i][0]] + memory[src[i][1]]
			elif instructions[i] == 2:
				memory[dst[i]] = memory[src[i][0]] * memory[src[i][1]]
			update()

		output = memory[0]
		verb += 1

		#print(output, noun, verb)

	verb = 0
	noun += 1



print("Result: ", 100 * memory[1] + memory[2])
