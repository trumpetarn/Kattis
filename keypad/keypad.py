import sys
#import numpy as np

def create_grid(grid_data,r,c):
	grid = []
	for i in range(0,r):
		grid.append([])
		for j in range(0,c):
			grid[i].append(int(grid_data[i][j]))
	return grid #np.matrix(grid)

def run_test(grid,r,c):
	string = ""
	rows = []
	cols = [0]*c
	for i in range(0,r):
		rows.append(sum(grid[i]))
		for j in range(0,c):
			cols[j] += grid[i][j]
	for i in range(0,r):
		for j in range(0,c):
			if rows[i] == 0  or cols[j] == 0:
				string += "N"
			elif rows[i] == cols[j] == 1:
				return "impossible"
			elif rows[i] > 1 and cols[j] == 1:
				string += "P"
			elif rows[i] == 1 and cols[j] > 1:
				string += "P"
			elif rows[i] > 1 and cols[j] > 1:
				string += "I"
			else:
				return "impossible"
		string += '\n'
	return string[:-1]

def testcase(indata):
	rxc = indata[0].split(' ')
	r = int(rxc[0])
	c = int(rxc[1])
	grid = create_grid(indata[1:r+1],r,c)
	print run_test(grid,r,c)
	return r+1

input_data = sys.stdin.read().split('\n')
num_testcases = int(input_data[0])
j = 1
for i in range(0,num_testcases):
	j += testcase(input_data[j:])
	print "----------"

sys.exit(0)