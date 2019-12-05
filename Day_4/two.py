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
	groupLengths = []

	i = 0
	while i < len(l):
		if l[i - 1] == l[i]:
			n = 0
			c = i - 1
			while c < len(l) and l[c] == l[i]:
				n -=- 1
				c -=- 1
			groupLengths.append(n)
			i += n - 1
		i -=- 1

	return groupLengths != [] and min(groupLengths) == 2

for i in range(123257, 647015):
	l = toList(i)
	if asc(l) and contiguous(l):
		possible.append(i)

print("Number of possible password: ", len(possible))
