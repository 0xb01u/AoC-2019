# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 17

# ASCII
from functools import reduce
from os import system
import sys
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

robot = Intcomputer(list(map(int, open("ascii_awoken.txt", "r").read().split(","))))

l = lambda l: list(map(ord, list(l)))
seq = l("A,C,A,C,B,B,C,A,C,B\n")
A = l("L,12,L,10,R,8,L,12\n")
B = l("L,10,R,12,R,8\n")
C = l("R,8,R,10,R,12\n")
yes = l("y\n")
no = l("n\n")

#print(seq, A, B, C, yes, no)

robot.input(seq)
robot.input(A)
robot.input(B)
robot.input(C)
robot.input(no)

robot.run()

out = robot.output()
view = ""
row = ""

for n in out:
	row += chr(n)
	if n == 10:
		view += row
		row = ""
print(view)


print("Dust collected:", out[-1])
