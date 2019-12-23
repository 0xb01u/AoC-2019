# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 21

# *sigh* more droids
import sys
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

springdroid = Intcomputer(list(map(int, open("springdroid.txt", "r").read().split(","))))
springdroid.run()

l = lambda l: list(map(ord, list(l)))
w = l("RUN\n")
ex = l("NOT F J\nOR E J\nOR H J\nAND D J\nNOT C T\nAND T J\nNOT D T\nOR B T\nOR E T\nNOT T T\nOR T J\nNOT A T\nOR T J\n")

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
