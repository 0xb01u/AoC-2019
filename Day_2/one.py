# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 2

# Intcomputer
import math, functools

program = list(map(int, open("intcomputer.txt", "r").read().split(",")))
opcodes = []
src = []
dst = []

def update():
	global program, opcodes, src, dst
	opcodes = program[::4]
	src = list(zip(program[1::4], program[2::4]))
	dst = program[3::4]

program[1] = 12
program[2] = 2

update()

for i in range(len(opcodes)):
	if opcodes[i] == 99:
		break
	if opcodes[i] == 1:
		program[dst[i]] = program[src[i][0]] + program[src[i][1]]
	elif opcodes[i] == 2:
		program[dst[i]] = program[src[i][0]] * program[src[i][1]]
	update()

print(program)
