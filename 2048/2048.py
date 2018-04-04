#!/bin/python2
import sys

def read_input():
	data = sys.stdin.read().split('\n')
	grid = [line.split(' ') for line in data[:-2]]
	for line in grid:
		for i, cell in enumerate(line):
			line[i] = int(cell)
	return grid, int(data[-2])

def problem():
	grid,direction = read_input()
	if direction == 0:
		grid1 = move_left(grid[:])
	elif direction == 1:
		grid1 = move_up(grid[:])
	elif direction == 2:
		grid1 = move_right(grid[:])
	else:
		grid1 = move_down(grid[:])
	print_grid(grid1)

def transpose(grid):
	return map(list, zip(*grid))

def mirror(grid):
	new = grid
	for i,line in enumerate(grid):
		new[i] = list(reversed(line))
	return new

# basically move left, but by manipulating input does what we want
def move(grid): 
	for idx, line in enumerate(grid):
		tmp_len = len(line)
		line = filter(lambda a: a != 0, line)
		line  += [0]*(tmp_len-len(line))
		i = 0
		while i < len(line)-1:
			if line[i] == line[i+1]:
				line[i] += line[i+1]
				line[i+1] = 0
			i += 1
		line = filter(lambda a: a != 0, line)
		line  += [0]*(tmp_len-len(line))
		grid[idx] = line
	return grid

def move_left(grid):
	return move(grid[:])

def move_up(grid):
	grid = transpose(grid[:])
	grid = move(grid[:])
	return transpose(grid[:])

def move_right(grid):
	grid = mirror(grid[:])
	grid = move(grid[:])
	return mirror(grid[:])

def move_down(grid):
	grid = transpose(grid[:])
	grid = move_right(grid[:])
	return transpose(grid[:])

def print_grid(grid):
	string = ""
	for line in  grid:
		for cell in line:
			string += str(cell) + " "
		string = string[:-1]+"\n"
	print string[:-1]

problem()