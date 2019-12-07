# -*- coding: utf-8 -*-
# Advent of Code 2019 - Intcomputer object
# Wrote after Day 7. Intcomputer puzzles were getting annoying.

class Intcomputer:
	__mem__ = []
	__pc__ = 0
	__indata__ = []
	__outdata__ = []
	__states__ = "RIF"
	__ps__ = __states__[0]

	def __init__(self, program):
		self.__mem__ = program[:]
		self.__indata__ = []
		self.__outdata__ = []

	def input(self, e):
		self.__indata__.extend(e)
		if self.__ps__ == 'I':
			self.__ps__ = self.__states__[0]
			self.step()

	def output(self):
		r = self.__outdata__[:]
		self.__outdata__ = []
		return r

	def __sum__(self, i):
		self.__mem__[i.dst] = self.__mem__[i.srcA] + self.__mem__[i.srcB]
		self.__pc__ -=- 4

	def __prod__(self, i):
		self.__mem__[i.dst] = self.__mem__[i.srcA] * self.__mem__[i.srcB]
		self.__pc__ -=- 4

	def __input__(self, i):
		if len(self.__indata__) > 0:
			self.__mem__[i.srcA] = self.__indata__.pop(0)
			self.__pc__ -=- 2
		else:
			self.__ps__ = self.__states__[1]
			return 1

	def __output__(self, i):
		self.__outdata__.append(self.__mem__[i.srcA])
		self.__pc__ -=- 2

	def __jumpz__(self, i):
		if self.__mem__[i.srcA]: self.__pc__ = self.__mem__[i.srcB]
		else: self.__pc__ -=- 3

	def __jumpnz__(self, i):
		if not self.__mem__[i.srcA]: self.__pc__ = self.__mem__[i.srcB]
		else: self.__pc__ -=- 3

	def __slt__(self, i):
		self.__mem__[i.dst] = int(self.__mem__[i.srcA] < self.__mem__[i.srcB])
		self.__pc__ -=- 4

	def __seq__(self, i):
		self.__mem__[i.dst] = int(self.__mem__[i.srcA] == self.__mem__[i.srcB])
		self.__pc__ -=- 4

	def __halt__(self, i):
		self.__ps__ = self.__states__[2]
		return 1

	__exec__ = {1: __sum__, 2: __prod__, 3: __input__, 4: __output__, 5: __jumpz__, 6: __jumpnz__, 7: __slt__, 8: __seq__, 99: __halt__}

	def step(self):
		if self.__ps__ == 'R':
			instruction = Intinstruction(self.__mem__, self.__pc__)
			return 1 if self.__exec__[instruction.opcode](self, instruction) else 0
		return 1

	def state(self):
		return self.__ps__

	def run(self):
		while not self.step(): pass
		return self.state()


class Intinstruction:
	opcode = 0
	srcA = 0
	srcB = 0
	dst = 0

	def __init__(self, program, i):
		self.opcode = program[i] % 100
		params = self.__getParams__(program[i] // 100)

		while len(program) < (i + 3) + 1:
			program.append(0)

		self.srcA = i + 1 if params[0] else program[i + 1]
		self.srcB = i + 2 if params[1] else program[i + 2]
		self.dst  = i + 3 if params[2] else program[i + 3]

	@staticmethod
	def __getParams__(params):
		d = params // 100
		B = params // 10 - d*10
		A = params - d*100 - B*10

		return(A, B, d)
