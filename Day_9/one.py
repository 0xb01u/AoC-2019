# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 9

# BOOST
import sys
sys.path.append("../python_modules/custom")
from intcomputer import Intcomputer

com = Intcomputer(list(map(int, open("boost.txt", "r").read().split(","))))

com.input([1])
com.run()

print("Output:", com.output()[0])
