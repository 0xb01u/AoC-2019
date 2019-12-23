# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 21

# *sigh* more droids
import sys
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

springdroid = Intcomputer(list(map(int, open("springdroid.txt", "r").read().split(","))))
springdroid.run()

l = lambda l: list(map(ord, list(l)))
w = l("WALK\n")
ex = l("NOT C T\nOR D J\nAND T J\nNOT A T\nOR T J\n")

springdroid.input(ex)
springdroid.input(w)

out = springdroid.output()
# s = ""
# for e in out:
# 	if e == 10:
# 		print(s)
# 		s = ""
# 	else: s += chr(e)

print("Hull damage reported:", out[-1])
