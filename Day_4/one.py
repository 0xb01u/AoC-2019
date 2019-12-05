# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 4

# Password
possible = []

# Range: 123257-647015

# I'm dumb I forgot I could use Strings instead of lists.
def toList(n):
	r = []

	while n > 0:
		r.append(n % 10)
		n //= 10

	return r[::-1]

def asc(l):
	o = l[:]
	o.sort()
	return o == l

def contiguous(l):
	for i in range(1, len(l)):
			if l[i - 1] == l[i]: return True

	return False

for i in range(123257, 647015):
	l = toList(i)
	if asc(l) and contiguous(l):
		possible.append(i)

print("Number of possible password: ", len(possible))
