# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 8

# Space Image Fomrat
from functools import reduce

image = open("image.txt", "r").read()

width = 25
height = 6
layers = []

for i in range(len(image))[::width * height]:
	layer = []
	for j in range(width * height):
		layer.append(int(image[i + j]))
	layers.append(layer)

# Image decoding:
message = []
for i in range(height):
	row = []
	for j in range(width):
		for k in range(len(layers)):
			pixel = layers[k][i * width + j]
			if pixel != 2:
				row.append(pixel)
				break
	message.append(row)

decode = [reduce(lambda x, y : str(x) + str(y), s) for s in message]

for s in decode:
	print(s.replace("0", " ").replace("1", "X"))
