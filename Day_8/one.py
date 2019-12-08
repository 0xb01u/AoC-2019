# -*- coding: utf-8 -*-
# Advent of Code 2019 - Day 8

# Space Image Fomrat
image = open("image.txt", "r").read()

width = 25
height = 6
layers = []

for i in range(len(image))[::width * height]:
	layer = []
	for j in range(width * height):
		layer.append(int(image[i + j]))
	layers.append(layer)

zeroes = [layer.count(0) for layer in layers]
fewest_zeroes = layers[zeroes.index(min(zeroes))]
#print(fewest_zeroes)

print(fewest_zeroes.count(1) * fewest_zeroes.count(2))
