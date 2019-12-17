# -*- coding: utf-8 -*-
# Advent of Code 2019 - Intcomputer object
# Wrote after Day 7. Intcomputer puzzles were getting annoying.

class Intcomputer:
	__mem = []
	__pc = 0
	__indata = []
	__outdata = []
	__states = "RIF"
	__ps = __states[0]
	__rb = 0

	def __init__(self, program):
		self.__mem = program[:]
		self.__mem.extend([0] * 10*len(program))
		self.__indata = []
		self.__outdata = []

	def input(self, e):
		self.__indata.extend(e)
		if self.__ps == 'I':
			self.__ps = self.__states[0]
			self.run()

	def output(self):
		r = self.__outdata[:]
		self.__outdata = []
		return r

	def __sum(self, i):
		self.__mem[i.dst] = self.__mem[i.srcA] + self.__mem[i.srcB]
		self.__pc -=- 4

	def __prod(self, i):
		self.__mem[i.dst] = self.__mem[i.srcA] * self.__mem[i.srcB]
		self.__pc -=- 4

	def __input(self, i):
		if len(self.__indata) > 0:
			self.__mem[i.srcA] = self.__indata.pop(0)
			self.__pc -=- 2
		else:
			self.__ps = self.__states[1]
			return 1

	def __output(self, i):
		self.__outdata.append(self.__mem[i.srcA])
		self.__pc -=- 2

	def __jumpz(self, i):
		if self.__mem[i.srcA]: self.__pc = self.__mem[i.srcB]
		else: self.__pc -=- 3

	def __jumpnz(self, i):
		if not self.__mem[i.srcA]: self.__pc = self.__mem[i.srcB]
		else: self.__pc -=- 3

	def __slt(self, i):
		self.__mem[i.dst] = int(self.__mem[i.srcA] < self.__mem[i.srcB])
		self.__pc -=- 4

	def __seq(self, i):
		self.__mem[i.dst] = int(self.__mem[i.srcA] == self.__mem[i.srcB])
		self.__pc -=- 4

	def __rel(self, i):
		self.__rb += self.__mem[i.srcA]
		self.__pc -=- 2

	def __halt(self, i):
		self.__ps = self.__states[2]
		return 1

	__exec = {1: __sum, 2: __prod, 3: __input, 4: __output, 5: __jumpz, 6: __jumpnz, 7: __slt, 8: __seq, 9: __rel, 99: __halt}

	def step(self):
		if self.__ps == 'R':
			instruction = Intinstruction(self.__mem, self.__pc, self.__rb)
			return 1 if self.__exec[instruction.opcode](self, instruction) else 0
		return 1

	def state(self):
		return self.__ps

	def run(self):
		while not self.step(): pass
		return self.state()


class Intinstruction:
	opcode = 0
	srcA = 0
	srcB = 0
	dst = 0

	def __init__(self, program, i, rel):
		self.opcode = program[i] % 100
		params = self.__getParams(program[i] // 100)

		while len(program) < (i + 3) + 1:
			program.append(0)

		self.srcA = program[i + 1] + rel if params[0] == 2 else i + 1 if params[0] == 1 else program[i + 1]
		self.srcB = program[i + 2] + rel if params[1] == 2 else i + 2 if params[1] == 1 else program[i + 2]
		self.dst  = program[i + 3] + rel if params[2] == 2 else i + 3 if params[2] == 1 else program[i + 3]

	@staticmethod
	def __getParams(params):
		d = params // 100
		B = params // 10 - 10*d
		A = params - 100*d - 10*B

		return(A, B, d)
